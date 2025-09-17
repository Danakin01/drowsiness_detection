Drowsiness Detection 🚨
A real-time drowsiness detection system using computer vision to monitor eye closure and alert users when drowsy. Built with Python, OpenCV, dlib, and more.


📖 Table of Contents

About
Features
Prerequisites
Installation
Usage
Project Structure
Dependencies
Notes
License
Contributing
Contact


🧠 About
This project is a real-time drowsiness detection system that uses computer vision to monitor eye closure and alert users when drowsy. Built with Python, OpenCV, dlib, and other libraries, it calculates the Eye Aspect Ratio (EAR) to detect drowsiness, displaying visual and audio alerts to keep users safe, such as drivers or operators in critical environments.

✨ Features

🎥 Real-time face and eye detection using OpenCV's Haar Cascade and dlib's landmark predictor, even in low-light conditions.
✅ Dynamic alerts: Displays "You are alert" (green) or "You are drowsy!" (red) above the user's head.
⚠️ Visual warning: Shows a danger.png icon when drowsy.
🔊 Audio alert: Plays a beep sound when drowsiness is detected (~2 seconds of eye closure).
⚡ Optimized performance: Minimal lag with a clear, medium-sized video feed (640x480 resolution).


📋 Prerequisites
Before running the project, ensure you have:

🐍 Python 3.12 (or 3.8+)
📷 Webcam (built-in or external)
🖥️ Windows OS (for winsound audio alerts)
🖼️ danger.png: A small warning icon (e.g., 100x100 pixels) in the project root
🗂️ models/shape_predictor_68_face_landmarks.dat: dlib face landmark model (~99 MB)


🛠️ Installation
Follow these steps to set up the project locally:

Clone the repository:
git clone https://github.com/Danakin01/drowsiness_detection.git
cd drowsiness_detection


Create and activate a virtual environment (recommended):
python -m venv venv
.\venv\Scripts\activate  # Windows


Install dependencies:
pip install opencv-python imutils scipy


Install dlib for Python 3.12:

Download dlib-19.24.2-cp312-cp312-win_amd64.whl from this link.
Install:pip install dlib-19.24.2-cp312-cp312-win_amd64.whl




Download the dlib model:

Get shape_predictor_68_face_landmarks.dat from here.
Unzip and place in the models/ folder.


Add a warning icon:

Download a warning icon (PNG, e.g., from Flaticon) and save as danger.png in the project root.




🚀 Usage

Ensure your webcam is connected and audio is enabled.
Run the script:python Drowsiness_Detection.py


Face the webcam directly with minimal lighting.
Close your eyes for ~2 seconds to trigger the drowsiness alert (red text, beep, and warning icon).
Press q to quit.




🛠️ Dependencies



Package
Purpose



opencv-python
Computer vision library


imutils
Image processing utilities


scipy
Euclidean distance calculations


dlib
Face landmark detection


winsound
Audio alerts (Windows)



📝 Notes

The script uses OpenCV's Haar Cascade for fast face detection and dlib for eye landmark detection.
Adjust thresh (Eye Aspect Ratio threshold, default: 0.25) or frame_check (frames for drowsiness, default: 10) in Drowsiness_Detection.py if detection is too sensitive or slow.
For non-Windows systems, replace winsound with a compatible audio library (e.g., pygame.mixer).
The large model file (shape_predictor_68_face_landmarks.dat) is tracked with Git LFS to handle its ~99 MB size.


📜 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a Pull Request.


📧 Contact
For questions or feedback, reach out via GitHub Issues or contact Danakin01.

Built with ❤️ by Danakin01
