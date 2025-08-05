from flask import Flask, Response, render_template_string
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np

app = Flask(__name__)

# Initialize PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
raw_capture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)  

# Kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(7, 7))
    cl1 = clahe.apply(gray)

    # Median Blur
    cl2 = cv2.medianBlur(cl1, 5)

    # Adaptive thresholding
    th1 = cv2.adaptiveThreshold(cl2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY_INV, 25, 2.55)

    # Gaussian + Otsu
    blur = cv2.GaussianBlur(cl1, (5, 5), 0)
    _, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Combine both
    th2 = th1 & th3

    # Morphological opening
    opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)

    # Contour detection
    contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Draw contours
    img_contour = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(img_contour, contours, -1, (0, 255, 0), 2)

    return img_contour

def generate_frames():
    for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
        image = frame.array
        processed = process_frame(image)

        # Encode as JPEG
        ret, buffer = cv2.imencode('.jpg', processed)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        raw_capture.truncate(0)  

@app.route('/')
def index():
    return render_template_string('''
        <html>
        <head>
            <title>Live Video Stream</title>
        </head>
        <body>
            <h2>Live Processed Stream from Raspberry Pi</h2>
            <img src="{{ url_for('video_feed') }}" width="640" height="480">
        </body>
        </html>
    ''')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)   #run on the device connected to same network as pi
