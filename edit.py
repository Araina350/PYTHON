import cv2 as c
import numpy as np
import matplotlib.pyplot as plt
image = c.imread('scenery.jpeg')
gray_image = c.cvtColor(image,c.COLOR_BGR2GRAY)
(h,w) = image.shape[:2]
center = (w//2,h//2)
M = c.getRotationMatrix2D(center,45,1.0)
rotated = c.warpAffine(image,M,(w,h))
rotated_rgb = c.cvtColor(rotated,c.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated image")
plt.show()
brightness_matrix = np.ones(image.shape,dtype='uint8')*50
brighter = c.add(image,brightness_matrix) 
brighter_rgb = c.cvtColor(brighter,c.COLOR_BGR2GRAY)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()