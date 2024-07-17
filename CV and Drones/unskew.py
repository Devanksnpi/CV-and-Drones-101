#Pranjul Shikhar Verma
#220797
#Assignment2 - Code3

import cv2
import numpy as np
from flag import generate
import matplotlib.pyplot as plt

saffron = np.array([52, 153, 255])
green = np.array([1, 128, 0])
white = np.array([255,255,255])

def first_vertical_color(img: np.ndarray):
    h,w,_=img.shape
    for i in range(h):
        if np.array_equal(img[i][w//2],saffron): return "saffron"
        elif np.array_equal(img[i][w//2],green): return "green"
        elif np.array_equal(img[i][w//2],white): return "white"

def first_horizontal_color(img: np.ndarray):
    h,w,_=img.shape
    for i in range(w):
        if np.array_equal(img[h//2][i],saffron): return "saffron"
        elif np.array_equal(img[h//2][i],green): return "green"
        elif np.array_equal(img[h//2][i],white): return "white"

def unskew(s):
    img = cv2.imread(s)
    plt.figure("Input Image", figsize=[5,3])
    plt.imshow(img[:,:,::-1])
    plt.figure("Unskewed Image",figsize=[5,3])
    if first_vertical_color(img)=="saffron":
        plt.imshow(generate())
    elif first_vertical_color(img)=="green":
        plt.imshow(cv2.rotate(src=generate(),rotateCode=cv2.ROTATE_180))
    elif first_vertical_color(img)=="white" and first_horizontal_color(img)=="saffron":
        plt.imshow(cv2.rotate(src=generate(),rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE))
    elif first_vertical_color(img)=="white" and first_horizontal_color(img)=="green":
        plt.imshow(cv2.rotate(src=generate(),rotateCode=cv2.ROTATE_90_CLOCKWISE))
    else: print("No Indian Flag detected")

    plt.show()
