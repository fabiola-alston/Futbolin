from tkinter import *

def teamSelectRun(root):
    window = Toplevel(root)
    window.title("Select Team")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 800
    height = 600
    window.geometry(f"{width}x{height}+{round(screen_width / 2) - int(width / 2)}+{round(screen_height / 2) - int(height / 1.8)}")

    def close():
        root.deiconify()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", close)

    root.mainloop()