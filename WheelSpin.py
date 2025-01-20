import pyautogui
import keyboard
import time

# Wait for F1 key to start
print("Press F1 to start the script.")
keyboard.wait("F1")
print("Script started.")

is_first = True
while True:
    # open Car Collection
    while True:
        try:
            car_collection_location = pyautogui.locateOnScreen("./Images/CarCollection.png", grayscale=True, confidence=0.75)
            if car_collection_location is not None:
                """ # .click() is not working, so use .moveTo() and .press() instead. or just use .moveTo() and .mouseDown() and .mouseUp()
                # -> both methods are not stable. don't know why. just gonna use the keyboard.
                time.sleep(0.5)
                pyautogui.moveTo(car_collection_location)
                time.sleep(0.5)
                pyautogui.press("enter") """
                time.sleep(0.5)
                pyautogui.press("right", presses=2, interval=0.05)
                pyautogui.press("enter")
                break
        except pyautogui.ImageNotFoundException:
            continue

    # buy the Peel Trident
    if is_first:
        time.sleep(1)
        pyautogui.press("backspace") # open search window
        # focus on the search window. if not doing this, scrolling will work weirdly
        pyautogui.moveTo(1, 1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        # select top left corner
        pyautogui.keyDown('w')
        time.sleep(3)
        pyautogui.keyUp('w')
        pyautogui.keyDown('a')
        time.sleep(1.5)
        pyautogui.keyUp('a')
        # select "Peel"
        pyautogui.press("up", presses=9, interval=0.05)
        pyautogui.press("right", presses=3, interval=0.05)
        pyautogui.press("enter")
    # select "Trident" and buy it
    time.sleep(1)
    pyautogui.press("right")
    pyautogui.press('y')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("esc") # back to Car Garage menu

    # select the Peel Trident in the garage
    time.sleep(1)
    pyautogui.press("left")
    pyautogui.press("enter") # enter the garage
    # order the cars by most recent
    time.sleep(1)
    pyautogui.press('x')
    time.sleep(0.5)
    pyautogui.press("down", presses=6, interval=0.05)
    pyautogui.press("enter")
    # scroll to the left end
    pyautogui.keyDown("pageup")
    time.sleep(10 if is_first else 1) # adjust this value to match the time it takes to get to the left end of the garage
    pyautogui.keyUp("pageup")

    # validate that the Peel Trident is selected
    while True:
        try:
            if pyautogui.locateOnScreen("./Images/PeelTrident.png", grayscale=True, confidence=0.9) is not None:
                break
        except pyautogui.ImageNotFoundException:
            continue

    # get in car
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    # wait for the Forza Vista to load
    while True:
        try:
            if pyautogui.locateOnScreen("./Images/Esc.png", grayscale=True, confidence=0.75) is not None:
                time.sleep(1)
                pyautogui.press("esc") # exit Forza Vista
                break
        except pyautogui.ImageNotFoundException:
            continue

    # unlock mastery perks
    time.sleep(1)
    pyautogui.press("left", presses=2, interval=0.05)
    pyautogui.press("enter") # enter Upgrades & Tuning menu
    time.sleep(1)
    """ pyautogui.press("enter") # discard "New Upgrades Available" popup """
    pyautogui.press("right", presses=2, interval=0.05)
    pyautogui.press("down")
    pyautogui.press("enter") # enter Car Mastery menu
    time.sleep(0.5)
    pyautogui.press("enter") # unlock first perk
    time.sleep(1)
    pyautogui.press("right")
    pyautogui.press("enter") # unlock second perk
    time.sleep(1)
    pyautogui.press("right")
    pyautogui.press("enter") # unlock third perk
    time.sleep(1)
    pyautogui.press("up")
    pyautogui.press("enter") # unlock fourth perk
    time.sleep(1)
    pyautogui.press("right")
    pyautogui.press("enter") # unlock last perk
    time.sleep(1)
    pyautogui.press("esc") # back to Upgrades & Tuning menu
    time.sleep(1)
    pyautogui.press("esc") # back to Garage menu
    
    if is_first:
        is_first = False