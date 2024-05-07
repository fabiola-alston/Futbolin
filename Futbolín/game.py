from game_assets import *
from board_data import randomBallData

def gameRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE, GAME_MODE, GOALIE_MODE, SELECTED_TEAM2, SELECTED_ATTACKER2, SELECTED_GOALIE2):
    window = Toplevel(root)
    window.title("Game")
    window.configure(background="black")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    window.geometry(f"{width}x{height}+{round(screen_width / 2) - int(width / 2)}+{round(screen_height / 2) - int(height / 1.8)}")

    print(f"GAME. SELECTED TEAM {SELECTED_TEAM}")
    print(f"ATTACKER: {SELECTED_ATTACKER}")
    print(f"GOALIE: {SELECTED_GOALIE}")
    print(f"GOALIE MODE: {GOALIE_MODE}")

    # to show the correct selected team sprites
    if SELECTED_TEAM == 1:
        directory = "Samurai Blue"
    elif SELECTED_TEAM == 2:
        directory = "Real Madrid"
    else:
        directory = "Manchester United"

    if SELECTED_TEAM2 == 1:
        directory2 = "Samurai Blue"
    elif SELECTED_TEAM2 == 2:
        directory2 = "Real Madrid"
    else:
        directory2 = "Manchester United"

    # to show attacker and goalie sprite
    attacker_dir = str(SELECTED_ATTACKER)
    goalie_dir = str(SELECTED_GOALIE)

    team = ['attacker1', 'attacker2', 'attacker3', 'goalie1', 'goalie2', 'goalie3']

    team.remove(f"attacker{attacker_dir}")
    team.remove(f"goalie{goalie_dir}")

    # mode assign
    if GAME_MODE == 1:
        mode = "MANUAL"
    elif GAME_MODE == 2:
        mode = "AUTOMATIC"

    if GOALIE_MODE == 1:
        goalie_mode = "AN1"
    elif GOALIE_MODE == 2:
        goalie_mode = "AN2"
    elif GOALIE_MODE == 3:
        goalie_mode = "AN3"

    # round number
    global round_num
    round_num = 0

    # limits amount of shots per round (1)
    global shot_flag
    shot_flag = 0

    # score counter
    global score
    score = 0

    def closeGame():
        window.destroy()
        root.destroy()

    def closeWindow():
        selectSound()
        root.deiconify()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", closeGame)

    game_canvas = Canvas(window, bg="black", width=800, height=600, highlightbackground="black")
    game_canvas.place(x=0, y=0)

    back_button = Button(game_canvas, text="QUIT", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="black", fg="white", overbackground="gray", focuscolor="black",
                         activebackground="gray", padx=-20, command=closeWindow)
    back_button.place(x=20, y=20)

    home_score_label = Label(game_canvas, text=f"{directory.upper()}: {score}", font=font2, bg="black", fg="white")
    home_score_label.place(relx=0.18, rely=0.08, anchor=W)

    opp_score_label = Label(game_canvas, text=f"{directory2.upper()}: 0", font=font2, bg="black", fg="white")
    opp_score_label.place(relx=0.18, rely=0.12, anchor=W)

    mode_label = Label(game_canvas, text=f"MODE: {mode}, {goalie_mode}", font=font2, bg="black", fg="white")
    mode_label.place(relx=0.45, rely=0.12, anchor=W)

    round_num_label = Label(game_canvas, text=f"ROUND: {round_num}", font=font2, bg="black", fg="white")
    round_num_label.place(relx=0.7, rely=0.12, anchor=W)

    field_img = Image.open("Images/field.png")
    field_img = field_img.resize((500, 350), 3)
    field_img_tk = ImageTk.PhotoImage(field_img)
    field = game_canvas.create_image((150, 100), anchor=NW, image=field_img_tk)

    att_img = Image.open(f"Images/Team Players/{directory}/attacker{attacker_dir}.png")
    att_img = att_img.resize((40, 80), 4)
    att_tk = ImageTk.PhotoImage(att_img)
    attacker = game_canvas.create_image((350, 370), anchor=NW, image=att_tk)

    go_img = Image.open(f"Images/Team Players/{directory}/goalie{goalie_dir}.png")
    go_img = go_img.resize((40, 80), 4)
    go_tk = ImageTk.PhotoImage(go_img)
    goalie = game_canvas.create_image((380, 210), anchor=NW, image=go_tk)

    ball_img = Image.open("Images/soccer_ball.png")
    ball_img = ball_img.resize((40, 40), 4)
    ball_tk = ImageTk.PhotoImage(ball_img)
    global soccer_ball
    soccer_ball = game_canvas.create_image((380, 350), anchor=NW, image=ball_tk)

    bench_img = Image.open("Images/bench.png")
    bench_img = bench_img.resize((160, 100), 4)
    bench_tk = ImageTk.PhotoImage(bench_img)
    bench = game_canvas.create_image((50, 480), anchor=NW, image=bench_tk)

    # sprites random bench
    random_player1 = team[random.randint(0, len(team) - 1)]
    team.remove(random_player1)

    random_player2 = team[random.randint(0, len(team) - 1)]
    team.remove(random_player2)

    random_player3 = team[random.randint(0, len(team) - 1)]
    team.remove(random_player3)

    player1_img = Image.open(f"Images/Team Players/{directory}/{random_player1}.png")
    player1_img = player1_img.resize((40, 80), 4)
    player1_tk = ImageTk.PhotoImage(player1_img)
    player1 = game_canvas.create_image((55, 480), anchor=NW, image=player1_tk)

    player2_img = Image.open(f"Images/Team Players/{directory}/{random_player2}.png")
    player2_img = player2_img.resize((40, 80), 4)
    player2_tk = ImageTk.PhotoImage(player2_img)
    player2 = game_canvas.create_image((100, 480), anchor=NW, image=player2_tk)

    player3_img = Image.open(f"Images/Team Players/{directory}/{random_player3}.png")
    player3_img = player3_img.resize((40, 80), 4)
    player3_tk = ImageTk.PhotoImage(player3_img)
    player3 = game_canvas.create_image((150, 480), anchor=NW, image=player3_tk)

    def oppWin():
        title = Label(game_canvas, text=f"OPPONENT WINS", font=font3, bg="black", fg="red")
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        game_canvas.update()
        time.sleep(2)
        game_canvas.update()
        title.destroy()
        game_canvas.update()

    def homeWin():
        title = Label(game_canvas, text=f"HOME WINS", font=font3, bg="black", fg="blue")
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        game_canvas.update()
        time.sleep(2)
        game_canvas.update()
        title.destroy()
        game_canvas.update()

    def tie():
        title = Label(game_canvas, text=f"TIE", font=font3, bg="black", fg="green")
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        game_canvas.update()
        time.sleep(2)
        game_canvas.update()
        title.destroy()
        game_canvas.update()

    def nextTeam():
        global score
        opp_score = random.randint(0, 5)
        opp_score_label['text'] = f"{directory2.upper()}: {opp_score}"

        title = Label(game_canvas, text=f"Opponent scored {opp_score} goals.", font=font3, bg="black", fg="red")
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        game_canvas.update()
        time.sleep(2)
        game_canvas.update()
        title.destroy()
        game_canvas.update()

        if opp_score > score:
            oppWin()

        elif opp_score < score:
            homeWin()

        elif opp_score == score:
            tie()

    def ballAnimation():
        global soccer_ball
        global round_num

        for i in range(10):
            game_canvas.move(soccer_ball, 0, -10)
            time.sleep(0.025)
            game_canvas.update()

        time.sleep(1)
        game_canvas.update()

        for i in range(10):
            game_canvas.move(soccer_ball, 0, 10)
            time.sleep(0.025)
            game_canvas.update()
        time.sleep(1)
        if round_num <= 5 and GAME_MODE == 2:
            print("IN")
            ballRandScore()
            game_canvas.after(3000, roundTitleAnimation)

        elif round_num <= 5 and GAME_MODE == 1:
            ballRandScore()


    global goalie_pos
    global goalie_pos2
    global goalie_pos3

    def generateGoaliePos():
        global goalie_pos
        global goalie_pos2
        global goalie_pos3

        if GOALIE_MODE == 1:
            goalie_pos = random.randint(1,5)
            goalie_pos2 = goalie_pos + 1
            goalie_pos3 = 0

        elif GOALIE_MODE == 2:
            goalie_pos = random.randint(1, 4)
            goalie_pos2 = goalie_pos + 1
            goalie_pos3 = goalie_pos2 + 1

        elif GOALIE_MODE == 3:
            goalie_ind = random.randint(0,1)
            if goalie_ind == 0:
                goalie_pos = 1
                goalie_pos2 = 2
                goalie_pos3 = 3
            elif goalie_ind == 1:
                goalie_pos = 4
                goalie_pos2 = 5
                goalie_pos3 = 6


    def roundTitleAnimation():
        global title
        global round_num
        global shot_flag

        generateGoaliePos()

        def deleteTitle():
            global title
            global shot_flag
            title.destroy()
            shot_flag = 0
        def displayTitle():
            global title
            title = Label(game_canvas, text=f"ROUND {round_num}", font=font3, bg="black", fg="blue")
            title.place(relx=0.5, rely=0.5, anchor=CENTER)
            game_canvas.after(2000, deleteTitle)

        round_num += 1

        if round_num <= 5:
            round_num_label['text'] = f"ROUND: {round_num}"
            displayTitle()

    roundTitleAnimation()

    def goalAnimation():
        global score
        def deleteTitle():
            global title
            title.destroy()
            if round_num == 5:
                game_canvas.after(1000, nextTeam)
        def displayTitle():
            global title
            cheerSound()
            title = Label(game_canvas, text=f"GOAL", font=font3, bg="black", fg="blue")
            title.place(relx=0.5, rely=0.5, anchor=CENTER)
            game_canvas.after(2000, deleteTitle)

        if round_num <= 5:
            score += 1
            home_score_label['text'] = f"{directory.upper()}: {score}"
            displayTitle()

    def noGoalAnimation():
        def deleteTitle():
            global title
            title.destroy()
            if round_num == 5:
                game_canvas.after(1000, nextTeam)
        def displayTitle():
            global title
            booSound()
            title = Label(game_canvas, text=f"NO GOAL", font=font3, bg="black", fg="red")
            title.place(relx=0.5, rely=0.5, anchor=CENTER)
            game_canvas.after(2000, deleteTitle)

        if round_num <= 5:
            displayTitle()

    def ballRandScore():
        global goalie_pos
        global goalie_pos2
        global goalie_pos3

        goal = randomBallData()
        print(goal)
        if goal == goalie_pos or goal == goalie_pos2 or goal == goalie_pos3:
            noGoalAnimation()
        else:
            goalAnimation()


    # every round that is played, function
    def playRound():
        global round_num
        global soccer_ball
        global shot_flag

        if GAME_MODE == 2:
            def shootBall():
                global shot_flag
                if round_num <= 5 and shot_flag == 0:
                    shootSound()
                    shot_flag = 1
                    ballAnimation()
                else:
                    dullSound()
            shootBall()
        else:
            if round_num <= 5 and shot_flag == 0:
                shootSound()
                shot_flag = 1
                round_num_label['text'] = f"ROUND: {round_num}"
                ballAnimation()

            else:
                dullSound()


    if GAME_MODE == 1:
        def nextRound():
            global round_num
            global shot_flag

            if round_num < 5:
                selectSound()
                shot_flag = 1
                roundTitleAnimation()
            else:
                dullSound()

        next_round_button = Button(game_canvas, text="NEXT ROUND", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=nextRound)
        next_round_button.place(relx=0.5, rely=0.9, anchor=CENTER)


    shoot_button = Button(game_canvas, text="SHOOT", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=playRound)
    shoot_button.place(relx=0.8, rely=0.9, anchor=CENTER)

    root.mainloop()

# root = Tk()
# root.withdraw()
# gameRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE, GAME_MODE, GOALIE_MODE)
# root.mainloop()