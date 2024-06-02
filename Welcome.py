import tkinter as tk
from tkinter import ttk
from tkinter import font
from utils import OpenSignIn

class welcome(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Welcome')   
        self.geometry("600x400")
        self['background'] = '#ffffff'
        self.resizable(0, 0)

        self.CostumFontWelcome = ('Times New Roman',40)
        self.CostumFontButton = ('Times New Roman',13)

        self.white = '#ffffff'
        self.black = "#000000"

        self.createWidgets()
    def createWidgets(self):
        self.columnconfigure(0, weight=1)
        welcome = ttk.Label(text="WELCOME",font=self.CostumFontWelcome,background=self.white)
        welcome.grid(column=0, row=0, padx=5, pady=70)

        SignInButton = tk.Button(text='SIGN IN', font=self.CostumFontButton, bg=self.black,fg=self.white, height=2, width=13, command=self.SignIn)
        SignInButton.grid(column=0, row=2, padx=5, pady=(0,0))
        SignUpButton = tk.Button(text='SIGN UP', font=self.CostumFontButton, bg=self.black,fg=self.white ,height=2, width=13)
        SignUpButton.grid(column=0, row=3, padx=5, pady=(20,0))
    def SignIn(self):
        self.destroy()
        OpenSignIn()
        


if __name__ == "__main__":
    main = welcome()
    main.mainloop()

