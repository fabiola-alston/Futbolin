from game_assets import *
from game import gameRun

def teamSelectRun(root):
    global SELECTED_TEAM
    window = Toplevel(root)
    window.title("Select Team")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    window.geometry(f"{width}x{height}+{round(screen_width / 2) - int(width / 2)}+{round(screen_height / 2) - int(height / 1.8)}")
    window.configure(background="black")

    def selectSamurai():
        SELECTED_TEAM = 0
        selectSound()
        window.destroy()
        gameRun(root, SELECTED_TEAM)

    def selectRealMadrid():
        SELECTED_TEAM = 1
        selectSound()
        window.destroy()
        gameRun(root, SELECTED_TEAM)

    def selectManchester():
        SELECTED_TEAM = 2
        selectSound()
        window.destroy()
        gameRun(root, SELECTED_TEAM)


    title_label = Label(window, text="Select your team: ", font=font1, bg="black", fg="white")
    title_label.place(relx=0.5, rely=0.25, anchor=CENTER)

    samurai_blue_img = Image.open("Images/japan_team_badge.png")
    samurai_blue_img = samurai_blue_img.resize((100, 136), 3)
    samurai_blue_img = ImageTk.PhotoImage(samurai_blue_img)
    samurai_blue_button = Button(window, image=samurai_blue_img, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=selectSamurai)
    samurai_blue_button.place(relx=0.2, rely=0.5, anchor=CENTER)

    real_madrid_img = Image.open("Images/real_madrid_badge.png")
    real_madrid_img = real_madrid_img.resize((100, 136), 3)
    real_madrid_img = ImageTk.PhotoImage(real_madrid_img)
    real_madrid_button = Button(window, image=real_madrid_img,bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=selectRealMadrid)
    real_madrid_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    manchester_img = Image.open("Images/manchester_team_badge.png")
    manchester_img = manchester_img.resize((100, 136), 3)
    manchester_img = ImageTk.PhotoImage(manchester_img)
    manchester_button = Button(window, image=manchester_img, bg="#085c04", borderless=1, highlightthickness=3, borderwidth=5, relief=RAISED, overbackground="#3f9e3a", activebackground="#3f9e3a", command=selectManchester)
    manchester_button.place(relx=0.8, rely=0.5, anchor=CENTER)

    japan_label = Label(window, text="Samurai Blue", font=font1, bg="black", fg="white")
    japan_label.place(relx=0.2, rely=0.68, anchor=CENTER)

    real_madrid_label = Label(window, text="Real Madrid", font=font1, bg="black", fg="white")
    real_madrid_label.place(relx=0.5, rely=0.68, anchor=CENTER)

    manchester_label = Label(window, text="Manchester United", font=font1, bg="black", fg="white")
    manchester_label.place(relx=0.8, rely=0.68, anchor=CENTER)

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