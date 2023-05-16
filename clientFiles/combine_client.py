import socket
from take_action import post_process_command
import time
import io
import struct
import time
import picamera
import Adafruit_PCA9685 # Import the library used to communicate with PCA9685
from adafruit_servokit import ServoKit

def client_program():
    command_list = []
    host = "192.168.163.120"
    port = 7000
    
    client_socket = socket.socket()
    client_socket.connect((host, port))

    connection = client_socket.makefile('wb')
    camera = picamera.PiCamera()
    camera.vflip = False
    camera.resolution = (640, 480)
    stream = io.BytesIO()
    for foo in camera.capture_continuous(stream, 'jpeg'):
        # Write the length of the capture to the stream and flush to
        # ensure it actually gets sent
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()
        # Rewind the stream and send the image data over the wire
        stream.seek(0)
        connection.write(stream.read())
        # Reset the stream for the next capture
        stream.seek(0)
        stream.truncate()
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        post_process_command(data)
        command_list.append(data)
        time.sleep(0.7)
        ## After sending an image
            
        # Write a length of zero to the stream to signal we're done
    connection.write(struct.pack('<L', 0))
    client_socket.close()
    
if __name__=="__main__":
    client_program()
