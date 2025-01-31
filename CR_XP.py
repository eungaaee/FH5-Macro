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

def Macro(interrupt_event, loop=0):
    current_loop = 0
    while interrupt_event.is_set() == False:
        if (loop == 0): # set loop 0 to run infinitely
            current_loop += 1
            print(f"{current_loop} / INF")
        else:
            if (current_loop < loop):
                current_loop += 1
                print(f"{current_loop} / {loop}")
            else:
                print("Completed.")
                interrupt_event.set()
                break

        # go to menu
        FindImage("V.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("esc")

        # go to the Creetive Hub tab
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)
        time.sleep(0.5)
        pyautogui.press("pagedown", presses=6, interval=0.05)

        # enter the EventLab
        pyautogui.press("enter")

        # enter the Event Blueprint menu
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # go to My History tab
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("pagedown", presses=7, interval=0.05)

        # enter the event
        time.sleep(0.25)
        FindImage("Space.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # select Solo race
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # select the current car
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # start
        time.sleep(0.25)
        FindImage("StartRaceEvent.png", 0.9, interval=0.1)
        pyautogui.press("enter")

        # skip the checkpoint
        time.sleep(7)
        pyautogui.keyDown('w')
        time.sleep(2.5)
        pyautogui.keyDown('a')
        time.sleep(0.4)
        pyautogui.keyUp('a')
        time.sleep(2)
        pyautogui.press('e')
        time.sleep(2)
        pyautogui.keyDown('d')
        time.sleep(0.55)
        pyautogui.keyUp('d')
        time.sleep(4)
        pyautogui.keyUp('w')
        time.sleep(5) # wait for the respawn

        # go to the tunnel from the checkpoint
        pyautogui.keyDown('w')
        time.sleep(2.5)
        pyautogui.keyDown('d')
        time.sleep(0.5)
        pyautogui.keyUp('d')
        time.sleep(2)
        pyautogui.keyDown('d')
        time.sleep(1.75)
        pyautogui.keyUp('d')
        pyautogui.keyUp('w')
        pyautogui.keyDown('a')
        time.sleep(0.3)
        pyautogui.keyUp('a')
        pyautogui.keyDown('d')
        time.sleep(0.4)
        pyautogui.keyUp('d')

        """ # put the front wheels in the tunnel (* not stable)
        time.sleep(0.25)
        pyautogui.keyDown('w')
        time.sleep(1.5)
        pyautogui.keyUp('w')
        pyautogui.keyDown("space") """
        # put the front wheels in the tunnel manually and press T(telemetry)
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        keyboard.wait('t')
        pyautogui.keyDown("space")

        # wait for the event to finish
        time.sleep(20)
        pyautogui.press('t') # close telemetry
        FindImage("X.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.keyUp("space")
        pyautogui.press("enter")

        # skip "rate the event"
        time.sleep(0.25)
        if FindImage("Enter.png", 0.9, interval=0.1, limit=10) != None:
            time.sleep(0.1)
            pyautogui.press("down", presses=2, interval=0.05)
            pyautogui.press("enter")

        # skip xp reward screen
        time.sleep(0.25)
        FindImage("Enter.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # skip cr reward screen
        time.sleep(0.25)
        FindImage("Enter.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # skip wheelspin reward screen
        time.sleep(0.25)
        FindImage("Enter.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # skip wheelspin reward redeem
        time.sleep(0.25)
        FindImage("Enter.png", 0.9, interval=0.1)
        time.sleep(0.1)
        pyautogui.press("enter")

        # check if car already owned
        time.sleep(0.25)
        while FindImage("CarAlreadyOwned.png", 0.9, interval=0.1, limit=10) != None:
            continue

        # skip another "rate the event"
        time.sleep(0.25)
        if FindImage("Enter.png", 0.9, interval=0.1, limit=10) != None:
            time.sleep(0.1)
            pyautogui.press("down", presses=2, interval=0.05)
            pyautogui.press("enter")

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