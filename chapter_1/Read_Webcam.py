# Importing the OpenCV library
import cv2

# Capturing video from the default camera (0)
cap = cv2.VideoCapture(0)

# Setting the width of the captured video frame to 640 pixels
cap.set(3, 640)

# Setting the height of the captured video frame to 480 pixels
cap.set(4, 480)

# Setting the brightness of the captured video to 100 (if supported by the camera)
cap.set(10, 100)

# Loop to continuously capture frames from the camera
while True:
    # Read a frame from the video capture object
    success, img = cap.read()

    # Display the captured frame in a window named "video"
    cv2.imshow("video", img)

    # Check for the 'q' key press to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


'''
The list below includes numerical IDs that you can use as parameters for the ".set" function:

        0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
        1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
        2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
        3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
        4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
        5. CV_CAP_PROP_FPS Frame rate.
        6. CV_CAP_PROP_FOURCC 4-character code of codec.
        7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
        8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
        9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
        10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
        11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
        12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
        13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
        14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
        15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
        16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
        17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
        18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

*** Note ***
    Not all parameters are supported by all cameras - actually, they are one of the most troublesome part of the OpenCV library.
    Each camera type - from android cameras to USB cameras to professional ones offer a different interface to modify its parameters.
    There are many branches in OpenCV code to support as many of them, but of course not all possibilities are covered.
'''