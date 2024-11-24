import cv2
from hand_tracking.hand_tracker import HandTracker
from utils.cursor_control import move_cursor, click_mouse

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    click_threshold = 0.05

    last_x, last_y = None, None # Store last hand position

    while True:
        success, frame = cap.read()

        if not success:
            break

        # Process the frame from hand tracking
        hand_landmarks = tracker.get_hand_landmarks(frame)

        if hand_landmarks:
            # get index finger tip position
            current_x, current_y = tracker.get_index_finger_tip(hand_landmarks)

            if last_x is not None and last_y is not None:
                # calculate relative mocement (displacement)
                dx = current_x - last_x
                dy = current_y - last_y
                move_cursor(dx, dy) # Move the cursor
            
            # update last hand position
            last_x, last_y = current_x, current_y

            # get landmarks for thumb and index finger
            thumb_tip = hand_landmarks.landmark[4] # thumb index
            index_tip = hand_landmarks.landmark[8] # index finger

            # check if thumb and index are close enough
            distance = tracker.get_distance(thumb_tip, index_tip)
            
            click_mouse(distance < click_threshold)
        else:
            last_x, last_y = None, None
        
        cv2.imshow("Hand Tracking Cursor", frame)

        # exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()