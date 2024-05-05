from game_assets import *

def gameRun(root, SELECTED_TEAM, SELECTED_ATTACKER, SELECTED_GOALIE):
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
