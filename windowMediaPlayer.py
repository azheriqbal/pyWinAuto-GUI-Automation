from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError

try:
    # Start the application
    app = Application(backend="uia").start(r'C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
    app = Application(backend="uia").connect(title='Windows Media Player Legacy', timeout=30)


    vid = app.WindowsMediaPlayerLegacy.child_window(title="Videos", control_type="TreeItem").wrapper_object()
    vid.click_input()

    btn = (app.WindowsMediaPlayerLegacy
           .child_window(title="Play", control_type="Button", found_index=1)
           .wrapper_object())

    btn.click_input()
    app.WindowsMediaPlayerLegacy.print_control_identifiers()

except ElementNotFoundError as e:
    print(f"Element not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
