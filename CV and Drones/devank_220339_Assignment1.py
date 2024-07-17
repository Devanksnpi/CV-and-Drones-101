import cv2
import matplotlib.pyplot as plt
import numpy as np


def fourier(img):
    F=np.fft.fft2(img)
    fshift=np.fft.fftshift(F)
    return fshift


def inv_fourier(fshift):
    a=np.fft.ifftshift(fshift)
    return np.abs(np.fft.ifft2(a))


def ideal_filter(shape, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2

    filter = np.zeros((rows, cols), np.uint8)
    filter[int(crow - cutoff):int(crow + cutoff), int(ccol - cutoff):int(ccol + cutoff)] = 1
    
    return filter


def hybrid(s1,s2):
    img1=cv2.imread(s1,0)
    img2=cv2.imread(s2,0)
    img1=cv2.resize(img1,(256,256))
    img2=cv2.resize(img2,(256,256))
    
    FT_1 = fourier(img1)
    FT_2 = fourier(img2)
    
    lpf=ideal_filter((256,256),30)
    hpf=1-ideal_filter((256,256),20)
    filtered_ft_1=FT_1*lpf
    filtered_ft_2=FT_2*hpf
    filt_img1=inv_fourier(filtered_ft_1)
    filt_img2=inv_fourier(filtered_ft_2)
    hybrid_img = (filt_img1+filt_img2)/2

    fig,ax=plt.subplots(2,5,figsize=[10,10])
    images=[img1,np.log1p(np.abs(FT_1)),lpf,np.log1p(np.abs(filtered_ft_1)),img2,np.log1p(np.abs(FT_2)),hpf,np.log1p(np.abs(filtered_ft_2))]
    labels=['Image 1','FT of Img1','LPF applied','FT after LPF','Image 2','FT of Img2','HPF applied','FT after HPF']

    for i in range(2):
        for j in range(4):
            ax[i,j].imshow(images[4*i+j],cmap='gray')
            ax[i,j].axis('on')
            ax[i,j].set_xticks([])
            ax[i,j].set_yticks([])
            ax[i,j].set_title(labels[4*i+j])

    ax[0,4].imshow(hybrid_img,cmap='gray')
    ax[0,4].axis('on')
    ax[0,4].set_xticks([])
    ax[0,4].set_yticks([])
    ax[0,4].set_title('Hybrid Image')
    fig.delaxes(ax[1,4])
    plt.show()

    return hybrid_img