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

def Macro(interrupt_event, car="Peel"):
    # filter so that only the car want to gift is displayed
    pyautogui.press('y') # open filter menu
    time.sleep(0.25)

    if car == "Peel":
        pass
    elif car == "BMW":
        pass
    elif car == "Lexus":
        pass
    elif car == "Jaguar":
        pyautogui.press("enter") # filter by Favorites
        pyautogui.press("down", presses=4, interval=0.05) # filter by Performance Class 'C'
        pyautogui.press("enter")
        pyautogui.press("down", presses=24, interval=0.05) # filter by Car Type "Rare Classics"
        pyautogui.press("enter")

    pyautogui.press("esc") # close filter menu

    count = 0
    while interrupt_event.is_set() == False:
        FindImage("GiftSelect.png", 0.75, interval=0.1) # wait for the gift menu screen open
        pyautogui.press("backspace") # open search window
        # focus on the search window. if not doing this, scrolling will work weirdly
        pyautogui.moveTo(1, 1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        location = None
        if car == "Peel":
            # find "Peel"
            location = FindImage("Peel.png", 0.9, interval=0.1, limit=5, scroll=5) # scroll down to find the "Peel"
        elif car == "Jaguar":
            # find "Jaguar"
            location = FindImage("Jaguar.png", 0.9, interval=0.1, limit=5, scroll=5) # scroll down to find the "Jaguar"
        if location != None:
            pyautogui.moveTo(location)
            pyautogui.press("enter")
        else:
            print(f"{count} of {car} have been gifted.")
            pyautogui.press("esc")
            interrupt_event.set()
            break

        # send gift
        time.sleep(0.4)
        pyautogui.press("enter") # select the Peel car
        time.sleep(0.4)
        pyautogui.press("enter") # gift to
        time.sleep(0.4)
        pyautogui.press("enter") # gift message
        time.sleep(0.4)
        pyautogui.press("down", presses=2, interval=0.05) # select "UNSIGNED"
        pyautogui.press("enter") # gift from
        time.sleep(0.4)
        pyautogui.press("enter") # your gift
        """ time.sleep(0.4)
        pyautogui.press("down") # confirm warning message
        pyautogui.press("enter")
        time.sleep(0.4) """

        FindImage("GiftSent.png", 0.9, interval=0.1) # wait for the gift to be sent
        pyautogui.press("enter") # gift sent

        count += 1
        print(f"Gift sent. Count: {count}")

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