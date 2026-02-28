## 🟡 Milestone 2: Gesture Recognition and Distance Measurement

### 🎯 Objective
The objective of Milestone 2 is to accurately recognize hand gestures by calculating the distance between the thumb tip and index finger tip and classifying gestures based on this distance.

---

### 🛠 Functionalities Implemented
- Real-time hand landmark detection
- Calculation of Euclidean distance between thumb and index finger
- Gesture classification based on distance thresholds
- Gesture annotation on live video feed
- Display of calculated distance values as overlays
- Real-time performance monitoring (FPS)

---

### ⚙ Gesture Classification Logic
The gesture is classified based on the measured distance between the thumb and index finger tips:

| Distance Between Fingers (pixels) | Gesture |
|---------------------------------|---------|
| Less than 40                     | Closed  |
| Between 40 and 100               | Pinch   |
| Greater than 100                 | Open    |

The Euclidean distance is calculated for every video frame to ensure real-time responsiveness.

---

### Output
- Live camera feed with gesture annotations
- Hand landmarks and connections displayed
- Line connecting thumb tip and index finger tip
- Calculated distance shown as overlay
- Gesture label displayed on screen

---

## 🛠 Technologies Used
- **Python**
- **OpenCV** – Video capture and drawing utilities
- **MediaPipe Hands** – Hand landmark detection
- **Streamlit** – Interactive web interface
- **NumPy** – Numerical computations
- **PyCAW (Windows)** – System audio control (Milestone 1)



---


## 📁 Project Structure

```
Gesture-Volume-Control-with-Hand-Gestures/
│
├── app.py              # Main Streamlit application
├── handgesture.py      # Hand gesture detection & volume logic
├── run_app.py          # Application launcher
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
├── LICENSE             # License file
└── .gitignore          # Ignored files
---
## ▶️ How to Run the Project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python run_app.py
```

OR

```bash
streamlit run app.py
```

Step 3: Usage Instructions
Click Start Camera to activate the webcam

Place your hand in front of the camera

Move thumb and index finger to:

Adjust volume (Milestone 1)

Observe distance and gesture classification (Milestone 2)

Close your hand to mute the system

Click Stop Camera to end the session

🧪 Observations and Results
The system performs accurately under adequate lighting conditions

Gesture recognition is stable with minimal latency

Distance-based control provides intuitive interaction

Streamlit interface offers clear real-time feedback


✅ Conclusion
The combined implementation of Milestone 1 and Milestone 2 successfully demonstrates a real-time gesture-based interaction system. Milestone 1 establishes reliable volume control using hand gestures, while Milestone 2 enhances the system with accurate gesture recognition and distance measurement. Together, these milestones form a robust foundation for advanced gesture-controlled applications.

---

## 👤 Author
Aasif N

---

## 📜 License
This project is licensed under the MIT License.


