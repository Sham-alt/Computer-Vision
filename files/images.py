import cv2

# Load the image from the Images folder
img = cv2.imread('Images/sample_image.jpg')

# Display the image
cv2.imshow('Loaded Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
