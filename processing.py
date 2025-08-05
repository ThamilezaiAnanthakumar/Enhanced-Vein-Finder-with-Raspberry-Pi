import numpy as np
import cv2

# Load grayscale image
img = cv2.imread('temp.jpg', 0)

# Define kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(7, 7))
cl1 = clahe.apply(img)

# Median blur to reduce noise
cl2 = cv2.medianBlur(cl1, 5)

# Adaptive thresholding
th1 = cv2.adaptiveThreshold(cl2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY_INV, 25, 2.55)

# Otsu’s thresholding after Gaussian filtering
blur = cv2.GaussianBlur(cl1, (5, 5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Combine both thresholding results
th2 = th1 & th3

# Morphological opening to remove small noise
opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)

# Find contours
image, contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw contours on the original image (converted to color)
img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
dst = cv2.drawContours(img1, contours, -1, (0, 255, 0), -1)

# Save output images
cv2.imwrite("out.jpg", dst)
cv2.imwrite("dst.jpg", dst)

