import tkinter as tk
import customtkinter as ctk
from tkinter.colorchooser import askcolor

# from tkinter import messagebox, PhotoImage
# import pyperclip
import sys


def main():
    app = MainWindow()
    app.bind("<Escape>", sys.exit)
    app.mainloop()


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main Window Configuration
        self.title("Color Picker")
        self.resizable(False, False)
        self.iconbitmap("icon.ico")

        # Create frames
        self.leftFrame = LeftFrameColumn(self)
        self.midFrame = MidFrameColumn(self, self.pick_color)
        self.rightFrame = RightFrameColumn(self)

    def pick_color(self):
        # reset textfields
        self.midFrame.hexEntry.delete(0, tk.END)
        self.midFrame.rgbEntry.delete(0, tk.END)

        # open color dialog
        colors = askcolor(title="Pick Color")

        # update textfields with the new color
        self.midFrame.hexEntry.insert(0, colors[1])
        self.midFrame.rgbEntry.insert(0, colors[0])

        # add color to palette
        self.rightFrame.paletteBox.insert(tk.END, str(colors[1]))
        self.rightFrame.paletteBox.itemconfig(tk.END, {"bg": colors[1]})

        # copy to clipboard
        self.clipboard_append
        self.clipboard_append(str(colors[1]))


class LeftFrameColumn(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Left Column Frame
        self.grid(row=0, column=0, sticky="n", pady=5, padx=5)
        ctk.CTkLabel(self, text="Saved Palettes").grid(row=0, pady=5, padx=5)
        self.presetBox = tk.Listbox(self, bg="#222222")
        self.presetBox.grid(row=1, pady=5, padx=5)


class MidFrameColumn(ctk.CTkFrame):
    def __init__(self, master, pick_color_callback):
        super().__init__(master)

        # Middle Column Frame
        self.grid(row=0, column=1, sticky="n", pady=5, padx=5)

        # Button
        self.pickColorBtn = ctk.CTkButton(
            self, text="Pick Color", command=pick_color_callback
        )
        self.pickColorBtn.grid(row=0, columnspan=2, pady=10, padx=5)

        # Textfields HEX and RGB
        ctk.CTkLabel(self, text="HEX:").grid(row=1, columnspan=2, padx=5)
        self.hexEntry = ctk.CTkEntry(self)
        self.hexEntry.grid(row=2, columnspan=2, pady=5, padx=5)

        ctk.CTkLabel(self, text="RGB:").grid(row=3, columnspan=2, padx=5)
        self.rgbEntry = ctk.CTkEntry(self)
        self.rgbEntry.grid(row=4, columnspan=2, pady=5, padx=5)

        self.checkClipBoard = ctk.CTkCheckBox(self, text="Auto copy to clipboard")
        self.checkClipBoard.grid(row=5, columnspan=2, pady=5, padx=5)
        self.checkClipBoard.select()  # Make a config so the user can turn this off as default

        self.selectedRadio = tk.StringVar()
        self.hexRadio = ctk.CTkRadioButton(
            self, text="HEX", value="hex", variable=self.selectedRadio
        )
        self.hexRadio.grid(row=6, column=0, pady=5, padx=5)
        self.hexRadio.select()  # Make a config so the user can change this as default

        self.rgbRadio = ctk.CTkRadioButton(
            self, text="RGB", value="rgb", variable=self.selectedRadio
        )
        self.rgbRadio.grid(row=6, column=1, pady=5, padx=5)


class RightFrameColumn(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Right Column Frame
        self.grid(row=0, column=2, pady=5, padx=5)

        ctk.CTkLabel(self, text="Current Palette").grid(row=0, pady=5, padx=5)
        self.paletteBox = tk.Listbox(self, bg="#222222", fg="#dedede")
        self.paletteBox.grid(row=1, pady=5, padx=5)
        self.paletteBox.insert(tk.END, " ")

        # Save palette Entry and Button
        self.paletteEntryName = ctk.CTkEntry(self, placeholder_text="Palette name ...")
        self.paletteEntryName.grid(row=2, pady=5, padx=5)

        self.savePaletteBtn = ctk.CTkButton(self, text="Save")
        self.savePaletteBtn.grid(row=3, pady=5, padx=5)

        self.clearPaletteBtn = ctk.CTkButton(
            self, text="Clear", fg_color="#e02c2c", hover_color="#ff4848"
        )
        self.clearPaletteBtn.grid(row=4, pady=5, padx=5)


if __name__ == "__main__":
    main()
