# Gesture Recognition & Distance Measurement (Milestone 2)

This project implements a real-time **gesture recognition and distance measurement system** using **MediaPipe Hands**, **OpenCV**, and **Streamlit**.

The application detects hands from a live camera feed, measures the distance between the **thumb tip and index finger tip**, and classifies gestures based on this distance. An interactive Streamlit interface is used to display live video, gesture status, distance values, and system performance.

---

## 🚀 Features
- Real-time hand detection using MediaPipe
- Thumb–Index fingertip distance calculation
- Gesture classification:
  - **Open** (> 100 px)
  - **Pinch** (40–100 px)
  - **Closed** (< 40 px)
- Detection of multiple hands
- Distance and gesture calculated using the **first detected hand**
- Streamlit-based UI with:
  - Live camera feed
  - Status panel
  - Adjustable detection confidence
  - Adjustable tracking confidence
  - Max hands selection
  - FPS display

---

## 🛠 Technologies Used
- **Python**
- **OpenCV**
- **MediaPipe**
- **Streamlit**

---

## 📂 Project Structure
MILESTONE-2/
│
├── app.py # Streamlit application
├── handgesture.py # Gesture and distance logic
├── run_app.py # App launcher
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── LICENSE # License file


---

## ▶ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
2️⃣ Run the Application
streamlit run app.py

or

python run_app.py
📸 Output

Live camera feed with hand landmarks

Distance measurement overlay (in pixels)

Gesture classification display

Status indicators:

Camera status

Hands detected

Distance value

Gesture type

FPS

🎓 Academic Note

This project is developed as Milestone 2 (Weeks 3–4) for the Gesture Recognition and Distance Measurement Module.

📌 Author

Asifnava Khan

📄 License

This project is licensed under the MIT License.
