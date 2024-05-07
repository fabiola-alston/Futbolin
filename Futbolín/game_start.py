from game_assets import *
from game import gameRun

def preGameRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE, GAME_MODE, GOALIE_MODE):
    window = Toplevel(root)
    window.title("About")
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

    def runGame():
        selectSound()
        window.destroy()
        gameRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE, GAME_MODE, GOALIE_MODE, SELECTED_TEAM2, SELECTED_ATTACKER2, SELECTED_GOALIE2)

    if SELECTED_TEAM == 1:
        directory = "Samurai Blue"
        photo = "japan_team_badge"
    elif SELECTED_TEAM == 2:
        directory = "Real Madrid"
        photo = "real_madrid_badge"
    else:
        directory = "Manchester United"
        photo = "manchester_team_badge"

    title_label = Label(window, text="HOME TEAM:", font=font1, bg="black", fg="white")
    title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    team_img = Image.open(f"Images/{photo}.png")
    team_img = team_img.resize((100, 136), 4)
    team_tk = ImageTk.PhotoImage(team_img)
    team_label = Label(window, image=team_tk, bg="black")
    team_label.place(relx=0.3, rely=0.25, anchor=CENTER)

    att_img = Image.open(f"Images/Team Players/{directory}/attacker{str(SELECTED_ATTACKER)}.png")
    att_img = att_img.resize((40, 80), 4)
    att_tk = ImageTk.PhotoImage(att_img)
    att_label = Label(window, image=att_tk, bg="black")
    att_label.place(relx=0.5, rely=0.25, anchor=CENTER)

    go_img = Image.open(f"Images/Team Players/{directory}/goalie{str(SELECTED_GOALIE)}.png")
    go_img = go_img.resize((40, 80), 4)
    go_tk = ImageTk.PhotoImage(go_img)
    go_label = Label(window, image=go_tk, bg="black")
    go_label.place(relx=0.6, rely=0.25, anchor=CENTER)

    def randTeam():
        team = random.randint(1,3)
        if team == SELECTED_TEAM:
            randTeam()
        else:
            return team

    SELECTED_TEAM2 = randTeam()

    if SELECTED_TEAM2 == 1:
        directory2 = "Samurai Blue"
        photo2 = "japan_team_badge"
    elif SELECTED_TEAM2 == 2:
        directory2 = "Real Madrid"
        photo2 = "real_madrid_badge"
    else:
        directory2 = "Manchester United"
        photo2 = "manchester_team_badge"

    SELECTED_ATTACKER2 = random.randint(1,3)

    SELECTED_GOALIE2 = random.randint(1,3)

    title2_label = Label(window, text="OPPONENT TEAM:", font=font1, bg="black", fg="white")
    title2_label.place(relx=0.5, rely=0.45, anchor=CENTER)

    team2_img = Image.open(f"Images/{photo2}.png")
    team2_img = team2_img.resize((100, 136), 4)
    team2_tk = ImageTk.PhotoImage(team2_img)
    team2_label = Label(window, image=team2_tk, bg="black")
    team2_label.place(relx=0.3, rely=0.6, anchor=CENTER)

    att2_img = Image.open(f"Images/Team Players/{directory2}/attacker{str(SELECTED_ATTACKER2)}.png")
    att2_img = att2_img.resize((40, 80), 4)
    att2_tk = ImageTk.PhotoImage(att2_img)
    att2_label = Label(window, image=att2_tk, bg="black")
    att2_label.place(relx=0.5, rely=0.6, anchor=CENTER)

    go2_img = Image.open(f"Images/Team Players/{directory2}/goalie{str(SELECTED_GOALIE2)}.png")
    go2_img = go2_img.resize((40, 80), 4)
    go2_tk = ImageTk.PhotoImage(go2_img)
    go2_label = Label(window, image=go2_tk, bg="black")
    go2_label.place(relx=0.6, rely=0.6, anchor=CENTER)



    back_button = Button(window, text="Back", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=closeWindow)
    back_button.place(relx=0.4, rely=0.85, anchor=CENTER)

    continue_button = Button(window, text="Continue", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=runGame)
    continue_button.place(relx=0.6, rely=0.85, anchor=CENTER)

    window.protocol("WM_DELETE_WINDOW", closeGame)

    root.mainloop()