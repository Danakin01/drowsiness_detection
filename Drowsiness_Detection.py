from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import numpy as np
import winsound

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

thresh = 0.25
frame_check = 10  # ~2 seconds at 5-10 fps
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# Load danger image
danger_img = cv2.imread("danger.png", cv2.IMREAD_UNCHANGED)
if danger_img is None:
    print("DEBUG: Warning: danger.png not found. Continuing without it.")
else:
    print(f"DEBUG: danger.png loaded, shape: {danger_img.shape}")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("DEBUG: Error: Cannot open camera!")
    exit()

flag = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("DEBUG: Error: Failed to grab frame.")
        break
    
    frame = imutils.resize(frame, width=640)  # Lower resolution for speed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Minimal CLAHE for low-light (reduced clipLimit for speed)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
    print(f"DEBUG: Number of faces detected: {len(faces)}")
    
    for (x, y, w, h) in faces:
        subject = dlib.rectangle(x, y, x+w, y+h)
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        print(f"DEBUG: EAR = {ear:.3f}")
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        text_y = max(10, y - 30)  # Text above head
        if ear < thresh:
            flag += 1
            print(f"DEBUG: Flag count: {flag}")
            if flag >= frame_check:
                cv2.putText(frame, "You are drowsy!", (10, text_y), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                winsound.Beep(1000, 500)  # Beep when drowsy
                if danger_img is not None:
                    danger_resized = cv2.resize(danger_img, (100, 100))
                    h, w = danger_resized.shape[:2]
                    if danger_resized.shape[2] == 4:  # RGBA
                        alpha = danger_resized[:, :, 3] / 255.0
                        for c in range(3):
                            frame[10:10+h, frame.shape[1]-w-10:frame.shape[1]-10, c] = \
                                alpha * danger_resized[:, :, c] + (1 - alpha) * frame[10:10+h, frame.shape[1]-w-10:frame.shape[1]-10, c]
                    else:  # BGR
                        frame[10:10+h, frame.shape[1]-w-10:frame.shape[1]-10] = danger_resized[:, :, :3]
        else:
            cv2.putText(frame, "You are alert", (10, text_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            flag = 0
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
