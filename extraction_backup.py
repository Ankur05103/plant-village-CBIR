import numpy as np
import os
from skimage import io, img_as_ubyte
from skimage.transform import resize
import h5py
from skimage.filters import roberts, sobel
from skimage.color import rgb2lab, rgb2gray
from skimage.filters.rank import entropy
from skimage.morphology import disk

def extract_features(img):
    LAB_img = rgb2lab(img)
    A_img = LAB_img[:,:,1]
    A_feat = A_img.mean()
    
    B_img = LAB_img[:,:,2]
    B_feat = B_img.mean()
    

    
    gray_img = rgb2gray(img) 
    gray_img = resize(gray_img, (256,256)) 
    gray_img = img_as_ubyte(gray_img)
   
    #entropy
    entropy_img = entropy(gray_img, disk(3))
    entropy_mean = entropy_img.mean()
    entropy_std = entropy_img.std()
    
    roberts_img = roberts(gray_img)
    roberts_mean = roberts_img.mean()

    sobel_img = sobel(gray_img)
    sobel_mean = sobel_img.mean()
    
    custom_features = np.array([A_feat, B_feat, entropy_mean, entropy_std, roberts_mean, 
                                sobel_mean])
    
    return custom_features