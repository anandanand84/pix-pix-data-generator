import numpy as np
import scipy.ndimage
import cv2
import os

photo_count = 1
while photo_count < 2500:
    photo_count = photo_count + 1
    if os.path.isfile('out/'+str(photo_count)+'.jpeg'):
        img = scipy.ndimage.imread('out/'+str(photo_count)+'.jpeg')
        img = img[:400, :400]
        imgnoised = scipy.ndimage.imread('out/noised/'+str(photo_count)+'.jpeg')
        imgnoised = imgnoised[:400, :400]
        scipy.misc.imsave('out/'+str(photo_count)+'.jpeg', img)
        scipy.misc.imsave('out/noised/'+str(photo_count)+'.jpeg', imgnoised)
    pass