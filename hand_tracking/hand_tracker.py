import cv2
import mediapipe as mp
import math

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

    def get_hand_landmarks(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
                return hand_landmarks
        return None
    
    def get_index_finger_tip(self, hand_landmakrs):
        index_tip = hand_landmakrs.landmark[8]
        return index_tip.x, index_tip.y
    
    def get_distance(self, p1, p2):
        """"alculate Euclidean distance between two points"""
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)