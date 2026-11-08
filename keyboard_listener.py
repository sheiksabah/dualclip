from pynput import keyboard
import time

current_time = None
last_time_copy = None
pressed_keys = set()
copy_combo = {keyboard.Key.ctrl, keyboard.Keycode.from_char('c')}

def on_press(key):
    global last_time_copy 
    pressed_keys.add(key)
    if pressed_keys == copy_combo:

            if last_time_copy is None:
               last_time_copy = time.time()
               print(pressed_keys)
            else:
                current_time = time.time()
                elapsed_time = current_time - last_time_copy
                if elapsed_time <= 0.35:
                    print(pressed_keys)
                    last_time_copy = None
                else:
                    last_time_copy = current_time
                    print(pressed_keys)       

def on_release(key):
    pressed_keys.discard(key)


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()