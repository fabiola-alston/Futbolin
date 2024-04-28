from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
import pygame

from about import aboutRun
from settings import settingsRun
from team_select import teamSelectRun

def titleScreen():
    root = Tk()
    root.title("Futbolín")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    root.geometry(f"{width}x{height}+{round(screen_width/2)-int(width/2)}+{round(screen_height/2)-int(height/1.8)}")
    root.resizable(False, False)
    root.configure(bg="black")
    # root.eval("tk::PlaceWindow . center")

    # pygame music
    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/main_theme.mp3")
    pygame.mixer.music.play(-1)

    # fonts
    font1 = ("retro gaming", 16)

    # button functions
    def aboutScreen():
        root.withdraw()
        aboutRun(root)

    def settingsScreen():
        root.withdraw()
        settingsRun(root)

    def gameScreen():
        root.withdraw()
        teamSelectRun(root)

    frame = Frame(root, bg="#42a529", width=500, height=315, highlightthickness=3, highlightbackground="#2c541b")
    frame.place(relx=0.5, rely=0.3, anchor=CENTER)

    bg_img = Image.open("Images/title_bg.png")
    bg_img = bg_img.resize((400, 300), 3)
    tk_bg_img = ImageTk.PhotoImage(bg_img)
    bg_label = Label(frame, image=tk_bg_img, bg="#42a529")
    bg_label.place(relx=0.5, rely=0.5, anchor=CENTER)


    play_button = Button(root, text="Play", font=font1, borderless=1, borderwidth=2, highlightthickness=3, relief="raised",
                         bg="#ff0000", fg="white", overbackground="#59d600", focuscolor="#ff0000", activebackground="#59d600", padx=3, command=gameScreen)
    play_button.place(relx=0.5, rely=0.65, anchor=CENTER)

    settings_button = Button(root, text="Settings", font=font1, borderless=1, borderwidth=2, highlightthickness=3, relief="raised",
                         bg="#ff0000", fg="white", overbackground="#59d600", focuscolor="#ff0000", activebackground="#59d600", command=settingsScreen)
    settings_button.place(relx=0.5, rely=0.75, anchor=CENTER)

    about_button = Button(root, text="About", font=font1, borderless=1, borderwidth=2, highlightthickness=3, relief="raised",
                         bg="#ff0000", fg="white", overbackground="#59d600", focuscolor="#ff0000", activebackground="#59d600", padx=3, command=aboutScreen)
    about_button.place(relx=0.5, rely=0.85, anchor=CENTER)


    root.mainloop()

titleScreen()