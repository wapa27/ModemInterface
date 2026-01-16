from flask import Flask, request, jsonify
import serial
from serial.tools import list_ports

app = Flask(__name__)

def find_serial_port():
    ports = list_ports.comports()
    for p in ports:
        # Print once during dev to see what's available
        print(p.device, p.vid, p.pid, p.manufacturer, p.description)

        # Example matching logic — adjust for your device
        if p.description == 'USB-Serial Controller':          # example VID
            return p.device

    raise RuntimeError("Target serial device not found")

def open_serial():
    port = find_serial_port()
    return serial.Serial(port, 115200, timeout=1)

@app.route('/passCounts', methods=['POST'])
def write_to_serial():
    ser = None
    try:
        ser = open_serial()

        data = request.get_json()
        print(data)
        if not data or 'message' not in data:
            return jsonify({"status": "error", "message": "Missing 'message'"}), 400

        command = f"AT$APP msg {data['message']}\r"
        ser.write(data['message'].encode('ascii'))
        response = ser.read(100)

        return jsonify({
            "status": "success",
            "response": response.decode(errors="ignore")
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        if ser and ser.is_open:
            ser.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
