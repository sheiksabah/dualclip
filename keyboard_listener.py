from pynput import keyboard
import time
import threading
from clipboard_manager import ClipboardManager

current_time = None
last_time_copy = None
pressed_keys = set()
copy_combo = {keyboard.Key.ctrl, keyboard.KeyCode.from_char('c')}
timer = None

clipboard = ClipboardManager()

def save_slot_one():
    global last_time_copy
    print("Saved to slot 1")
    clipboard.save_clipboard(1)
    print("Slots:", clipboard.clipboard_slots)
    last_time_copy = None

def on_press(key):
    global last_time_copy, timer
    pressed_keys.add(key)
    print("Key pressed:", key)

    if pressed_keys == copy_combo:

            if last_time_copy is None:
               last_time_copy = time.monotonic()

               timer = threading.Timer(0.35, save_slot_one)
               timer.start()
            else:
                current_time = time.monotonic()
                elapsed_time = current_time - last_time_copy
                if elapsed_time <= 0.35:
                    print(pressed_keys)
                    last_time_copy = None
                    timer.cancel()
                    clipboard.save_clipboard(2)
                    print("Slots:", clipboard.clipboard_slots)
                else:
                    last_time_copy = current_time
                    timer = threading.Timer(0.35, save_slot_one)
                    timer.start()

def on_release(key):
    pressed_keys.discard(key)


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()