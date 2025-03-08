import asyncio
import time

import pyautogui
import keyboard


slow_mode = False
y_icon_location = (370, 1000) # A (x, y) of the 'Y' icon's white area
enter_icon_location = (85, 1000) # A (x, y) of the "Enter" icon's white area
color_white = (255, 255, 255)


async def GetPixelColor(x, y):
    color = await asyncio.to_thread(pyautogui.pixel, x, y)
    return color


async def Buyout():
    # attempt to buyout
    pyautogui.press("down")
    pyautogui.press("enter")
    await asyncio.sleep(0.14 if slow_mode else 0.1)
    pyautogui.press("enter")

    # wait for the Buyout message and press Enter
    await asyncio.sleep(1)
    while sum(await GetPixelColor(*enter_icon_location)) < sum(color_white) * 0.75:
        await asyncio.sleep(0.1)
    pyautogui.press("enter")

    await asyncio.sleep(0.14 if slow_mode else 0.1)
    pyautogui.press("esc")
    await asyncio.sleep(0.14 if slow_mode else 0.1)


def DetectBuyKey():
    while True:
        key_event = keyboard.read_event(suppress=False)
        if key_event.name == 'b' and key_event.event_type == keyboard.KEY_DOWN:
            return True
        elif key_event.name == 'n' and key_event.event_type == keyboard.KEY_DOWN:
            return False


async def Macro(interrupt_event, advanced_search=False, halfauto=False, halfauto_scroll=60):
    advanced_search |= halfauto
    pyautogui.moveTo(1, 1) # move the cursor to the top left corner to prevent interference

    while interrupt_event.is_set() == False:
        pyautogui.press("enter")
        await asyncio.sleep(0.18 if slow_mode else 0.14)
        if advanced_search:
            pyautogui.press('x')
            await asyncio.sleep(0.18 if slow_mode else 0.14)
        pyautogui.press("enter")

        if advanced_search: # advanced search takes longer to load
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(0.8 if slow_mode else 0.72)

        if halfauto:
            pyautogui.press("down", presses=halfauto_scroll, interval=0.01) # scroll down to the fresh 59m auctions
            if await asyncio.to_thread(DetectBuyKey):
                pyautogui.press('y')
                await asyncio.sleep(0.1)
                await Buyout()
        else:
            if sum(await GetPixelColor(*y_icon_location)) >= sum(color_white) * 0.75: # if search result is not empty
                print(time.strftime("[%Y-%m-%d / %H:%M:%S] Found!"))
                # spam the Y key
                while True:
                    pyautogui.press('y')
                    if sum(await GetPixelColor(*y_icon_location)) < sum(color_white) * 0.75:
                        await asyncio.sleep(0.12 if slow_mode else 0.1)
                        await Buyout()
                        break
                    else:
                        await asyncio.sleep(0.05)

        pyautogui.press("esc")
        await asyncio.sleep(0.7 if slow_mode else 0.6)


async def Stopper(interrupt_event):
    while interrupt_event.is_set() == False:
        await asyncio.sleep(0.1)
        if await asyncio.to_thread(keyboard.is_pressed, "F2"): # run the blocking function in a separate thread
            interrupt_event.set()
            print("Script will be stopped after the current loop.")


async def main():
    # wait for F1 key to start
    print("Script ready. Press F1 to start the script.")
    await asyncio.to_thread(keyboard.wait, "F1") # run the blocking function in a separate thread
    print("Script started.")

    interrupt_event = asyncio.Event()
    await asyncio.gather(Macro(interrupt_event), Stopper(interrupt_event))

    print("Exiting the script.")


def IconLocationFinder(interval=0.5):
    while True:
        position = pyautogui.position()
        print(f"{position} / color {pyautogui.pixel(*position)}")
        print(f"y_icon_location {y_icon_location} / color {pyautogui.pixel(*y_icon_location)}")
        print(f"enter_icon_location {enter_icon_location} / color {pyautogui.pixel(*enter_icon_location)}\n\n")
        time.sleep(interval)


if __name__ == "__main__":
    asyncio.run(main())