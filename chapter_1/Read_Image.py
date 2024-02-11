# Importing the OpenCV library
import cv2

# Printing a message indicating that the package is imported
print("Package Imported")

# Reading an image from the specified file
img = cv2.imread("./Resources/lena.png")

# Displaying the image in a window named "Output"
cv2.imshow("Output", img)

# Waiting for a key press before closing the window
cv2.waitKey(0)

'''
*** NOTE ***
    In the .waitKey function, if you pass the value 0, the window will remain open indefinitely.
    However, if you input a value other than zero, the window will be open for the specified duration in milliseconds.
'''