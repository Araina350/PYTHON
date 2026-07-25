import cv2
image = cv2.imread('scenery.jpeg')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resize_image = cv2.resize(gray_image,(224,224))
cv2.imshow('Processed image',resize_image) 
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayscale_resized_image.jpeg',resize_image)
    print("Image saved as'grayscale_resized_image.jpeg'")
else:
    print("Image not saved")
cv2.destroyAllWindows()
print(f"Processed image dimensions: {resize_image.shape}")        