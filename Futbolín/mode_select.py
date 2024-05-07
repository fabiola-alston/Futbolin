from game_assets import *
from game_start import preGameRun

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
        preGameRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE, GAME_MODE, GOALIE_MODE)

    def modeSelect(mode):
        selectSound()
        global GAME_MODE
        if mode == 1:
            GAME_MODE = 1
            manual_mode_button['bg'] = "#4554ff"
            automatic_mode_button['bg'] = "#085c04"
        elif mode == 2:
            GAME_MODE = 2
            manual_mode_button['bg'] = "#085c04"
            automatic_mode_button['bg'] = "#4554ff"

    def goalieModeSelect(mode):
        selectSound()
        global GOALIE_MODE
        if mode == 1:
            GOALIE_MODE = 1
            twopallette_mode_button['bg'] = "#4554ff"
            threepaletterand_mode_button['bg'] = "#085c04"
            threepalette_mode_button['bg'] = "#085c04"
        elif mode == 2:
            GOALIE_MODE = 2
            twopallette_mode_button['bg'] = "#085c04"
            threepaletterand_mode_button['bg'] = "#4554ff"
            threepalette_mode_button['bg'] = "#085c04"
        elif mode == 3:
            GOALIE_MODE = 3
            twopallette_mode_button['bg'] = "#085c04"
            threepaletterand_mode_button['bg'] = "#085c04"
            threepalette_mode_button['bg'] = "#4554ff"



    # test_button = Button(window, text="PRESS", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
    #                      relief="raised",
    #                      bg="#0000ff", fg="white", overbackground="#3838ff", focuscolor="#0000ff",
    #                      activebackground="#3838ff", pady=15)
    # test_button.place(x=50, y=50)

    title_label = Label(window, text="Select a Game Mode: ", font=font1, bg="black", fg="white")
    title_label.place(relx=0.5, rely=0.15, anchor=CENTER)


    # manual mode button
    manual_mode_button = Button(window, text="Manual", font=font1, bg="#085c04", fg="white", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=lambda: modeSelect(1))
    manual_mode_button.place(relx=0.4, rely=0.25, anchor=CENTER)

    # automatic mode button
    automatic_mode_button = Button(window, text="Automatic", font=font1, bg="#085c04", fg="white", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=lambda: modeSelect(2))
    automatic_mode_button.place(relx=0.6, rely=0.25, anchor=CENTER)

    title2_label = Label(window, text="Select a Goalie Mode: ", font=font1, bg="black", fg="white")
    title2_label.place(relx=0.5, rely=0.35, anchor=CENTER)

    # an1 button
    twopallette_mode_button = Button(window, text="Two Palette Goalie", font=font1, bg="#085c04", fg="white", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=lambda: goalieModeSelect(1))
    twopallette_mode_button.place(relx=0.5, rely=0.45, anchor=CENTER)

    # an2 button
    threepaletterand_mode_button = Button(window, text="Three Palette Goalie (Random)", font=font1, bg="#085c04", fg="white", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=lambda: goalieModeSelect(2))
    threepaletterand_mode_button.place(relx=0.5, rely=0.55, anchor=CENTER)

    # an3 button
    threepalette_mode_button = Button(window, text="Three Palette Goalie", font=font1, bg="#085c04", fg="white", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=lambda: goalieModeSelect(3))
    threepalette_mode_button.place(relx=0.5, rely=0.65, anchor=CENTER)


    # play button
    play_button = Button(window, text="Play", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=runGame)
    play_button.place(relx=0.6, rely=0.85, anchor=CENTER)

    # back button
    back_button = Button(window, text="Back", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=closeWindow)
    back_button.place(relx=0.4, rely=0.85, anchor=CENTER)

    window.protocol("WM_DELETE_WINDOW", closeGame)

    root.mainloop()