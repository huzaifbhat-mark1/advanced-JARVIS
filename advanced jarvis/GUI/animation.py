import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os

def run_gui():
    root = tk.Tk()
    root.title("JARVIS UI")
    root.geometry("500x500")
    root.resizable(False, False)

    lbl = tk.Label(root)
    lbl.pack()

    # Path to the gif
    gif_path = os.path.join(os.path.dirname(__file__), "jarvis.gif")

    # Load gif
    try:
        gif = Image.open(gif_path)
    except FileNotFoundError:
        print(f"GIF not found at {gif_path}")
        return

    frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    def animate(index):
        lbl.config(image=frames[index])
        root.after(50, animate, (index + 1) % len(frames))

    animate(0)
    root.mainloop()
