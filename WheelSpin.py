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

async def UnlockPerk():
    pyautogui.press("enter") # unlock perk
    found = await FindImage("NoSkillPoint.png", 0.9, interval=0.5, limit=1)
    return True if found == None else False

# buy in Car Collection
async def Macro(interrupt_event, loop=111): # 999sp / 9sp per car = 111 cars
    is_first = True
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
                break

        # open Car Collection
        await asyncio.sleep(0.1)
        if is_first:
            location = await FindImage("CarCollection.png", 0.9, interval=0.1)
            pyautogui.moveTo(location)
        else:
            pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("enter")

        # wait for the Car Collection menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        if is_first:
            # open search window
            await asyncio.sleep(0.1)
            pyautogui.press("backspace")
            # focus on the search window. if not doing this, scrolling will work weirdly
            pyautogui.moveTo(1, 1)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            # select "Peel"
            location = await FindImage("Peel.png", 0.9, interval=0.1, scroll=-5)
            pyautogui.moveTo(location)
            pyautogui.press("enter")
            pyautogui.moveTo(1, 1) # move the cursor to the top left corner to prevent interference
            # there is a bug in the game that the Peel section is not selected properly at the first time if it is too far from the opened section
            # so, select the Peel section again
            await asyncio.sleep(0.25)
            pyautogui.press("backspace")
            await asyncio.sleep(0.25)
            pyautogui.press("enter")
            await asyncio.sleep(0.25)

        await asyncio.sleep(0.1)
        pyautogui.press("right")
        pyautogui.press('y')
        await asyncio.sleep(0.25)
        pyautogui.press("enter")
        await asyncio.sleep(0.5)
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Garage menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # enter the My Cars menu
        await asyncio.sleep(0.1)
        pyautogui.press("left")
        pyautogui.press("enter")

        # wait for the My Cars menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # order the cars by most recent
        await asyncio.sleep(0.1)
        pyautogui.press('x')
        await asyncio.sleep(0.25)
        pyautogui.press("down", presses=6, interval=0.05)
        pyautogui.press("enter")

        # scroll to the left end
        await asyncio.sleep(0.25)
        if is_first:
            pyautogui.keyDown("pageup")
            await asyncio.sleep(25) # adjust this value to match the time it takes to get to the left end of the garage
            pyautogui.keyUp("pageup")
        else:
            pyautogui.press("pageup")

        # validate that the Peel Trident is selected
        await FindImage("Trident.png", 0.9, interval=0.1)

        # get in the car
        pyautogui.press("enter")
        await asyncio.sleep(0.25)
        pyautogui.press("enter")

        # wait for the Forza Vista to load
        await asyncio.sleep(5)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # exit Forza Vista
        await asyncio.sleep(0.5) # forza vista is very slow and laggy compared to the other menus, so it needs more delay
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Garage menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # enter the Upgrade & Tuning menu
        await asyncio.sleep(0.1)
        pyautogui.press("left")
        pyautogui.press("enter")

        # wait for the Upgrade & Tuning menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # enter Car Mastery menu
        """ pyautogui.press("enter") # discard "New Upgrades Available" popup """
        await asyncio.sleep(0.1)
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
        await asyncio.sleep(0.5)
        is_unlocked = await UnlockPerk() # unlock first perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.4)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock second perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.25)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock third perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.25)
        pyautogui.press("up")
        is_unlocked = await UnlockPerk() # unlock fourth perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.25)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        # back to Upgrades & Tuning menu
        await asyncio.sleep(0.25)
        pyautogui.press("esc")

        # wait for the Upgrade & Tuning menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # back to Garage menu
        await asyncio.sleep(0.1)
        pyautogui.press("esc")

        # wait for the Garage menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        if is_first == True:
            is_first = False

    interrupt_event.set()

# buy in Autoshow
async def Macro_Autoshow(interrupt_event, loop=111): # 999sp / 9sp per car = 111 cars
    current_loop = 0
    while interrupt_event.is_set() == False:
        if (loop == 0): # set loop 0 to run infinitely
            current_loop += 1
            print(f"{current_loop} / INF")
        else:
            print(f"{current_loop} / {loop}")
            if (current_loop < loop):
                current_loop += 1
            else:
                print("Completed.")
                break

        # open Autoshow menu
        await FindImage("Autoshow.png", 0.75)
        pyautogui.press("left", presses=3, interval=0.05)
        pyautogui.press("right")
        pyautogui.press("enter")

        # wait for the menu to load
        await asyncio.sleep(0.5)
        await FindImage("Esc.png", 0.75, interval=0.1)

        # move to "Peel" section
        await asyncio.sleep(0.5)
        pyautogui.press("backspace") # open search window
        # focus on the search window. if not doing this, scrolling will work weirdly
        pyautogui.moveTo(1, 1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        
        location = await FindImage("Peel.png", 0.9, scroll=-5)
        pyautogui.moveTo(location)
        pyautogui.press("enter")

        # validate that the Peel Trident is selected
        await asyncio.sleep(0.5)
        await FindImage("Trident.png", 0.9, interval=0.1)
        # buy Trident
        pyautogui.press("enter")

        # wait for the select design menu to load
        await asyncio.sleep(0.1)
        await FindImage("Esc.png", 0.75)

        await asyncio.sleep(0.5)
        pyautogui.press('y') # enter the color menu
        await asyncio.sleep(0.5)
        pyautogui.press("enter") # select default color
        await asyncio.sleep(0.5)
        pyautogui.press("enter") # confirm color
        await asyncio.sleep(0.5)
        pyautogui.press("enter") # confirm purchase

        # wait for the Forza Vista to load
        await asyncio.sleep(0.5)
        await FindImage("Esc.png", 0.75, interval=0.1)
        # exit Forza Vista
        await asyncio.sleep(1)
        pyautogui.press("esc") # back to the Autoshow menu

        # wait for the Autoshow menu to load
        await asyncio.sleep(0.5)
        await FindImage("Esc.png", 0.75, interval=0.1)
        # enter the Upgrade & Tuning menu
        await asyncio.sleep(0.5)
        pyautogui.press("pagedown")
        pyautogui.press("left")
        pyautogui.press("enter")
        # wait for the Upgrade & Tuning menu to load
        await asyncio.sleep(0.5)
        await FindImage("Esc.png", 0.75, interval=0.1)
        """ pyautogui.press("enter") # discard "New Upgrades Available" popup """
        # enter Car Mastery menu
        await asyncio.sleep(0.5)
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
        await asyncio.sleep(0.5)
        is_unlocked = await UnlockPerk() # unlock first perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.5)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock second perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.5)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock third perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.5)
        pyautogui.press("up")
        is_unlocked = await UnlockPerk() # unlock fourth perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.5)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(0.5)
        pyautogui.press("esc") # back to Upgrades & Tuning menu

        await asyncio.sleep(0.5)
        await FindImage("Esc.png", 0.75, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("esc") # back to Garage menu

        await asyncio.sleep(0.5)
        await FindImage("Esc.png", 0.75, interval=0.1)
        await asyncio.sleep(0.1)
        pyautogui.press("pageup") # back to Buy & Sell menu

    interrupt_event.set()

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