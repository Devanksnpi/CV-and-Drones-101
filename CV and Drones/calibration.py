import numpy as np
import cv2 as cv
import glob

chessboardsize = (8,6)
frameSize = (640,480)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,30,0.001)

objp = np.zeros((chessboardsize[0]*chessboardsize[1],3), np.float32)
objp[:,:2]=np.mgrid[0:chessboardsize[0],0:chessboardsize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm=20
objp=objp*size_of_chessboard_squares_mm

objpoints=[]
imgpoints=[]

images = glob.glob('./calibration/images/*.jpeg')
for image in images:
    img = cv.imread(image)
    cpy=img.copy()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    ret, corners = cv.findChessboardCorners(gray, chessboardsize, None)

    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        cv.drawChessboardCorners(img, chessboardsize, corners2,ret)
        img=cv.resize(img,(500,500))
        cpy=cv.resize(cpy,(500,500))
        cv.imshow('input',cpy)
        cv.imshow('output',img)

        cv.waitKey(0)

cv.destroyAllWindows()

ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints,imgpoints,frameSize,None,None)
print(cameraMatrix)