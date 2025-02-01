import pyautogui
import keyboard
import asyncio

async def FindImage(file_name, confidence, interval=0, limit=0, scroll=0):
    for _ in iter(int, 1) if limit == 0 else range(limit):
        if (interval > 0):
            await asyncio.sleep(interval)
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

async def Macro(interrupt_event, car="Peel"):
    # filter so that only the car want to gift is displayed
    pyautogui.press('y') # open filter menu
    await asyncio.sleep(0.25)

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
        await FindImage("GiftSelect.png", 0.75, interval=0.1) # wait for the gift menu screen open
        pyautogui.press("backspace") # open search window
        # focus on the search window. if not doing this, scrolling will work weirdly
        pyautogui.moveTo(1, 1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        location = None
        if car == "Peel":
            # find "Peel"
            location = await FindImage("Peel.png", 0.9, interval=0.1, limit=5, scroll=5) # scroll down to find the "Peel"
        elif car == "Jaguar":
            # find "Jaguar"
            location = await FindImage("Jaguar.png", 0.9, interval=0.1, limit=5, scroll=5) # scroll down to find the "Jaguar"
        if location != None:
            pyautogui.moveTo(location)
            pyautogui.press("enter")
        else:
            print(f"{count} of {car} have been gifted.")
            pyautogui.press("esc")
            interrupt_event.set()
            break

        # send gift
        await asyncio.sleep(0.4)
        pyautogui.press("enter") # select the Peel car
        await asyncio.sleep(0.4)
        pyautogui.press("enter") # gift to
        await asyncio.sleep(0.4)
        pyautogui.press("enter") # gift message
        await asyncio.sleep(0.4)
        pyautogui.press("down", presses=2, interval=0.05) # select "UNSIGNED"
        pyautogui.press("enter") # gift from
        await asyncio.sleep(0.4)
        pyautogui.press("enter") # your gift
        """ await asyncio.sleep(0.4)
        pyautogui.press("down") # confirm warning message
        pyautogui.press("enter")
        await asyncio.sleep(0.4) """

        await FindImage("GiftSent.png", 0.9, interval=0.1) # wait for the gift to be sent
        pyautogui.press("enter") # gift sent

        count += 1
        print(f"Gift sent. Count: {count}")

async def Stopper(interrupt_event):
    await asyncio.get_event_loop().run_in_executor(None, keyboard.wait, "F2") # run the blocking function in a separate thread
    interrupt_event.set()
    print("Script will be stopped after the current loop.")

async def main():
    # wait for F1 key to start
    print("Press F1 to start the script.")
    await asyncio.get_event_loop().run_in_executor(None, keyboard.wait, "F1") # run the blocking function in a separate thread
    print("Script started.")

    interrupt_event = asyncio.Event()
    await asyncio.gather(Macro(interrupt_event), Stopper(interrupt_event))

    print("Exiting the script.")

if __name__ == "__main__":
    asyncio.run(main())