import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0) # 0 is default camera

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()
    if not success:
        break

    # conver frames to rgb
    frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRgb)

    # draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # press Q to quit
        break

cap.release()
cv2.destroyAllWindows()