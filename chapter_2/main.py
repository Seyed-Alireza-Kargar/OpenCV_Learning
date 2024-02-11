# Importing necessary libraries
import cv2
import numpy as np

# Reading an image from the specified file
img = cv2.imread("./Resources/lena.png")

# Creating a kernel for morphological operations (Dilation and Erosion)
kernel = np.ones((5, 5), np.uint8)

# Converting the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying Gaussian blur to the grayscale image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# Detecting edges in the image using the Canny edge detector
imgCanny = cv2.Canny(img, 150, 250)

# Dilating the edges to make them thicker
imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)

# Eroding the dilated image to revert it closer to the original edges
imgEroded = cv2.erode(imgDialation, kernel, iterations=2)

# Displaying the processed images in separate windows
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

# Waiting for a key press before closing the windows
cv2.waitKey(0)
