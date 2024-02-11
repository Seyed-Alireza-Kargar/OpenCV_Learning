# Importing the OpenCV library
import cv2

# Creating a video capture object and reading video from the specified file
cap = cv2.VideoCapture("./Resources/test_video.mp4")

# Loop to continuously read frames from the video file
while True:
    # Read a frame from the video capture object
    success, img = cap.read()

    # Display the captured frame in a window named "video"
    cv2.imshow("video", img)

    # Check for the 'q' key press to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
