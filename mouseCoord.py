import pyautogui
import time

print("Press Ctrl-C to quit.")

try:
    while True:
        # Get the current mouse coordinates
        x, y = pyautogui.position()
        # Print the coordinates
        print(f"X: {x}, Y: {y}")
        # Wait for a short period to avoid spamming the console
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program exited.")
