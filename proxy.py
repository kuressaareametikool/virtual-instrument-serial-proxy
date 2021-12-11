from serial import Serial
import socketio

serial_port_name = 'COM3'
URL = "http://localhost:8000"

sio = socketio.Client()

# arduino = Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
serial_port = Serial(port=serial_port_name, baudrate=9600, timeout=.1)

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')
    
sio.connect(URL)

while True:
    key, value = serial_port.readline().decode('utf-8').strip().split()
    
    if value:
        print('Key:', key, 'Value:', value)
        sio.emit('send-data', {'key': key, 'value': value})
  




