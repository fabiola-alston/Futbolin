from game_assets import *

def settingsRun(root):
    window = Toplevel(root)
    window.title("Settings")
    window.configure(background="black")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    window.geometry(f"{width}x{height}+{round(screen_width / 2) - int(width / 2)}+{round(screen_height / 2) - int(height / 1.8)}")

    def closeGame():
        window.destroy()
        root.destroy()

    def closeWindow():
        selectSound()
        root.deiconify()
        window.destroy()

    def musicOn():
        pygame.mixer.music.set_volume(1)


    def musicOff():
        pygame.mixer.music.set_volume(0)

    title_label = Label(window, text="Music: ", font=font1, bg="black", fg="white")
    title_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    on_button = Button(window, text="On", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=musicOn)
    on_button.place(relx=0.5, rely=0.4, anchor=CENTER)

    off_button = Button(window, text="Off", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=musicOff)
    off_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    back_button = Button(window, text="Back", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=closeWindow)
    back_button.place(relx=0.5, rely=0.85, anchor=CENTER)

    window.protocol("WM_DELETE_WINDOW", closeGame)

    root.mainloop()