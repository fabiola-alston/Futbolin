from natsort import natsorted

from game_assets import *
import natsort

def statsRun(root, goal_num, team):
    window = Toplevel(root)
    window.title("About")
    window.configure(background="black")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    window.geometry(
        f"{width}x{height}+{round(screen_width / 2) - int(width / 2)}+{round(screen_height / 2) - int(height / 1.8)}")

    print(goal_num)
    print(team)

    top = []

    if team == 1:
        directory = 'Scores/samurai.txt'
        with open('Scores/samurai.txt', 'a') as file:
            file.write(f"Goals: {goal_num} - Missed: {5 - goal_num},")

        with open('Scores/samurai.txt', 'r') as file:
            read = file.read().split(',')

        top = natsorted(read, reverse=True)

    elif team == 2:
        directory = 'Scores/realmadrid.txt'
        with open('Scores/realmadrid.txt', 'a') as file:
            file.write(f"Goals: {goal_num} - Missed: {5 - goal_num},")

        with open('Scores/realmadrid.txt', 'r') as file:
            read = file.read().split(',')

        top = natsorted(read, reverse=True)

    elif team == 3:
        directory = 'Scores/manchester.txt'
        with open('Scores/manchester.txt', 'a') as file:
            file.write(f"Goals: {goal_num} - Missed: {5 - goal_num},")

        with open('Scores/manchester.txt', 'r') as file:
            read = file.read().split(',')

        top = natsorted(read, reverse=True)

    title_label = Label(window, text="SCORES", font=font4, bg="black", fg="white", justify="left")
    title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    top_label = Label(window, text=f"Your Score:\nGoals: {goal_num} - Missed: {5 - goal_num}", font=font1, bg="black", fg="white")
    top_label.place(relx=0.5, rely=0.25, anchor=CENTER)

    title2_label = Label(window, text="HIGH SCORES", font=font4, bg="black", fg="white", justify="left")
    title2_label.place(relx=0.5, rely=0.35, anchor=CENTER)


    top1_label = Label(window, text=top[0], font=font1, bg="black", fg="white", justify="left")
    top1_label.place(relx=0.5, rely=0.45, anchor=CENTER)

    top2_label = Label(window, text=top[1], font=font1, bg="black", fg="white", justify="left")
    top2_label.place(relx=0.5, rely=0.55, anchor=CENTER)

    top3_label = Label(window, text=top[2], font=font1, bg="black", fg="white", justify="left")
    top3_label.place(relx=0.5, rely=0.65, anchor=CENTER)

    def clearScore():
        with open(directory, 'w') as file:
            file.write("Goals: 0 - Missed: 0,Goals: 0 - Missed: 0,")

        top1_label.destroy()
        top2_label.destroy()
        top3_label.destroy()

    clear_button = Button(window, text="Delete Scores!", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=clearScore)

    clear_button.place(relx=0.5, rely=0.75, anchor=CENTER)


    def closeGame():
        window.destroy()
        root.destroy()

    def closeWindow():
        selectSound()
        root.deiconify()
        window.destroy()

    back_button = Button(window, text="Back", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=closeWindow)
    back_button.place(relx=0.5, rely=0.85, anchor=CENTER)

    window.protocol("WM_DELETE_WINDOW", closeGame)

    root.mainloop()