import cv2
import numpy as np

def aruco_display(corners,ids,rejected,image):
	if(len(corners)>0):
		ids=ids.flatten()
		for(markerCorner,markerID) in zip(corners,ids):
			corners=markerCorner.reshape((4,2))
			(topLeft,topRight,bottomRight,bottomLeft)=corners
			topRight=(int(topRight[0]),int(topRight[1]))
			topLeft=(int(topLeft[0]),int(topLeft[1]))
			bottomRight=(int(bottomRight[0]),int(bottomRight[1]))
			bottomLeft=(int(bottomLeft[0]),int(bottomLeft[1]))
			cv2.line(image,topLeft,topRight,(0,255,0),2)
			cv2.line(image,topRight,bottomRight,(0,255,0),2)
			cv2.line(image,bottomRight,bottomLeft,(0,255,0),2)
			cv2.line(image,bottomLeft,topLeft,(0,255,0),2)
			cX=int((topLeft[0]+bottomRight[0]+topRight[0]+bottomLeft[0])/4)
			cY=int((topLeft[1]+bottomLeft[1]+bottomRight[1]+topRight[1])/4)
			cv2.circle(image,(cX,cY),4,(0,0,255),-1)
			print(str(image.shape[0])+'x'+str(image.shape[1]))
			print("[Inference] Aruco marker ID: {}".format(markerID))

	return image

cap=cv2.VideoCapture(0)
    
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while cap.isOpened():
	ret,img=cap.read()
	h,w,_=img.shape
	width=500
	height=int(width*(h/w))
	img=cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)
	arucoDict=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
	arucoParams=cv2.aruco.DetectorParameters()
	detector = cv2.aruco.ArucoDetector(arucoDict,arucoParams)
	corners,ids,rejected=detector.detectMarkers(img)
	detected_markers=aruco_display(corners,ids,rejected,img)
	cv2.imshow("Image",detected_markers)
	# cv2.aruco.drawDetectedMarkers(img, corners)
	# cv2.imshow("Image", img)

	key=cv2.waitKey(10)

	if key == 27:
		break
cv2.destroyAllWindows()
cap.release()
