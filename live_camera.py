from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

def nothing(x):
    pass

# Open dummy webcam for GUI (required for trackbar)
cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('CLimit', 'image', 0, 8, nothing)

# PiCamera init
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Let camera warm up
time.sleep(0.1)

# Main loop to capture frames
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get current trackbar value (CLAHE clip limit)
    p = cv2.getTrackbarPos('CLimit', 'image')
    r = 0.5 + (p / 2)

    # Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=r, tileGridSize=(9, 9))
    cl1 = clahe.apply(gray)

    cv2.imshow("image", cl1)
    k = cv2.waitKey(1) & 0xFF

    if k == ord("a")
        cv2.imwrite(time.strftime("Screenshot%Y%m%d%H%M%S.jpg"), cl1)
        cv2.imwrite("temp.jpg", cl1)
        break

    if k == ord("q"):
        break

    rawCapture.truncate(0)

cap.release()
cv2.destroyAllWindows()
