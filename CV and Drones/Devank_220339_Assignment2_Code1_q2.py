import cv2
import numpy as np
import matplotlib.pyplot as plt
from flag import generate

def rotate(img: np.ndarray, y):
    rows,cols,_= img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),y,1) 
    rotated = cv2.warpAffine(img,M,(cols,rows))
    return rotated

def rotatedFlags():
    flag = generate()
    images = [flag]
    for y in [90,180,270]:
        rotated=rotate(flag,y)
        images.append(rotated)

    _, ax=plt.subplots(2,2)
    for i in range(2):
        for j in range(2):
            ax[i][j].imshow(images[2*i+j])
            ax[i][j].set_title(f"{(2*i+j)*90} degree")
            ax[i][j].axis('off')
    
    plt.show()