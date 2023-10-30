import tkinter as tk
from settings import TITLE, HEIGHT, WIDTH, ICON
from logic import *

window = tk.Tk()
window.resizable(False, False)
window.title(TITLE)
window.geometry(f"{WIDTH}x{HEIGHT}")
window.iconbitmap(ICON)

app_logic(window)

window.mainloop()
