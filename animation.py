import tkinter as tk
from PIL import Image, ImageTk

def play_animation(preroot, animation_label):
    frames = [ImageTk.PhotoImage(Image.open(f"frame_{i}.png")) for i in range(1, 5)]
    forward = True

    def update_frame(index):
        nonlocal forward
        frame = frames[index]
        animation_label.config(image=frame)
        
        index = index + 1 if forward else index - 1
        if index == len(frames) - 1:
            forward = False
        if index == 0:
            forward = True

        preroot.after(100, update_frame, index)

    update_frame(0)
