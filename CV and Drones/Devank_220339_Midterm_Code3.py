import numpy as np
import matplotlib.pyplot as plt
import cv2

def colour(s):

    img = cv2.imread(s)
    temp=img.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(temp, contours_blue, -1, (0, 255, 0), 5)

    images = [img[:,:,::-1],temp[:,:,::-1]]
    labels = ['Input Image','Blue Color Detected']
    _,ax=plt.subplots(1,2,figsize=[10,5])
    for i in range(2):
        ax[i].imshow(images[i])
        ax[i].set_title(labels[i])
        ax[i].set_xticks([]);ax[i].set_yticks([])

    plt.show()

    return temp

