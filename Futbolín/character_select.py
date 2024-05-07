from game_assets import *
from mode_select import modeRun

def characterSelectRun(root, SELECTED_TEAM):
    global SELECTED_ATTACKER
    global SELECTED_GOALIE
    global current_select

    # variable para sólo poder escoger un personaje a la vez
    current_select = 0

    window = Toplevel(root)
    window.title("About")
    window.configure(background="black")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    window.geometry(
        f"{width}x{height}+{round(screen_width / 2) - int(width / 2)}+{round(screen_height / 2) - int(height / 1.8)}")

    # determine sprites based on selected team
    # samurai blue
    if SELECTED_TEAM == 1:
        team_directory = "Samurai Blue"
    elif SELECTED_TEAM == 2:
        team_directory = "Real Madrid"
    else:
        team_directory = "Manchester United"

    at1 = Image.open(f"Images/Team Players/{team_directory}/attacker1.png")
    at1 = at1.resize((30, 60), 5)
    at1_tk = ImageTk.PhotoImage(at1)

    at2 = Image.open(f"Images/Team Players/{team_directory}/attacker2.png")
    at2 = at2.resize((30, 60), 5)
    at2_tk = ImageTk.PhotoImage(at2)

    at3 = Image.open(f"Images/Team Players/{team_directory}/attacker3.png")
    at3 = at3.resize((30, 60), 5)
    at3_tk = ImageTk.PhotoImage(at3)

    go1 = Image.open(f"Images/Team Players/{team_directory}/goalie1.png")
    go1 = go1.resize((30, 60), 5)
    go1_tk = ImageTk.PhotoImage(go1)

    go2 = Image.open(f"Images/Team Players/{team_directory}/goalie2.png")
    go2 = go2.resize((30, 60), 5)
    go2_tk = ImageTk.PhotoImage(go2)

    go3 = Image.open(f"Images/Team Players/{team_directory}/goalie3.png")
    go3 = go3.resize((30, 60), 5)
    go3_tk = ImageTk.PhotoImage(go3)


    title_label = Label(window, text="Select an attacker and a goalie: ", font=font1, bg="black", fg="white")
    title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    attacker1_button = Button(window, image=at1_tk, font=font1, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a")
    attacker1_button.place(relx=0.2, rely=0.25, anchor=CENTER)

    attacker2_button = Button(window, image=at2_tk, font=font1, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a")
    attacker2_button.place(relx=0.5, rely=0.25, anchor=CENTER)

    attacker3_button = Button(window, image=at3_tk, font=font1, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a")
    attacker3_button.place(relx=0.8, rely=0.25, anchor=CENTER)

    goalie1_button = Button(window, image=go1_tk, font=font1, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a")
    goalie1_button.place(relx=0.2, rely=0.45, anchor=CENTER)

    goalie2_button = Button(window, image=go2_tk, font=font1, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a")
    goalie2_button.place(relx=0.5, rely=0.45, anchor=CENTER)

    goalie3_button = Button(window, image=go3_tk, font=font1, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a")
    goalie3_button.place(relx=0.8, rely=0.45, anchor=CENTER)

    scale = Scale(window, from_=1, to=3, orient=HORIZONTAL, bg="black", fg="white", font=font1, length=500)
    scale.place(relx=0.5, rely=0.6, anchor=CENTER)

    # seleccionar attacker vía scale
    def attackerSelectScale():
        global current_select

        current_select = 0

        selectSound()
        def checkScale():
            global SELECTED_ATTACKER
            scale_value = scale.get()
            SELECTED_ATTACKER = scale_value
            if scale_value == 1:
                attacker1_button['bg'] = "#4554ff"
                attacker2_button['bg'] = "#085c04"
                attacker3_button['bg'] = "#085c04"
            elif scale_value == 2:
                attacker1_button['bg'] = "#085c04"
                attacker2_button['bg'] = "#4554ff"
                attacker3_button['bg'] = "#085c04"
            elif scale_value == 3:
                attacker1_button['bg'] = "#085c04"
                attacker2_button['bg'] = "#085c04"
                attacker3_button['bg'] = "#4554ff"

            if current_select == 0:
                scale.after(200, checkScale)

        checkScale()

    # seleccionar goalie vía scale
    def goalieSelectScale():
        global current_select

        current_select = 1

        selectSound()
        def checkScale():
            global SELECTED_GOALIE
            scale_value = scale.get()
            SELECTED_GOALIE = scale_value
            if scale_value == 1:
                goalie1_button['bg'] = "#4554ff"
                goalie2_button['bg'] = "#085c04"
                goalie3_button['bg'] = "#085c04"
            elif scale_value == 2:
                goalie1_button['bg'] = "#085c04"
                goalie2_button['bg'] = "#4554ff"
                goalie3_button['bg'] = "#085c04"
            elif scale_value == 3:
                goalie1_button['bg'] = "#085c04"
                goalie2_button['bg'] = "#085c04"
                goalie3_button['bg'] = "#4554ff"

            if current_select == 1:
                scale.after(200, checkScale)

        checkScale()

    def closeGame():
        window.destroy()
        root.destroy()

    def closeWindow():
        selectSound()
        root.deiconify()
        window.destroy()

    def gameWindow():
        selectSound()
        window.destroy()
        modeRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE)

    set_attacker_button = Button(window, text="Set Attacker", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=attackerSelectScale)
    set_attacker_button.place(relx=0.3, rely=0.75, anchor=CENTER)

    set_goalie_button = Button(window, text="Set Goalie", font=font1, borderless=1, borderwidth=2,
                                 highlightthickness=3,
                                 relief="raised",
                                 bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                                 activebackground="#ff5252", padx=5, command=goalieSelectScale)
    set_goalie_button.place(relx=0.7, rely=0.75, anchor=CENTER)

    back_button = Button(window, text="Back", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", padx=5, command=closeWindow)
    back_button.place(relx=0.4, rely=0.85, anchor=CENTER)

    continue_button = Button(window, text="Continue", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=gameWindow)
    continue_button.place(relx=0.6, rely=0.85, anchor=CENTER)

    attackerSelectScale()

    window.protocol("WM_DELETE_WINDOW", closeGame)

    root.mainloop()