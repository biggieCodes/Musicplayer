import tkinter as tk
from tkinter import filedialog
import pygame
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# Create the main application window
app = tk.Tk()
app.title("Music Player")
app.geometry("500x300")

# Function to open a file and play it
def play_music():
    filepath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if filepath:
        mixer.music.load(filepath)
        mixer.music.play()

# Function to stop the currently playing music
def stop_music():
    mixer.music.stop()

# Create and place widgets
play_button = tk.Button(app, text="Play", command=play_music)
play_button.pack()

stop_button = tk.Button(app, text="Stop", command=stop_music)
stop_button.pack()

# Start the main loop
app.mainloop()
