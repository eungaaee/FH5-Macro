import pyautogui
import keyboard
import time
import threading

def FindImage(file_name, confidence, interval=0, limit=0, scroll=0):
    for _ in iter(int, 1) if limit == 0 else range(limit):
        if (interval > 0):
            time.sleep(interval)
        try:
            location = pyautogui.locateOnScreen(f"./Images/{file_name}", grayscale=True, confidence=confidence)
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
def Macro(interrupt_event, loop=111): # 999sp / 9sp per car = 111 cars
    is_first = False
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
            time.sleep(0.25)
            pyautogui.press("backspace")
            # focus on the search window. if not doing this, scrolling will work weirdly
            pyautogui.moveTo(1, 1)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            # select "Peel"
            location = FindImage("Peel.png", 0.9, scroll=-5)
            pyautogui.moveTo(location)
            pyautogui.press("enter")
            # there is a bug in the game that the Peel section is not selected properly at the first time if it is too far from the opened section
            # so, select the Peel section again
            time.sleep(0.25)
            pyautogui.press("backspace")
            time.sleep(0.25)
            pyautogui.press("enter")
            time.sleep(0.25)

        time.sleep(0.25)
        pyautogui.press("right")
        pyautogui.press('y')
        time.sleep(0.25)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Garage menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # enter the My Cars menu
        time.sleep(0.25)
        pyautogui.press("left")
        pyautogui.press("enter")

        # wait for the My Cars menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # order the cars by most recent
        time.sleep(0.25)
        pyautogui.press('x')
        time.sleep(0.25)
        pyautogui.press("down", presses=6, interval=0.05)
        pyautogui.press("enter")

        # scroll to the left end
        time.sleep(0.25)
        if is_first:
            pyautogui.keyDown("pageup")
            time.sleep(20) # adjust this value to match the time it takes to get to the left end of the garage
            pyautogui.keyUp("pageup")
        else:
            pyautogui.press("pageup")

        # validate that the Peel Trident is selected
        FindImage("PeelTrident.png", 0.9, interval=0.1)

        # get in car
        pyautogui.press("enter")
        time.sleep(0.25)
        pyautogui.press("enter")

        # wait for the Forza Vista to load
        time.sleep(1)
        FindImage("Esc.png", 0.9, interval=0.1)

        # exit Forza Vista
        time.sleep(0.25)
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Garage menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # enter the Upgrade & Tuning menu
        time.sleep(0.25)
        pyautogui.press("left")
        pyautogui.press("enter")

        # wait for the Upgrade & Tuning menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # enter Car Mastery menu
        """ pyautogui.press("enter") # discard "New Upgrades Available" popup """
        time.sleep(0.25)
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
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

        time.sleep(0.4)
        pyautogui.press("right")
        is_unlocked = UnlockPerk() # unlock third perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(0.4)
        pyautogui.press("up")
        is_unlocked = UnlockPerk() # unlock fourth perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(0.4)
        pyautogui.press("right")
        is_unlocked = UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        # back to Upgrades & Tuning menu
        time.sleep(0.4)
        pyautogui.press("esc")

        # wait for the Upgrade & Tuning menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # back to Garage menu
        time.sleep(0.25)
        pyautogui.press("esc")

        # wait for the Garage menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        if is_first == True:
            is_first = False

    interrupt_event.set()

# buy in Autoshow
def Macro_Autoshow(interrupt_event, loop=111): # 999sp / 9sp per car = 111 cars
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

        # open Autoshow menu
        FindImage("Autoshow.png", 0.75)
        pyautogui.press("left", presses=3, interval=0.05)
        pyautogui.press("right")
        pyautogui.press("enter")

        # wait for the menu to load
        time.sleep(0.5)
        FindImage("Esc.png", 0.75, interval=0.1)

        # move to "Peel" section
        time.sleep(0.5)
        pyautogui.press("backspace") # open search window
        # focus on the search window. if not doing this, scrolling will work weirdly
        pyautogui.moveTo(1, 1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        
        peel_location = FindImage("Peel.png", 0.9, scroll=-5)
        pyautogui.moveTo(peel_location)
        pyautogui.press("enter")

        # validate that the Peel Trident is selected
        time.sleep(0.5)
        FindImage("PeelTrident.png", 0.9, interval=0.1)
        # buy Trident
        pyautogui.press("enter")

        # wait for the select design menu to load
        time.sleep(0.1)
        FindImage("Esc.png", 0.75)

        time.sleep(0.5)
        pyautogui.press('y') # enter the color menu
        time.sleep(0.5)
        pyautogui.press("enter") # select default color
        time.sleep(0.5)
        pyautogui.press("enter") # confirm color
        time.sleep(0.5)
        pyautogui.press("enter") # confirm purchase

        # wait for the Forza Vista to load
        time.sleep(0.5)
        FindImage("Esc.png", 0.75, interval=0.1)
        # exit Forza Vista
        time.sleep(1)
        pyautogui.press("esc") # back to the Autoshow menu

        # wait for the Autoshow menu to load
        time.sleep(0.5)
        FindImage("Esc.png", 0.75, interval=0.1)
        # enter the Upgrade & Tuning menu
        time.sleep(0.5)
        pyautogui.press("pagedown")
        pyautogui.press("left")
        pyautogui.press("enter")
        # wait for the Upgrade & Tuning menu to load
        time.sleep(0.5)
        FindImage("Esc.png", 0.75, interval=0.1)
        """ pyautogui.press("enter") # discard "New Upgrades Available" popup """
        # enter Car Mastery menu
        time.sleep(0.5)
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
        time.sleep(0.5)
        is_unlocked = UnlockPerk() # unlock first perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(0.5)
        pyautogui.press("right")
        is_unlocked = UnlockPerk() # unlock second perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(0.5)
        pyautogui.press("right")
        is_unlocked = UnlockPerk() # unlock third perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(0.5)
        pyautogui.press("up")
        is_unlocked = UnlockPerk() # unlock fourth perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(0.5)
        pyautogui.press("right")
        is_unlocked = UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(0.5)
        pyautogui.press("esc") # back to Upgrades & Tuning menu

        time.sleep(0.5)
        FindImage("Esc.png", 0.75, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("esc") # back to Garage menu

        time.sleep(0.5)
        FindImage("Esc.png", 0.75, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("pageup") # back to Buy & Sell menu

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