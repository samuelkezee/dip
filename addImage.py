import cv2

# Load the two images
image1 = cv2.imread('image.jpeg')
image2 = cv2.imread('image2.jpg')

# Ensure both images have the same dimensions
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Add the images together
result = cv2.add(image1, image2)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
