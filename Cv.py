import cv2
image = cv2.imread('scenery.jpeg')
cv2.namedWindow('loaded image',cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded window",500,800)
cv2.imshow('Loaded Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Image Dimesions: ",image.shape)