from game_assets import *

def aboutRun(root):
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

    label = Label(window, text="About", font=font3, bg="black", fg="white")
    label.place(x=50, y=50)

    label = Label(window, text="Developers", font=font4, bg="black", fg="white")
    label.place(x=50, y=100)

    label = Label(window, text="Tamara Cajiao Molina\n2024143333", font=font2, bg="black", fg="white", justify="left")
    label.place(x=50, y=130)

    label = Label(window, text="Fabiola Alston Ramos\n2024227262", font=font2, bg="black", fg="white", justify="left")
    label.place(x=50, y=180)

    label = Label(window, text="Course:\nFundamentos de Sistemas Computacionales", font=font2, bg="black", fg="white", justify="left")
    label.place(x=50, y=250)

    label = Label(window, text="Major:\nIngeniería en Computadores (CE)", font=font2, bg="black",
                  fg="white", justify="left")
    label.place(x=50, y=300)

    label = Label(window, text="Professor:\nLuis Alonso Barboza Artavia", font=font2, bg="black",
                  fg="white", justify="left")
    label.place(x=50, y=350)

    label = Label(window, text="Production year:\n2024", font=font2, bg="black", fg="white", justify="left")
    label.place(x=50, y=400)

    label = Label(window, text="Production country:\nCosta Rica", font=font2, bg="black",
                  fg="white", justify="left")
    label.place(x=50, y=450)

    label = Label(window, text="Program version: 1.0.0", font=font2, bg="black",
                  fg="white", justify="left")
    label.place(x=50, y=500)

    img = Image.open("Images/devs .jpg")
    img = img.resize((300, 200), 3)
    tk_img = ImageTk.PhotoImage(img)

    label_image = Label(window, image=tk_img)
    label_image.place(x=450, y=50)

    back_button = Button(window, text="Back", font=font1, borderless=1, borderwidth=2, highlightthickness=3,
                         relief="raised",
                         bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000",
                         activebackground="#ff5252", command=closeWindow)
    back_button.place(relx=0.8, rely=0.85, anchor=CENTER)

    window.protocol("WM_DELETE_WINDOW", closeGame)

    root.mainloop()