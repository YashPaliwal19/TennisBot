from ultralytics import YOLO

#model.predict(source="1.png", show=True, save=True, show_labels=True, show_conf=True, conf=0.5, save_txt=False, save_crop=False, line_thickness=2)

def infer_ball(image,i):
	model = YOLO("best.pt")
	results = model.predict(image, save=True, project="seg_imgs", name="img_"+str(i))
	#print(f"The _keys is {results[0].boxes.boxes}")
	conf = -1
	if len(results[0].boxes.boxes)!=0:
		conf = results[0].boxes.boxes[0][4]
	print(f"Confidence score is: {conf}")
	#print(len(results))
	if conf<=0.8:
		print("No predictions")
		return (-1,-1,-1,-1)
	else:
		print("ball detected")
		ans = results[0].boxes[0].xywh
		x_c, y_c, w, h = ans[0]
		print(f"my result in terms of x_c, y_c, w, h: {x_c},{y_c},{w},{h}")
		return (x_c, y_c, w, h)

if __name__=="__main__":
	image = "img387.jpg"
	x = infer_ball(image,1)
