# Pranjul Shikhar Verma
# 220797
# Assignment 2- Question 1

import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate():
    img = np.zeros((600,600,3), dtype=np.uint8)

    white=[255,255,255]
    saffron=[255,153,51]
    green=[19,136,8]

    img[:200,:,:]=saffron
    img[200:400,:,:]=white
    img[400:,:,:]=green

    spokes=24
    radius=100
    theta=np.linspace(0,2*np.pi,spokes,endpoint=False)

    for angle in theta:
        x=int(300+radius*np.cos(angle))
        y=int(300+radius*np.sin(angle))
        cv2.line(img,(300,300),(x,y),(0,0,128), thickness=1)

    cv2.circle(img, (300,300),100,(0,0,128),thickness=2)

    if __name__=="__main__":
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    return img