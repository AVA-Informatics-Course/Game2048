"""
Sets up and runs the 2048 game using Tkinter.
"""

from tkinter import Tk
from ui_manager import Game2048UI

if __name__ == "__main__":
    root = Tk()
    app = Game2048UI(root)
    root.mainloop()