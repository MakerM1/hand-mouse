import pyautogui

def move_cursor(dx, dy, sensitivity=1):
    """
    Move the cursor based on relative displacement (dx, dy) with sensitivity.
    """
    pyautogui.FAILSAFE = False
    # Get the current cursor position
    current_x, current_y = pyautogui.position()
    
    # Constrain the cursor within screen bounds
    screen_width, screen_height = pyautogui.size()

    # Calculate the new position
    new_x = current_x + int(dx * screen_width)
    new_y = current_y + int(dy * screen_height)

    new_x = max(0, min(new_x, screen_width))
    new_y = max(0, min(new_y, screen_height))
    
    # Move the cursor
    pyautogui.moveTo(new_x, new_y)

def click_mouse(is_thumb_up):
    """Simulate a mouse click"""
    if is_thumb_up:
        pyautogui.mouseDown()
    else:
        pyautogui.mouseUp()