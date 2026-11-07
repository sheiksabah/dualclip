from clipboard_manager import ClipboardManager
import pyperclip

clipboard = ClipboardManager()

# Save current system clipboard into slot 1
pyperclip.copy("Hello, World!")
clipboard.save_clipboard(1)

pyperclip.copy("Hello, China!")
clipboard.save_clipboard(2)

# Display both slots
print(clipboard.clipboard_slots)

