import cv2
import numpy as np

# Load the two images
image1 = cv2.imread('image.jpeg').astype(np.float32)
image2 = cv2.imread('image2.jpg').astype(np.float32)

# Ensure both images have the same dimensions
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Multiply the images
result = cv2.multiply(image1, image2)

# Convert the result back to uint8
result = result.astype(np.uint8)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
