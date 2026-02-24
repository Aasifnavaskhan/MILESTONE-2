# handgesture.py

import cv2
import mediapipe as mp
import math

class GestureDistanceController:
    def __init__(self, det_conf=0.7, trk_conf=0.7, max_hands=2):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            min_detection_confidence=det_conf,
            min_tracking_confidence=trk_conf,
            max_num_hands=max_hands
        )

    def process_frame(self, frame):
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        distance = None
        gesture = "None"
        hand_detected = 0

        if results.multi_hand_landmarks:
            hand_detected = len(results.multi_hand_landmarks)

            # Draw ALL hands
            for handLms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame, handLms, self.mp_hands.HAND_CONNECTIONS
                )

            # Use FIRST hand for calculation
            first_hand = results.multi_hand_landmarks[0]

            thumb = first_hand.landmark[4]
            index = first_hand.landmark[8]

            x1, y1 = int(thumb.x * w), int(thumb.y * h)
            x2, y2 = int(index.x * w), int(index.y * h)

            distance = int(math.hypot(x2 - x1, y2 - y1))

            if distance < 40:
                gesture = "Closed"
            elif distance < 100:
                gesture = "Pinch"
            else:
                gesture = "Open"

            cv2.circle(frame, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 10, (0, 255, 0), cv2.FILLED)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            cv2.putText(frame, f"Distance: {distance} px",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0, 255, 255), 2)

            cv2.putText(frame, f"Gesture: {gesture}",
                        (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0, 255, 255), 2)

        return frame, distance, gesture, hand_detected