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

        self.CostumFontMyDebitCard = ('Times New Roman',20)
        self.CostumFontButton = ('Times New Roman',13)

        self.white = '#ffffff'
        self.black = "#000000"

        self.createWidgets()
    def createWidgets(self):
        self.columnconfigure(0, weight=1)
        MyDebitCard = ttk.Label(text="MY DEBIT CARD XXXXXX",font=self.CostumFontMyDebitCard,background=self.white)
        MyDebitCard.grid(column=0, row=0, padx=5, rowspan=1, pady=(70,50))

        ## LEFT SIDE

        BankLabel = ttk.Label(text="BANK: xxxx",font=self.CostumFontButton,background=self.white)
        BankLabel.grid(column=0, row=1, padx=5, pady=(15,0),sticky='w')

        AccountLabel = ttk.Label(text="ACCOUNT: xxx",font=self.CostumFontButton,background=self.white)
        AccountLabel.grid(column=0, row=2, padx=5, pady=(15,0),sticky='w')

        AvailableLabel = ttk.Label(text="AVAILABLE: xxx",font=self.CostumFontButton,background=self.white)
        AvailableLabel.grid(column=0, row=3, padx=5, pady=(15,0),sticky='w')

        IncomeLabel = ttk.Label(text="INCOME LAST MONTH: xxx",font=self.CostumFontButton,background=self.white)
        IncomeLabel.grid(column=0, row=4, padx=5, pady=(15,0),sticky='w')

        SpentLabel = ttk.Label(text="SPENT LAS MONT: xxx",font=self.CostumFontButton,background=self.white)
        SpentLabel.grid(column=0, row=5, padx=5, pady=(15,0),sticky='w')

        SavedLabel = ttk.Label(text="SAVED LAST MONTH: xxx",font=self.CostumFontButton,background=self.white)
        SavedLabel.grid(column=0, row=6, padx=5, pady=(15,0),sticky='w')

        LimitLabel = ttk.Label(text="MONTHLY SPENDING LIMIT: xxx",font=self.CostumFontButton,background=self.white)
        LimitLabel.grid(column=0, row=6, padx=5, pady=(15,0),sticky='w')

        AcceptButton = tk.Button(text='ACCEPT', font=self.CostumFontButton, bg=self.black,fg=self.white,height=2, width=13)
        AcceptButton.grid(column=0, row=7, padx=5, pady=(15,0),sticky='w')

        #RIGHT SIDE
        DateLabel = ttk.Label(text="DATE",font=self.CostumFontButton,background=self.white)
        DateLabel.grid(column=1, row=1, padx=5, pady=(15,0))

        Void = ttk.Label(text="",font=self.CostumFontButton,background=self.white)
        Void.grid(column=1, row=2, padx=5, pady=(15,0))

        IncomeLabel = ttk.Label(text="INCOME",font=self.CostumFontButton,background=self.white)
        IncomeLabel.grid(column=1, row=3, padx=5, pady=(15,0))

        self.entry = ttk.Entry(self)
        self.entry.grid(column=1, row=4, padx=5, pady=(1,0))

        SpentLabel = ttk.Label(text="SPENT",font=self.CostumFontButton,background=self.white)
        SpentLabel.grid(column=1, row=5, padx=5, pady=(15,0))

        self.entry = ttk.Entry(self)
        self.entry.grid(column=1, row=6, padx=5, pady=(1,0))

        NewMslLabel = ttk.Label(text="NEW MSL",font=self.CostumFontButton,background=self.white)
        NewMslLabel.grid(column=1, row=7, padx=5, pady=(15,0))

        self.entry = ttk.Entry(self)
        self.entry.grid(column=1, row=8, padx=5, pady=(1,0))

        

if __name__ == "__main__":
    main = welcome()
    main.mainloop()

