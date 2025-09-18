# 🚨 Drowsiness Detection  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv" />
  <img src="https://img.shields.io/badge/dlib-Facial%20Landmarks-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" />
</p>

<p align="center">
  A real-time <b>drowsiness detection system</b> using computer vision.  
  Monitors eye closure and alerts users with <b>visual + audio warnings</b> to prevent accidents.  
</p>

---

## 🧠 About
This project implements a **real-time drowsiness detection system** using Python, OpenCV, and dlib.  
It calculates the **Eye Aspect Ratio (EAR)** to detect eye closure and triggers **visual and audio alerts** to keep users safe — especially drivers and operators in critical environments.  

---

## ✨ Features
- 🎥 **Real-time face & eye detection** (Haar Cascade + dlib landmarks)  
- ✅ **Dynamic alerts**: Green text (“You are alert”) / Red text (“You are drowsy!”)  
- ⚠️ **Visual warning**: Displays `danger.png` when drowsy  
- 🔊 **Audio alert**: Beep sound after ~2 seconds of closed eyes  
- ⚡ **Optimized performance**: Smooth video feed at 640x480  

---

## 📋 Prerequisites
- 🐍 Python **3.8+ (tested on 3.12)**  
- 📷 Webcam (built-in or external)  
- 🖥️ Windows OS (for `winsound` alerts)  
- 🖼️ `danger.png` (warning icon, ~100x100px)  
- 🗂️ `models/shape_predictor_68_face_landmarks.dat` (~99 MB landmark model)  

---

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/Danakin01/drowsiness_detection.git
cd drowsiness_detection

# (Optional) Create a virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install opencv-python imutils scipy
```
## 📖 Installing dlib (Python 3.12 on Windows)

1. Download wheel:  
   [dlib-19.24.2-cp312-cp312-win_amd64.whl](https://pypi.org/project/dlib/#files)  

2. Install with:  
```bash
pip install dlib-19.24.2-cp312-cp312-win_amd64.whl
```

🚀 Usage

Run the project:

python Drowsiness_Detection.py
