# Real-Time Image Processing using Raspberry Pi + NoIR Camera + Custom LED PCB

This project is a complete real-time image capturing and processing system using a Raspberry Pi, a Raspberry Pi NoIR Camera, and a custom-made LED light board for better lighting control. It uses advanced image processing methods such as CLAHE, adaptive thresholding, Otsu’s method, morphological operations, and contour detection to clearly highlight important areas in grayscale images.

At first, this was based on a simpler ESP32-CAM project we did in Semester 2. But after learning more about image processing and computer vision, I decided to improve it using what I had studied. This upgraded system gives better image quality, flexibility, and accuracy. The processed video is shown live on a website that can be viewed on any device connected to the same network as the Raspberry Pi.

In the future, I plan to improve the website to make it more responsive and secure. This system can be used as a real-time screen for nurses to clearly see veins and help guide needle placement more accurately.

---

## 🧰 Tools & Technologies

- **Raspberry Pi 4B**
- **Raspberry Pi NoIR Camera**
- **Custom LED Array PCB**
- **Python 3**
- **OpenCV**
- **NumPy**
- **PiCamera Python Module**
- **Flask**

---

## 🖼️ Hardware Setup

| Raspberry Pi + NoIR Camera | Custom LED PCB |
|----------------------------|----------------|
| ![Raspberry NoIR Camera](https://raw.githubusercontent.com/your-username/your-repo/main/images/raspberry_pi_noir.jpg) | ![Custom PCB](Assets/3D_Vein.jpg) |



---

## 🔬 Image Processing Pipeline

1. **CLAHE (Contrast Limited Adaptive Histogram Equalization)**  
2. **Median & Gaussian Blur for noise suppression**
3. **Adaptive Thresholding (Mean)**
4. **Otsu’s Thresholding**
5. **Morphological Opening**
6. **Contour Detection and Overlay**

---


