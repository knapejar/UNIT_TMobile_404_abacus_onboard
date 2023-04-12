import cv2
import numpy as np

# Generate a random NumPy array
arr = np.random.rand(256, 256)

# Scale the array to the range [0, 255]
arr = (arr * 255).astype(np.uint8)

# Save the array as an image in shades of gray
cv2.imwrite("gray_image.jpg", arr)