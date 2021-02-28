import sys
import tkinter as tk 
import Tkinter as Tk 

"""
class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-zoomed', True)
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.mainloop()
"""
state = False

def toggle_fullscreen(event=None):
    state = not self.state  # Just toggling the boolean
    tk.attributes("-fullscreen", state)
    return "break"

def end_fullscreen(event=None):
    state = False
    tk.attributes("-fullscreen", False)
    return "break"

root = tk.Tk()

tk.attributes('-zoomed', True)
frame = Frame(self.tk)
frame.pack()
tk.bind("<F11>", self.toggle_fullscreen)
tk.bind("<Escape>", self.end_fullscreen)

root.mainloop()