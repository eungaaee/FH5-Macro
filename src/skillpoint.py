import asyncio

from modules.notifybot import ready_event, send_message, start_bot, close_bot

import pyautogui
import keyboard


async def FindImage(file_name, confidence, interval=0):
    while True:
        if (interval > 0):
            await asyncio.sleep(interval)
        try:
            location = await asyncio.to_thread(pyautogui.locateOnScreen, f"./Images/{file_name}", grayscale=True, confidence=confidence) # using the confidence parameter will force to use _locateAll_opencv() instead of _locateAll_pillow()
            return location
        except pyautogui.ImageNotFoundException:
            continue


async def Macro(interrupt_event, loop=100): # 10sp * 100 = 1000sp
    current_loop = 0
    while interrupt_event.is_set() == False:
        if (loop == 0): # set loop 0 to run infinitely
            current_loop += 1
            print(f"{current_loop} / INF")
            await send_message(f"{current_loop} / INF")
        else:
            if (current_loop < loop):
                current_loop += 1
                print(f"{current_loop} / {loop}")
                await send_message(f"{current_loop} / {loop}")
            else:
                print("Completed.")
                await send_message("Completed.")
                interrupt_event.set()
                break

        startraceevent_location = await FindImage("StartRaceEvent.png", 0.75, interval=0.1)
        pyautogui.moveTo(startraceevent_location)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        """ pyautogui.press("left")
        pyautogui.press("up")
        pyautogui.press("enter") """

        await asyncio.sleep(2)
        pyautogui.keyDown('w')

        await FindImage("X.png", 0.75, interval=0.1) # wait for the restart button
        pyautogui.keyUp('w')
        pyautogui.press('x') # restart event
        await asyncio(0.25)
        pyautogui.press("enter") # confirm restart


async def Stopper(interrupt_event):
    while interrupt_event.is_set() == False:
        await asyncio.sleep(0.1)
        if await asyncio.to_thread(keyboard.is_pressed, "F2"): # run the blocking function in a separate thread
            interrupt_event.set()
            print("Script will be stopped after the current loop.")
            await send_message("Script will be stopped after the current loop.")


async def main():
    # start the bot
    bot_task = asyncio.create_task(start_bot())
    await ready_event.wait()  # wait until the bot is ready

    # wait for F1 key to start
    print("Script ready. Press F1 to start the script.")
    await send_message("Script ready.")
    await asyncio.to_thread(keyboard.wait, "F1") # run the blocking function in a separate thread
    print("Script started.")
    await send_message("Script started.")

    interrupt_event = asyncio.Event()
    await asyncio.gather(Macro(interrupt_event), Stopper(interrupt_event))

    print("Exiting the script.")
    await send_message("Exiting the script.")

    await close_bot()


if __name__ == "__main__":
    asyncio.run(main())