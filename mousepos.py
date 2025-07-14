import pyautogui
import keyboard
import time

print("Press 'z' to get mouse position and pixel color. Press 'esc' to quit.")

while True:
    if keyboard.is_pressed('z'):
        x, y = pyautogui.position()
        try:
            color = pyautogui.pixel(x, y)
            print(f"Position: ({x}, {y}) | Color: {color}")
        except Exception as e:
            print(f"Error reading pixel color at ({x}, {y}): {e}")
        time.sleep(0.2)  # prevent spam on key hold

    if keyboard.is_pressed('esc'):
        print("Exiting.")
        break
