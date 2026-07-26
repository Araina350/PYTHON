import cv2 as c
import matplotlib.pyplot as plt
image = c.imread('scenery.jpeg')
image_rgb = c.cvtColor(image,c.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("Image RGB")
plt.show()
gray_scale = c.cvtColor(image,c.COLOR_BGR2GRAY)
plt.imshow(gray_scale,cmap='gray')
plt.title("Gray scale image")
plt.show()
cropped_image = image[100:3000000,200:4000000]
cropped_rgb = image_rgb = c.cvtColor(cropped_image,c.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()