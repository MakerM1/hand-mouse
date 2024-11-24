import cv2

cap = cv2.VideoCapture(0) # 0 is default camera

while True:
    success, frame = cap.read()
    if not success:
        break
    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # press Q to quit
        break

cap.release()
cv2.destroyAllWindows()