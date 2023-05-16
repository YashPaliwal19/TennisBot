import socket
from predict import infer_ball
from sendComm import send_signal
import io
import struct
from PIL import Image
import matplotlib.pyplot as pl
import time
from visualization import visualize


def write_file(data, i):
	if i==0:
		file1 = open("commands_read.txt", "w")  # append mode
	else:
		file1 = open("commands_read.txt", "a")
	file1.write(data+"\n")
	file1.close()

def server_program():
	# get the hostname
	host = "192.168.163.120"
	port = 7000  # initiate port no above 1024

	server_socket = socket.socket()  # get instance
	# look closely. The bind() function takes tuple as argument
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((host, port))  # bind host address and port together

	# configure how many client the server can listen simultaneously
	server_socket.listen(2)
	conn, address = server_socket.accept()  # accept new connection
	# Accept a single connection and make a file-like object out of it
	connection = conn.makefile('rb')
	print("Connection from: " + str(address))
	i = 0
	img = None
	
	while True:
		# Camera read
		image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
		if not image_len:
			break
		image_stream = io.BytesIO()
		image_stream.write(connection.read(image_len))
		# Rewind the stream, open it as an image with PIL and do some
		# processing on it
		image_stream.seek(0)
		image = Image.open(image_stream)

		if img is None:
		    img = pl.imshow(image)
		else:
		    img.set_data(image)

		#pl.pause(0.01)
		pl.draw()
		pl.savefig("img_data/img"+str(i)+".png")
	
		img_path = "img_data/img"+str(i)+".png"
		results = infer_ball(img_path,i)
		#print(f"results are")
		data = send_signal(results)
		write_file(data, i)
		print(f"Image processed: {i}")
		
		conn.send(data.encode())  # send data to the client
		i+=1
	conn.close()  # close the connection
    
if __name__=="__main__":
	server_program()
