from clipboard_manager import ClipboardManager
import pyperclip

clipboard = ClipboardManager()

pyperclip.copy("Hello, World!")
clipboard.save_clipboard(1)

pyperclip.copy("Hello, China!")
clipboard.save_clipboard(2)

print(clipboard.clipboard_slots)

