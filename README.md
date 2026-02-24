# Gesture Recognition & Distance Measurement (Milestone 2)

This project implements a real-time gesture recognition and distance measurement system using **MediaPipe Hands**, **OpenCV**, and **Streamlit**.

The system detects multiple hands from a live camera feed and calculates the distance between the thumb tip and index finger tip. Gesture classification is performed based on this distance and displayed through an interactive web interface.

---

## 📌 Features
- Real-time hand detection using MediaPipe
- Thumb–Index fingertip distance calculation
- Gesture classification:
  - **Open** (>100 px)
  - **Pinch** (40–100 px)
  - **Closed** (<40 px)
- Detection of multiple hands
- Distance and gesture calculated using the first detected hand
- Streamlit-based UI with:
  - Live camera feed
  - Status panel
  - Adjustable detection & tracking confidence
  - Max hands selection
  - FPS display

---

## 🛠 Technologies Used
- Python
- OpenCV
- MediaPipe
- Streamlit

---

## 📂 Project Structure
