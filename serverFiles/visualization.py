import os
import cv2
import numpy as np

def read_signal():
	file1 = open("commands_read.txt", "r")
	print("Output of Readlines after writing")
	#print(f"Signal recieve from txt: {file1.read()}")
	signal = file1.readlines()
	file1.close()
	return signal

def visualize():
	i = 0
	while True:
		orig_img_path = "img_data/img"+str(i)+".png"
		#orig_img_path = "FirstComb/orignal_images_iter1/img"+str(i)+".png"
		segmented_img_path = "seg_imgs/"+"img_"+str(i)+"/img"+str(i)+".png"
		isOrig = os.path.isfile(orig_img_path)
		isSeg = os.path.isfile(segmented_img_path)
		print(f"Signal is: {i}")
		#print(f"original_ex: {isOrig}\n Seg exist: {isSeg}")
		if isOrig and isSeg:
			print("Both path found")
			orig_img = cv2.imread(orig_img_path)
			seg_img = cv2.imread(segmented_img_path)
			# concatenate image Horizontally
			both_img = np.concatenate((orig_img, seg_img), axis=1)
			sig = read_signal()
			#print(sig)
			title_name = "Command: " + sig[i][:len(sig[i])-1]
			print(f"Command is: {title_name} and Signal is: {i}")
			i += 1
			# Using cv2.putText() method
			both_img = cv2.putText(both_img, title_name, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
			cv2.imshow(title_name, both_img)
					
			cv2.waitKey(1000)
			



if __name__=="__main__":
	visualize()
