import pyautogui

# Locate the image on the screen
res = pyautogui.locateOnScreen("img_1.png", confidence=0.9)

# Check if the image was found
if res is not None:
    # Print the location and size of the image
    print(f"Image found at coordinates: {res}")

    # Get the center coordinates of the found image
    center_x, center_y = pyautogui.center(res)
    print(f"Center coordinates: ({center_x}, {center_y})")
    pyautogui.moveTo(center_x,center_y)

else:
    print("Image not found on the screen.")


# Center coordinates: (1663, 22) 1187, 1047)

