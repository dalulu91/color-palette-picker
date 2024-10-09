import tkinter as tk
import customtkinter as ctk
from tkinter.colorchooser import askcolor
import pyperclip
import sys


def main():
    app = App()
    app.bind("<Escape>", sys.exit)
    app.mainloop()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main Window Configuration
        self.title("Color Picker")

        # Left Column Frame
        self.col1 = ctk.CTkFrame(self)
        self.col1.grid(row=0, column=0, sticky="n", pady=5, padx=5)

        ctk.CTkLabel(self.col1, text="Saved Palettes").grid(row=0, pady=5, padx=5)

        self.presetBox = tk.Listbox(self.col1, bg="#222222")
        self.presetBox.grid(row=1, pady=5, padx=5)

        # Middle Column Frame
        self.midFrame = ctk.CTkFrame(self)
        self.midFrame.grid(row=0, column=1, sticky="n", pady=5, padx=5)

        # Button
        self.pickColorBtn = ctk.CTkButton(
            self.midFrame, text="Pick Color", command=self.pick_color
        )
        self.pickColorBtn.grid(row=0, columnspan=2, pady=10, padx=5)

        # Textfields HEX and RGB
        ctk.CTkLabel(self.midFrame, text="HEX:").grid(row=1, columnspan=2, padx=5)
        self.hexEntry = ctk.CTkEntry(self.midFrame)
        self.hexEntry.grid(row=2, columnspan=2, pady=5, padx=5)

        ctk.CTkLabel(self.midFrame, text="RGB:").grid(row=3, columnspan=2, padx=5)
        self.rgbEntry = ctk.CTkEntry(self.midFrame)
        self.rgbEntry.grid(row=4, columnspan=2, pady=5, padx=5)

        self.checkClipBoard = ctk.CTkCheckBox(
            self.midFrame, text="Auto copy to clipboard"
        )
        self.checkClipBoard.grid(row=5, columnspan=2, pady=5, padx=5)
        self.checkClipBoard.select()  # Make a config so the user can turn this off as default

        self.selectedRadio = tk.StringVar()
        self.hexRadio = ctk.CTkRadioButton(
            self.midFrame, text="HEX", value="hex", variable=self.selectedRadio
        )
        self.hexRadio.grid(row=6, column=0, pady=5, padx=5)
        self.hexRadio.select()  # Make a config so the user can change this as default

        self.rgbRadio = ctk.CTkRadioButton(
            self.midFrame, text="RGB", value="rgb", variable=self.selectedRadio
        )
        self.rgbRadio.grid(row=6, column=1, pady=5, padx=5)

        # Right Column Frame
        self.rightFrame = ctk.CTkFrame(self)
        self.rightFrame.grid(row=0, column=2, pady=5, padx=5)

        ctk.CTkLabel(self.rightFrame, text="Current Palette").grid(
            row=0, pady=5, padx=5
        )
        self.paletteBox = tk.Listbox(self.rightFrame, bg="#222222", fg="#dedede")
        self.paletteBox.grid(row=1, pady=5, padx=5)
        self.paletteBox.insert(tk.END, " ")

        # Save palette Entry and Button
        self.paletteEntryName = ctk.CTkEntry(
            self.rightFrame, placeholder_text="Palette name ..."
        )
        self.paletteEntryName.grid(row=2, pady=5, padx=5)

        self.savePaletteBtn = ctk.CTkButton(self.rightFrame, text="Save")
        self.savePaletteBtn.grid(row=3, pady=5, padx=5)

        self.clearPaletteBtn = ctk.CTkButton(
            self.rightFrame, text="Clear", fg_color="#e02c2c", hover_color="#ff4848"
        )
        self.clearPaletteBtn.grid(row=4, pady=5, padx=5)

    def pick_color(self):
        # reset textfields
        self.hexEntry.delete(0, tk.END)
        self.rgbEntry.delete(0, tk.END)

        # open color dialog
        colors = askcolor(title="Pick Color")

        # update textfields with the new color
        self.hexEntry.insert(0, colors[1])
        self.rgbEntry.insert(0, colors[0])

        # add color to palette
        self.paletteBox.insert(tk.END, colors[1])
        self.paletteBox.itemconfig(tk.END, {"bg": colors[1]})


if __name__ == "__main__":
    main()
