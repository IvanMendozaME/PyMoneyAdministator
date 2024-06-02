import tkinter as tk
from tkinter import ttk
from tkinter import font

class welcome(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Welcome')   
        self.geometry("600x500")
        self['background'] = '#ffffff'
        self.resizable(0, 0)

        self.CostumFontHelloUser = ('Times New Roman',30)
        self.CostumFontButton = ('Times New Roman',13)

        self.white = '#ffffff'
        self.black = "#000000"

        self.createWidgets()
    def createWidgets(self):
        self.columnconfigure(0, weight=1)
        welcome = ttk.Label(text="MY CARDS",font=self.CostumFontHelloUser,background=self.white)
        welcome.grid(column=0, row=0, padx=5, pady=(70,50))
        Card = 0
        for i in range(3):
            CardButton = Card + 1
            CardButton = tk.Button(text=f'Card {i+1}', font=self.CostumFontButton, bg=self.black,fg=self.white,height=2, width=13)
            CardButton.grid(column=0, row=i+1, padx=5, pady=(15,0))

if __name__ == "__main__":
    main = welcome()
    main.mainloop()

