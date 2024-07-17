import cv2
import numpy as np
import matplotlib.pyplot as plt

def shape(s):
    img = cv2.imread(s)
    cpy=img.copy()
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgGry=cv2.GaussianBlur(imgGry,(3,3),0)
    _, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
    contours , _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max1=-1
    max2=-2

    max1_cx, max1_cy=0,0
    max2_cx, max2_cy=0,0
    for contour in contours:

        ar=cv2.contourArea(contour)

        # cv2.approxPloyDP() function to approximate the shape 
        approx = cv2.approxPolyDP( 
            contour, 0.01 * cv2.arcLength(contour, True), True) 
        
        # using drawContours() function 
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 5) 
    
        # finding center point of shape 
        M = cv2.moments(contour) 
        if M['m00'] != 0.0: 
            x = int(M['m10']/M['m00']) 
            y = int(M['m01']/M['m00']) 

        #For finding the maximum and seconnd maximum shape wrt area
        if ar>max1:
            max1=ar;max2=max1
            max2_cx,max2_cy=max1_cx,max1_cy
            max1_cx,max1_cy=x,y
        elif ar<max1 and ar>max2:
            max2=ar;max2_cx,max2_cy=x,y


        # putting shape name at center of each shape 
        if len(approx) == 3: 
            cv2.putText(img, 'Triangle', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2) 
        elif len(approx) == 4 :
            _,_ , w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            if aspectRatio >= 0.95 and aspectRatio < 1.05:
                cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0),2)
            else: cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0),2)
    
        elif len(approx) == 5: 
            cv2.putText(img, 'Pentagon', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2) 
    
        elif len(approx) == 6: 
            cv2.putText(img, 'Hexagon', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2) 
        
        elif len(approx) == 7: 
            cv2.putText(img, 'Heptagon', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
            
        elif len(approx) == 8: 
            cv2.putText(img, 'Octagon', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
            
        elif len(approx) == 9: 
            cv2.putText(img, 'Nonagon', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    
        else: 
            cv2.putText(img, 'circle', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
            
    cv2.putText(img, 'largest1', (max1_cx,max1_cy-20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),2)
    cv2.putText(img, 'largest2', (max2_cx,max2_cy-20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),2)

    _, ax=plt.subplots(1,2,figsize=[10,5])
    ax[0].imshow(cpy[:,:,::-1]);ax[0].set_xticks([]);ax[0].set_yticks([]);ax[0].set_title('Input')
    ax[1].imshow(img[:,:,::-1]);ax[1].set_xticks([]);ax[1].set_yticks([]);ax[1].set_title('Output')
    plt.show()

    return img
