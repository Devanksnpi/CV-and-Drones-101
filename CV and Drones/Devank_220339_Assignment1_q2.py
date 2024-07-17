import cv2
import numpy as np

def Sobel(s):
    img = cv2.imread(s,0)
    grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    grad = np.sqrt(grad_x**2 + grad_y**2)
    grad_norm = (grad * 255 / grad.max()).astype(np.uint8)

    final_frame = cv2.hconcat((img, grad_norm))
    cv2.imshow('Original vs Filtered', final_frame)
    cv2.waitKey(0)

    return grad_norm
