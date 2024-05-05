from about import aboutRun
from settings import settingsRun
from team_select import teamSelectRun
from game_assets import *

def titleScreen():
    root = Tk()
    root.title("Futbolín")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    root.geometry(f"{width}x{height}+{round(screen_width/2)-int(width/2)}+{round(screen_height/2)-int(height/1.8)}")
    root.configure(bg="black")

    # pygame music
    pygame.mixer.music.load("Sounds/main_theme.mp3")
    # pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)

    # button functions
    def aboutScreen():
        selectSound()
        root.withdraw()
        aboutRun(root)

    def settingsScreen():
        selectSound()
        root.withdraw()
        settingsRun(root)

    def gameScreen():
        selectSound()
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
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000", activebackground="#ff5252", padx=3, command=gameScreen)
    play_button.place(relx=0.5, rely=0.65, anchor=CENTER)

    settings_button = Button(root, text="Settings", font=font1, borderless=1, borderwidth=2, highlightthickness=3, relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000", activebackground="#ff5252", padx=1, command=settingsScreen)
    settings_button.place(relx=0.5, rely=0.75, anchor=CENTER)

    about_button = Button(root, text="About", font=font1, borderless=1, borderwidth=2, highlightthickness=3, relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000", activebackground="#ff5252", padx=3, command=aboutScreen)
    about_button.place(relx=0.5, rely=0.85, anchor=CENTER)


    root.mainloop()

titleScreen()