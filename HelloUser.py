import tkinter as tk
from tkinter import ttk
from tkinter import font

class Hellouser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Welcome')   
        self.geometry("600x400")
        self['background'] = '#ffffff'
        self.resizable(0, 0)

        self.CostumFontHelloUser = ('Times New Roman',30)
        self.CostumFontButton = ('Times New Roman',13)

        self.white = '#ffffff'
        self.black = "#000000"

        self.createWidgets()
    def createWidgets(self):
        self.columnconfigure(0, weight=1)
        welcome = ttk.Label(text="HELLO __USER__",font=self.CostumFontHelloUser,background=self.white)
        welcome.grid(column=0, row=0, padx=5, pady=70)

        MyCardsButton = tk.Button(text='MY CARDS', font=self.CostumFontButton, bg=self.black,fg=self.white,height=2, width=13)
        MyCardsButton.grid(column=0, row=2, padx=5, pady=(0,0))
        NewCardsButton = tk.Button(text='NEW CARD', font=self.CostumFontButton, bg=self.black,fg=self.white,height=2, width=13)
        NewCardsButton.grid(column=0, row=3, padx=5, pady=(20,0))

if __name__ == "__main__":
    main = Hellouser()
    main.mainloop()

