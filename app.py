import customtkinter as ctk
from tkinter.colorchooser import askcolor
import pyperclip


def main():
    app = App()
    app.mainloop()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main Window Configuration
        self.title("Color Picker")

    def pick_color(self):
        colors = askcolor(title="Pick Color")
        return colors[1]


if __name__ == "__main__":
    main()
