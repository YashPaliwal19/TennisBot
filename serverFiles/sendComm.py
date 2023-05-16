from predict import infer_ball

def send_signal(result):
	w_input = 640
	h_input = 480
	message = ""
	# ball is not detected
	if result[0]==-1:
		# send 45 degree as signal
		angle = 45
		message = "NoBall"
		print("No ball is detected")
	else:
	# Ball is detected
		print("ball is detected")
		x_c, y_c, w, h = result
		# ball range is image is 200
		one_side_px_forward = 100
		angle_to_rotate = 10
		if x_c>124 and x_c<435:
		# Move forward
			ratio = (w*h)/(w_input*h_input)
			if ratio>=0.22:
			# To grab
				message = "Grab"
			elif ratio>=0.1 and ratio<0.22:
				message = "lForward"
				print("Move less forward")
			else:
				message = "mForward"
				print("Move more forward")
		
		elif x_c<=124:
		# rotate left
			message = "Left"
			print("Left")
			
		elif x_c>=435:
		# rotate right
			message = "Right"
			print("right")
			
		print(f"message is: {message}")
	return message	

if __name__=="__main__":
	i = 10
	img_path = "img_data/img"+str(i)+".png"
	results = infer_ball(img_path)
	mess = send_signal(results)
