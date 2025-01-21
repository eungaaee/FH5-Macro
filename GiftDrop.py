import pyautogui
import keyboard
import time

# Wait for F1 key to start
print("Press F1 to start the script.")
keyboard.wait("F1")
print("Script started.")

while True:
    while True:
        try:
            pyautogui.locateOnScreen("./Images/GiftSelect.png", grayscale=True, confidence=0.75)
            break
        except pyautogui.ImageNotFoundException:
            continue

    pyautogui.press("backspace") # open search window
    # focus on the search window. if not doing this, scrolling will work weirdly
    pyautogui.moveTo(1, 1)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    # select "Peel"
    time.sleep(0.1)
    row = 30 # change this value to the maximum number of rows in the search window
    found = False
    for i in range(row):
        try:
            peel_location = pyautogui.locateOnScreen("./Images/Peel.png", grayscale=True, confidence=0.9)
            pyautogui.moveTo(peel_location)
            pyautogui.press("enter")
            found = True
            break
        except pyautogui.ImageNotFoundException:
            pyautogui.press("down")
            continue

    if not found:
        print("All Peel cars are sent.")
        break

    # send gift
    time.sleep(0.5)
    pyautogui.press("enter") # select the Peel car
    time.sleep(0.5)
    pyautogui.press("enter") # gift to
    time.sleep(0.5)
    pyautogui.press("enter") # gift message
    time.sleep(0.5)
    pyautogui.press("down", presses=2, interval=0.05) # select "UNSIGNED"
    pyautogui.press("enter") # gift from
    time.sleep(0.5)
    pyautogui.press("enter") # your gift
    time.sleep(0.5)
    pyautogui.press("down") # confirm warning message
    pyautogui.press("enter") # warning
    time.sleep(0.5)
    while True: # wait for the gift to be sent
        try:
            pyautogui.locateOnScreen("./Images/GiftSent.png", grayscale=True, confidence=0.9)
            print("Gift sent.")
            break
        except pyautogui.ImageNotFoundException:
            continue
    pyautogui.press("enter") # gift sent