import pyautogui
import keyboard
import time
import threading

def FindImage(file_name, confidence, interval=0, limit=0, scroll=0):
    for _ in iter(int, 1) if limit == 0 else range(limit):
        if (interval > 0):
            time.sleep(interval)
        try:
            location = pyautogui.locateOnScreen(f"./Images/{file_name}", grayscale=True, confidence=confidence) # using the confidence parameter will force to use _locateAll_opencv() instead of _locateAll_pillow()
            return location
        except pyautogui.ImageNotFoundException:
            if scroll > 0:
                pyautogui.press("down", presses=scroll, interval=0.05)
            elif scroll < 0:
                pyautogui.press("up", presses=-scroll, interval=0.05)
            continue
    
    return None

def UnlockPerk():
    pyautogui.press("enter") # unlock perk
    found = FindImage("NoSkillPoint.png", 0.9, interval=0.5, limit=1)
    return True if found == None else False

# buy in Car Collection
def Macro(interrupt_event, loop=999, car="Jaguar"): # BMW and Lexus: 999sp / 5sp per car = 199.8 cars, Jaguar: 999sp / 1sp per car = 999 cars
    is_first = True
    current_loop = 0
    while interrupt_event.is_set() == False:
        if (loop == 0): # set loop 0 to run infinitely
            pass
        else:
            if (current_loop < loop):
                current_loop += 1
                print(f"{current_loop} / {loop}")
            else:
                print("Completed.")
                break

        # open Car Collection
        time.sleep(0.1)
        if is_first:
            location = FindImage("CarCollection.png", 0.9, interval=0.1)
            pyautogui.moveTo(location)
        else:
            pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("enter")

        # wait for the Car Collection menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        if is_first:
            # open search window
            time.sleep(0.1)
            pyautogui.press("backspace")
            # focus on the search window. if not doing this, scrolling will work weirdly
            pyautogui.moveTo(1, 1)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            # select "car" Section
            location = FindImage(f"{car}.png" , 0.9, interval=0.1, scroll=5)
            pyautogui.moveTo(location)
            pyautogui.press("enter")
            pyautogui.moveTo(1, 1) # move the cursor to the top left corner to prevent interference
            # there is a bug in the game that the section is not selected properly at the first time if it is too far from the opened section
            # so, select the section again
            time.sleep(0.25)
            pyautogui.press("backspace")
            time.sleep(0.25)
            pyautogui.press("enter")
            time.sleep(0.25)

        time.sleep(0.1)
        if car == "BMW":
            pyautogui.press("right", presses=6, interval=0.05)
        elif car == "Lexus":
            pass
        elif car == "Jaguar":
            pyautogui.press("right", presses=3, interval=0.05)
        pyautogui.press('y')
        time.sleep(0.25)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Garage menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # enter the My Cars menu
        time.sleep(0.1)
        pyautogui.press("left")
        pyautogui.press("enter")

        # wait for the My Cars menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # order the cars by most recent
        time.sleep(0.1)
        pyautogui.press('x')
        time.sleep(0.25)
        pyautogui.press("down", presses=6, interval=0.05)
        pyautogui.press("enter")

        # scroll to the left end
        time.sleep(0.25)
        if is_first:
            pyautogui.keyDown("pageup")
            time.sleep(25) # adjust this value to match the time it takes to get to the left end of the garage
            pyautogui.keyUp("pageup")
        else:
            pyautogui.press("pageup")

        if (car == "BMW"):
            # validate that the BMW M5 1995 is selected
            FindImage("M5_1995.png", 0.9, interval=0.1)
        elif (car == "Lexus"):
            # validate that the Lexus SC300 is selected
            FindImage("SC300.png", 0.9, interval=0.1)
        elif (car == "Jaguar"):
            # validate that the Jaguar E-Type is selected
            FindImage("E-Type.png", 0.9, interval=0.1)

        # mark the car as favorite
        pyautogui.press("enter")
        time.sleep(0.25)
        pyautogui.press("down")
        pyautogui.press("enter")

        # get in the car
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(0.25)
        pyautogui.press("enter")

        # wait for the Forza Vista to load
        time.sleep(5)
        FindImage("Esc.png", 0.9, interval=0.1)

        # exit Forza Vista
        time.sleep(0.5) # forza vista is very slow and laggy compared to the other menus, so it needs more delay
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Garage menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # enter the Upgrade & Tuning menu
        time.sleep(0.1)
        pyautogui.press("left")
        pyautogui.press("enter")

        # wait for the Upgrade & Tuning menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # enter Car Mastery menu
        """ pyautogui.press("enter") # discard "New Upgrades Available" popup """
        time.sleep(0.1)
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
        if car == "BMW" or car == "Lexus":
            time.sleep(0.5)
            is_unlocked = UnlockPerk() # unlock first perk
            if is_unlocked == False:
                print("No skill point left.")
                break

            time.sleep(0.4)
            pyautogui.press("right")
            is_unlocked = UnlockPerk() # unlock second perk
            if is_unlocked == False:
                print("No skill point left.")
                break

            time.sleep(0.25)
            pyautogui.press("up")
            is_unlocked = UnlockPerk() # unlock third perk
            if is_unlocked == False:
                print("No skill point left.")
                break
        elif car == "Jaguar":
            time.sleep(0.5)
            is_unlocked = UnlockPerk() # unlock first perk
            if is_unlocked == False:
                print("No skill point left.")
                break
            time.sleep(0.15) # + 0.25 = 0.4

        # back to Upgrades & Tuning menu
        time.sleep(0.25)
        pyautogui.press("esc")

        # wait for the Upgrade & Tuning menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # back to Garage menu
        time.sleep(0.1)
        pyautogui.press("esc")

        # wait for the Garage menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        if is_first == True:
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