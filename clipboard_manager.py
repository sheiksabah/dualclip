import pyperclip

class ClipboardManager:

    def __init__(self):
        self.clipboard_slots = {
            1 : None, 
            2 : None
        }

    def save_clipboard(self, slot):
        self.clipboard_slots[slot] = pyperclip.paste()

    def paste_clipboard(self, slot):
        pyperclip.copy(self.clipboard_slots[slot])
