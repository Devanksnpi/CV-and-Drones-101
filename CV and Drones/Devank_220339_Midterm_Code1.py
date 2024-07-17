import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance

def ig_filter(s):
    img = Image.open(s)
    bri = ImageEnhance.Brightness(img)
    img1 = bri.enhance(0.5)
    cont=ImageEnhance.Contrast(img1)
    img2=cont.enhance(1.5)
    sat=ImageEnhance.Color(img2)
    final_img=sat.enhance(1.5)
    print("Filters applied successfully")

    _,ax=plt.subplots(1,2)
    ax[0].imshow(img);ax[0].axis('off');ax[0].set_title('Original')
    ax[1].imshow(final_img);ax[1].axis('off');ax[1].set_title('Filtered')
    plt.show()
    return np.array(final_img)