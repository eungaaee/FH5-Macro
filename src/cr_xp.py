import pyautogui
import keyboard
import asyncio


async def FindImage(file_name, confidence, interval=0, limit=0, scroll=0):
    for _ in iter(int, 1) if limit == 0 else range(limit):
        if (interval > 0):
            await asyncio.sleep(interval)
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


async def Macro(interrupt_event, loop=0):
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
        await FindImage("V.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("esc")

        # go to the Creetive Hub tab
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)
        await asyncio.sleep(0.5)
        pyautogui.press("pagedown", presses=6, interval=0.05)

        # enter the EventLab
        pyautogui.press("enter")

        # enter the Event Blueprint menu
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # go to My History tab
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("pagedown", presses=7, interval=0.05)

        # enter the event
        await asyncio.sleep(0.25)
        await FindImage("Space.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # select Solo race
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # select the current car
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # start
        await asyncio.sleep(0.25)
        await FindImage("StartRaceEvent.png", 0.9, interval=0.1)
        pyautogui.press("enter")

        # skip the checkpoint
        await asyncio.sleep(7)
        pyautogui.keyDown('w')
        await asyncio.sleep(2.5)
        pyautogui.keyDown('a')
        await asyncio.sleep(0.4)
        pyautogui.keyUp('a')
        await asyncio.sleep(2)
        pyautogui.press('e')
        await asyncio.sleep(2)
        pyautogui.keyDown('d')
        await asyncio.sleep(0.55)
        pyautogui.keyUp('d')
        await asyncio.sleep(4)
        pyautogui.keyUp('w')
        await asyncio.sleep(5) # wait for the respawn

        # go to the tunnel from the checkpoint
        pyautogui.keyDown('w')
        await asyncio.sleep(2.5)
        pyautogui.keyDown('d')
        await asyncio.sleep(0.5)
        pyautogui.keyUp('d')
        await asyncio.sleep(2)
        pyautogui.keyDown('d')
        await asyncio.sleep(1.75)
        pyautogui.keyUp('d')
        pyautogui.keyUp('w')
        pyautogui.keyDown('a')
        await asyncio.sleep(0.3)
        pyautogui.keyUp('a')
        pyautogui.keyDown('d')
        await asyncio.sleep(0.4)
        pyautogui.keyUp('d')

        """ # put the front wheels in the tunnel (* not stable)
        await asyncio.sleep(0.25)
        pyautogui.keyDown('w')
        await asyncio.sleep(1.5)
        pyautogui.keyUp('w')
        pyautogui.keyDown("space") """
        # put the front wheels in the tunnel manually and press T(telemetry)
        pyautogui.keyDown('s')
        await asyncio.sleep(1)
        pyautogui.keyUp('s')
        keyboard.wait('t')
        pyautogui.keyDown("space")

        # wait for the event to finish
        await asyncio.sleep(20)
        pyautogui.press('t') # close telemetry
        await FindImage("X.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.keyUp("space")
        pyautogui.press("enter")

        # skip "rate the event"
        await asyncio.sleep(0.25)
        if await FindImage("Enter.png", 0.9, interval=0.1, limit=10) != None:
            await asyncio.sleep(0.1)
            pyautogui.press("down", presses=2, interval=0.05)
            pyautogui.press("enter")

        # skip xp reward screen
        await asyncio.sleep(0.25)
        await FindImage("Enter.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # skip cr reward screen
        await asyncio.sleep(0.25)
        await FindImage("Enter.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # skip wheelspin reward screen
        await asyncio.sleep(0.25)
        await FindImage("Enter.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # skip wheelspin reward redeem
        await asyncio.sleep(0.25)
        await FindImage("Enter.png", 0.9, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("enter")

        # check if car already owned
        await asyncio.sleep(0.25)
        while await FindImage("CarAlreadyOwned.png", 0.9, interval=0.1, limit=10) != None:
            continue

        # skip another "rate the event"
        await asyncio.sleep(0.25)
        if await FindImage("Enter.png", 0.9, interval=0.1, limit=10) != None:
            await asyncio.sleep(0.1)
            pyautogui.press("down", presses=2, interval=0.05)
            pyautogui.press("enter")


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