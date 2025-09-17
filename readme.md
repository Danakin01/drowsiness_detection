# Drowsiness Detection

A real-time drowsiness detection system using computer vision to monitor eye closure and alert users when drowsy. Built with Python, OpenCV, dlib, and other libraries, it detects faces, calculates the Eye Aspect Ratio (EAR), and triggers visual and audio alerts for drowsiness.

## Features
- Detects faces and eye landmarks in real-time, even in low-light conditions.
- Displays "You are alert" (green) or "You are drowsy!" (red) above the user's head.
- Shows a warning icon (`danger.png`) when drowsy.
- Plays a beep sound when drowsiness is detected (~2 seconds of eye closure).
- Optimized for minimal lag with a clear, medium-sized video feed.

## Prerequisites
- Python 3.12 (or 3.8+)
- A webcam
- Windows OS (for `winsound` audio alerts)
- `danger.png`: A small warning icon (e.g., 100x100 pixels) in the project root
- `models/shape_predictor_68_face_landmarks.dat`: dlib face landmark model

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Danakin01/Drowsiness-Detection.git
   cd Drowsiness-Detection


Create and activate a virtual environment (recommended):python -m venv venv
.\venv\Scripts\activate  # Windows


Install dependencies:pip install opencv-python imutils scipy


Install dlib for Python 3.12:
Download dlib-19.24.2-cp312-cp312-win_amd64.whl from https://github.com/z-mahmud22/Dlib_Windows_Python3.x/releases.
Install:pip install dlib-19.24.2-cp312-cp312-win_amd64.whl




Download shape_predictor_68_face_landmarks.dat:
Get it from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2.
Unzip and place in the models/ folder.


Add danger.png:
Download a warning icon (PNG, e.g., from https://www.flaticon.com/) and place it in the project root.



Usage

Ensure your webcam is connected and audio is enabled.
Run the script:python Drowsiness_Detection.py


Face the webcam directly with minimal lighting.
Close your eyes for ~2 seconds to trigger the drowsiness alert (text, beep, and warning icon).
Press q to quit.

Project Structure
Drowsiness-Detection/
├── Drowsiness_Detection.py        # Main script
├── models/
│   └── shape_predictor_68_face_landmarks.dat  # dlib model
├── danger.png                     # Warning icon
├── README.md                     # This file
├── .gitignore                    # Git ignore file

Dependencies

opencv-python: Computer vision library
imutils: Image processing utilities
scipy: For Euclidean distance calculations
dlib: For face landmark detection
winsound: For audio alerts (Windows)

Notes

The script uses OpenCV's Haar Cascade for fast face detection and dlib for eye landmark detection.
Adjust thresh (Eye Aspect Ratio threshold) or frame_check (frames for drowsiness) in the script if detection is too sensitive or slow.
For non-Windows systems, replace winsound with a compatible audio library (e.g., pygame.mixer).

License
MIT License```