import pyautogui
import keyboard
import time

# Wait for F1 key to start
print("Press F1 to start the script.")
keyboard.wait("F1")
print("Script started.")

quit = False
while True:
    if quit == True:
        break

    while True:
        if keyboard.is_pressed("F2"):
            quit = True
            break
        try:
            if pyautogui.locateOnScreen("./Images/StartRaceEvent.png", grayscale=True, confidence=0.75) is not None:
                pyautogui.press("left")
                pyautogui.press("up")
                pyautogui.press("enter")
                break
        except pyautogui.ImageNotFoundException:
            continue

    if quit == True:
        break
    pyautogui.keyDown('w')

    while True:
        if keyboard.is_pressed("F2"):
            quit = True
            break
        try:
            if pyautogui.locateOnScreen("./Images/Restart.png", grayscale=True, confidence=0.75) is not None:
                pyautogui.keyUp('w')
                pyautogui.press('x') # restart event
                time.sleep(0.5)
                pyautogui.press("enter") # confirm restart
                break
        except pyautogui.ImageNotFoundException:
            continue