import pyautogui
import keyboard
import time
import threading

def Macro(interrupt_event, loop=111): # 999sp / 9sp per car = 111 cars
    is_first = True
    current_loop = 0
    while interrupt_event.is_set() == False:
        if (loop == 0): # set loop 0 to run infinitely
            pass
        else:
            print(f"{current_loop} / {loop}")
            if (current_loop < loop):
                current_loop += 1
            else:
                print("Completed.")
                break

        # open Car Collection
        while True:
            try:
                pyautogui.locateOnScreen("./Images/CarCollection.png", grayscale=True, confidence=0.75)
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

        # move to "Peel" section
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
        time.sleep(1.5)
        pyautogui.press("right")
        pyautogui.press('y')
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("esc") # back to Car Garage menu

        # enter the garage
        time.sleep(1)
        pyautogui.press("left")
        pyautogui.press("enter")

        # order the cars by most recent
        time.sleep(1)
        pyautogui.press('x')
        time.sleep(0.5)
        pyautogui.press("down", presses=6, interval=0.05)
        pyautogui.press("enter")

        # scroll to the left end
        pyautogui.keyDown("pageup")
        time.sleep(10 if is_first else 0.5) # adjust this value to match the time it takes to get to the left end of the garage
        pyautogui.keyUp("pageup")

        # validate that the Peel Trident is selected
        while True:
            try:
                pyautogui.locateOnScreen("./Images/PeelTrident.png", grayscale=True, confidence=0.9)
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
                pyautogui.locateOnScreen("./Images/Esc.png", grayscale=True, confidence=0.75)
                time.sleep(1)
                pyautogui.press("esc") # exit Forza Vista
                break
            except pyautogui.ImageNotFoundException:
                continue

        # enter Upgrades & Tuning menu
        time.sleep(1)
        pyautogui.press("left", presses=2, interval=0.05)
        pyautogui.press("enter") 

        # enter Car Mastery menu
        time.sleep(1)
        """ pyautogui.press("enter") # discard "New Upgrades Available" popup """
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
        time.sleep(0.5)
        pyautogui.press("enter") # unlock first perk
        try:
            time.sleep(0.5)
            pyautogui.locateOnScreen("./Images/NoSkillPoint.png", grayscale=True, confidence=0.9)
            print("No skill point left.")
            break
        except pyautogui.ImageNotFoundException:
            pass

        time.sleep(0.5)
        pyautogui.press("right")
        pyautogui.press("enter") # unlock second perk
        try:
            time.sleep(0.5)
            pyautogui.locateOnScreen("./Images/NoSkillPoint.png", grayscale=True, confidence=0.9)
            print("No skill point left.")
            break
        except pyautogui.ImageNotFoundException:
            pass

        time.sleep(0.5)
        pyautogui.press("right")
        pyautogui.press("enter") # unlock third perk
        try:
            time.sleep(0.5)
            pyautogui.locateOnScreen("./Images/NoSkillPoint.png", grayscale=True, confidence=0.9)
            print("No skill point left.")
            break
        except pyautogui.ImageNotFoundException:
            pass

        time.sleep(0.5)
        pyautogui.press("up")
        pyautogui.press("enter") # unlock fourth perk
        try:
            time.sleep(0.5)
            pyautogui.locateOnScreen("./Images/NoSkillPoint.png", grayscale=True, confidence=0.9)
            print("No skill point left.")
            break
        except pyautogui.ImageNotFoundException:
            pass

        time.sleep(0.5)
        pyautogui.press("right")
        pyautogui.press("enter") # unlock last perk
        try:
            time.sleep(0.5)
            pyautogui.locateOnScreen("./Images/NoSkillPoint.png", grayscale=True, confidence=0.9)
            print("No skill point left.")
            break
        except pyautogui.ImageNotFoundException:
            pass

        # exit Car Mastery menu
        time.sleep(0.5)
        pyautogui.press("esc") # back to Upgrades & Tuning menu
        time.sleep(1)
        pyautogui.press("esc") # back to Garage menu

        if is_first:
            is_first = False

    interrupt_event.set()

def Stopper(interrupt_event):
    while interrupt_event.is_set() == False:
        if keyboard.is_pressed("F2"):
            interrupt_event.set()
            print("Script will be stopped after the current loop.")
            break
        time.sleep(0.1)

def main():
    # wait for F1 key to start
    print("Press F1 to start the script.")
    keyboard.wait("F1")
    print("Script started.")

    interrupt_event = threading.Event()

    macro_thread = threading.Thread(target=Macro, args=(interrupt_event, ))
    stopper_thread = threading.Thread(target=Stopper, args=(interrupt_event, ))

    macro_thread.start()
    stopper_thread.start()

    macro_thread.join()
    stopper_thread.join()

    print("Exiting the script.")

if __name__ == "__main__":
    main()