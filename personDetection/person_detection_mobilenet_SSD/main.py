# USAGE
# python deep_learning_object_detection.py --image images/example_01.jpg \
#	--prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages
import numpy as np
import sys
import cv2
import time
import sys
sys.path.append('/home/ac/AOD-Net/test')
import test_changes

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt"
, "MobileNetSSD_deploy.caffemodel")
#start = time.time()
# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
# (note: normalization is done via the authors of the MobileNet SSD
# implementation)
v = cv2.VideoCapture('/home/ac/esdc/personDetection/video2.mp4')
#v = cv2.VideoCapture(2)
#v = cv2.VideoCapture('/home/ac/AOD-Net/test/Dehaze.mp4')


def video():
	#frame = 120
	#start = time.time()
	while (True):
	#for i in xrange(frame):

		ret, image = v.read()
		image = cv2.resize(image, (500,500))
	#	image = test_changes.AOD_Net_final(image)

	#	image = np.uint8(np.array(image)*255.0) 
		(h, w) = image.shape[:2]

		blob = cv2.dnn.blobFromImage(cv2.resize(image, (280, 280)), 0.007843, (280, 280), 127.5)
	#fps can be controled from here dude..just change the blob input size
	# pass the blob through the network and obtain the detections and
	# predictions
		
		net.setInput(blob)
		detections = net.forward()
		print "the detection is ", detections.shape

	# loop over the detections
		for i in np.arange(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with the
		# prediction

			confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
			if confidence > 0.1:
			# extract the index of the class label from the `detections`,
			# then compute the (x, y)-coordinates of the bounding box for
			# the object
				idx = int(detections[0, 0, i, 1])
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
	#			image =image.copy()
			# display the prediction
				label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
				print("[INFO] {}".format(label))
				if CLASSES[idx]  == "person":
					cv2.rectangle(image, (startX, startY), (endX, endY),
						COLORS[idx], 2)
					y = startY - 15 if startY - 15 > 15 else startY + 15
					#cv2.putText(image, label, (startX, y),
						#cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
		cv2.imshow("Output", image)
		key = cv2.waitKey(1)
	    
	        if key & 0xFF == ord('q'):
	             break
	#end = time.time()
	#print "fps : ", (frame/(end-start))
	# show the output image
def image():
	start = time.time()
	image = cv2.imread(sys.argv[1])
	(h, w) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

	# pass the blob through the network and obtain the detections and
	# predictions

	net.setInput(blob)
	detections = net.forward()
	#print "the detection is ", detections.shape

	# loop over the detections
	for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > 0.2:
			# extract the index of the class label from the `detections`,
			# then compute the (x, y)-coordinates of the bounding box for
			# the object
			idx = int(detections[0, 0, i, 1])
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# display the prediction
			label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
		
			if CLASSES[idx]  == "person":
				cv2.rectangle(image, (startX, startY), (endX, endY),
					COLORS[idx], 2)
				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(image, label, (startX, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
	end = time.time()
	print "the time elapsed is : ", (end-start)
	# show the output image
	#cv2.imwrite("Output.jpg", image
	cv2.imshow("image",image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	video()
