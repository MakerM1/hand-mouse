# Hand Tracking Cursor Control

This project uses **MediaPipe** and **PyAutoGUI** to track hand movements via a webcam and control the computer's mouse cursor. The cursor follows the index finger and can click when the index finger and thumb touch. This project simulates touchpad-like functionality with hand gestures, offering a hands-free way to control the mouse.

## Features

- **Hand Tracking**: Uses MediaPipe's hand tracking model to detect the position of hand landmarks.
- **Cursor Control**: Tracks the center of the hand and moves the cursor smoothly based on hand movements.
- **Click Detection**: Detects a fist gesture and simulates a mouse click when a fist is made.

## Prerequisites

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

### Install Dependencies

To install the required libraries, use the following command:

```bash
pip install opencv-python mediapipe pyautogui
```

## Usage

Connect your webcam and ensure it is properly configured.
Run the Python script:

```bash
python main.py
```

The webcam window will appear, showing the tracked hand landmarks.
Move your hand in front of the webcam to control the cursor. The cursor will follow the index finger.
Make the index finger and thumb touch to simulate a mouse click and release it to release the click.

## How It Works

    Index Finger Tracking: The program tracks the position of the index finger to control the cursor. The position of the cursor is based on the relative position of the index finger's tip.
    Cursor Movement: The cursor moves based on the relative displacement of the index finger.
    Click Detection: The program detects when the index finger and thumb touch (i.e., a pinch gesture) to simulate a mouse click using pyautogui.mouseDown(). The click is released when the pinch is no longer detected using pyautogui.mouseUp().
