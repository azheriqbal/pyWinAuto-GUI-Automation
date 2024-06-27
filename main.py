from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
import pyautogui



if __name__ == '__main__':
    pyautogui.moveTo(1420, 27, duration=1)  # Moves the mouse to (100, 100) in 1 second

    # Click at the current mouse position
    pyautogui.click()

    pyautogui.moveTo(956, 580, duration=1)

    pyautogui.click()


    try:
        # Start the application
        app = Application(backend="uia").start(r'C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
        app = Application(backend="uia").connect(title='Windows Media Player Legacy', timeout=30)

        vid = app.WindowsMediaPlayerLegacy.child_window(title="Music", control_type="TreeItem").wrapper_object()
        vid.click_input()
        viditem = app.WindowsMediaPlayerLegacy.child_window(title="Ringtone 1",
                                                            control_type="Text").wrapper_object()
        viditem.click_input()
        playbutton = (app
                      .WindowsMediaPlayerLegacy
                      .child_window(title="Play", control_type="Button", found_index=1)
                      .wrapper_object())
        playbutton.click_input()

        pausebutton = (app
                       .WindowsMediaPlayerLegacy
                       .child_window(title="Pause", control_type="Button")
                       .wrapper_object())
        pausebutton.click_input()
        app.WindowsMediaPlayerLegacy.print_control_identifiers()


    except ElementNotFoundError as e:
        print(f"Element not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
