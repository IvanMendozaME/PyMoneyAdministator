import tkinter as tk
from tkinter import ttk
from tkinter import font
import pandas as pd
from HelloUser import Hellouser
from utils import OpenWelcome


class signIn(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SignIn')   
        self.geometry("600x400")
        self['background'] = '#ffffff'
        self.resizable(0, 0)

        self.CostumFontSignIn = ('Times New Roman',30)
        self.CostumFontTasks = ('Times New Roman',9)

        self.white = '#ffffff'
        self.black = "#000000"

        self.createWidgets()
    def createWidgets(self):

        SignInLabel = ttk.Label(text="  SIGN IN",font=self.CostumFontSignIn,background=self.white)
        SignInLabel.grid(column=0, row=0, padx=200, pady=(70,20), columnspan=2)

        MailLabel = ttk.Label(text="Mail:",font=self.CostumFontTasks,background=self.white)
        MailLabel.grid(column=0, row=1, padx=5, pady=20,sticky='e') 

        PswdLabel = ttk.Label(text="Password",font=self.CostumFontTasks,background=self.white)
        PswdLabel.grid(column=0, row=2, padx=5, pady=20,sticky='e')

        #Right side

        self.entryMail = ttk.Entry(self)
        self.entryMail.grid(column=1, row=1, padx=5, pady=(1,0),sticky='w')

        self.entryPswd = ttk.Entry(self,show="*")
        self.entryPswd.grid(column=1, row=2, padx=5, pady=(1,0),sticky='w')

        #Buttons

        BackButton = tk.Button(text='Back', font=self.CostumFontTasks, bg=self.black,fg=self.white, height=2, width=13,command=self.Back)
        BackButton.grid(column=0, row=3, padx=5, pady=(20,0),sticky='e')
        SignUpButton = tk.Button(text='LogIn', font=self.CostumFontTasks, bg=self.black,fg=self.white ,height=2, width=13, command=self.SignIn)
        SignUpButton.grid(column=1, row=3, padx=5, pady=(20,0))

    def SignIn(self):
        df = pd.read_csv('Costumers.csv')
        #Entries values
        MailInput = self.entryMail.get()
        PsswInput = self.entryPswd.get()

        mails = df['Mail'].values
        pswds = df['Password'].values

        #Validate if user and pswd exist
        if MailInput in mails:
            #Showing Mail exist
            print('Mail exist in db')
            #validating pswd
            filteredDf = df[df['Mail'] == MailInput]
            pswdMatched = filteredDf['Password'].iloc[0]
            if pswdMatched == PsswInput:
                print('Correct password')
                self.destroy()
                Hellouser()
            else:
                print('Password Incorrect')

        else:
            print('Mail does not exist')

    def Back(self):
        self.destroy()
        OpenWelcome()


        

if __name__ == "__main__":
    main = signIn()
    main.mainloop()

