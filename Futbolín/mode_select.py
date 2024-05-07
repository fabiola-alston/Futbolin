from game_assets import *
from game import gameRun

def modeRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE):
    window = Toplevel(root)
    window.title("Select Mode")
    window.configure(background="black")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    window.geometry(
        f"{width}x{height}+{round(screen_width / 2) - int(width / 2)}+{round(screen_height / 2) - int(height / 1.8)}")

    def closeGame():
        window.destroy()
        root.destroy()

    def closeWindow():
        selectSound()
        root.deiconify()
        window.destroy()

    global GAME_MODE
    global GOALIE_MODE

    def runGame():
        global GAME_MODE
        selectSound()
        window.destroy()
        print(GOALIE_MODE)
        gameRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE, GAME_MODE, GOALIE_MODE)

    def modeSelect(mode):
        selectSound()
        global GAME_MODE
        if mode == 1:
            GAME_MODE = 1
        elif mode == 2:
            GAME_MODE = 2

    def goalieModeSelect(mode):
        selectSound()
        global GOALIE_MODE
        if mode == 1:
            GOALIE_MODE = 1
        elif mode == 2:
            GOALIE_MODE = 2
        elif mode == 3:
            GOALIE_MODE = 3
        print(GOALIE_MODE)



    test_button = Button(window, text="PRESS", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#0000ff", fg="white", overbackground="#3838ff", focuscolor="#0000ff",
                         activebackground="#3838ff", pady=15)
    test_button.place(x=50, y=50)

    manual_mode_button = Button(window, text="Manual", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=lambda: modeSelect(1))
    manual_mode_button.place(relx=0.5, rely=0.4, anchor=CENTER)

    automatic_mode_button = Button(window, text="Automatic", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                                relief="raised",
                                bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                                activebackground="#ff5252", command=lambda: modeSelect(2))
    automatic_mode_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    twopallette_mode_button = Button(window, text="Two Palette Goalie", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                                relief="raised",
                                bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                                activebackground="#ff5252", command=lambda: goalieModeSelect(1))
    twopallette_mode_button.place(relx=0.2, rely=0.6, anchor=CENTER)

    threepaletterand_mode_button = Button(window, text="Three Palette Goalie (Random)", font=font1, borderless=1, borderwidth=2,
                                   highlightthickness=3,
                                   relief="raised",
                                   bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                                   activebackground="#ff5252", command=lambda: goalieModeSelect(2))
    threepaletterand_mode_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    threepalette_mode_button = Button(window, text="Three Palette Goalie", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                                relief="raised",
                                bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                                activebackground="#ff5252", command=lambda: goalieModeSelect(3))
    threepalette_mode_button.place(relx=0.8, rely=0.6, anchor=CENTER)



    play_button = Button(window, text="Play", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=runGame)
    play_button.place(relx=0.6, rely=0.85, anchor=CENTER)

    back_button = Button(window, text="Back", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=closeWindow)
    back_button.place(relx=0.4, rely=0.85, anchor=CENTER)

    window.protocol("WM_DELETE_WINDOW", closeGame)

    root.mainloop()