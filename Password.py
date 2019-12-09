from random import randint
import string
import random
import tkinter
from kivy.app import App

import tkinter.messagebox



class Password:

    def __init__(self):
        self.pLength = 0
        self.pNumLetters = 0
        self.pNumNumbers = 0
        self.randomNumbers = []
        self.randomLetters = []
        self.randomSymbol = ""
        self.hasSymbols = "N"
        self.holder = ""
        self.finalPassword = ""
        self.isValid = False

    def randomize_numbers(self):
        for _ in range(self.pNumNumbers):
            value = randint(0, 9)
            self.randomNumbers.append(value)

    def randomize_letters(self):
            for _ in range(self.pNumLetters):
                value = random.choice(string.ascii_letters)
                self.randomLetters.append(value)

    def randomize_symbols(self):
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        self.randomSymbol = random.choice(symbols)

    def combine_contents(self):
        for index in range(len(self.randomLetters)):
            self.holder += (self.randomLetters[index])

        for index in range(len(self.randomNumbers)):
            self.holder += (str(self.randomNumbers[index]))

        if myPassword.hasSymbols == "Y":
            self.holder += self.randomSymbol

    def randomize_final_password(self):
        self.holder = random.sample(self.holder, len(self.holder))
        self.finalPassword = ''.join(self.holder)

    def validation_isdigit(self, question, validation_param):
        while not myPassword.isValid:
            val = input(question)
            if not val.isdigit():
                print("ERROR: input must be a positive number")
            else:
                myPassword.isValid = True
                if validation_param == myPassword.pNumNumbers:
                    myPassword.pNumNumbers = int(val)
                if validation_param == myPassword.pNumLetters:
                    myPassword.pNumLetters = int(val)
                else:  # validation_param == myPassword.pLength:
                    if int(val) < 6:
                        print("ERROR: password length must be greater or equal to 6")
                        myPassword.isValid = False
                    else:
                        myPassword.pLength = int(val)


if __name__ == '__main__':
    top = tkinter.Tk()
    top.title = "test"
    # Code to add widgets will go here...
    msg1 = tkinter.messagebox.showinfo("Say Hello", "Hello World")
    L1 = tkinter.Label(top, text="User Name")
    L1.pack(side=tkinter.LEFT)
    E1 = tkinter.Entry(top, bd=5)
    E1.pack(side=tkinter.RIGHT)
    #TODO add GUI code
    top.mainloop()
    while True:
        print("---------------------------------------")
        print("|Welcome to Random Password Generator!|")
        print("|      (press enter to continue)      |")
        print("---------------------------------------")
        welcomeInput = input()
        if not welcomeInput:
            break
    again = "Y"
    while again == "Y":
        myPassword = Password()
        myPassword.isValid = False
        myPassword.validation_isdigit("How LONG do you want your password to be? ", myPassword.pLength, )
        myPassword.isValid = False
        myPassword.validation_isdigit("How many NUMBERS do you want in your password? ", myPassword.pNumNumbers)
        myPassword.isValid = False
        myPassword.validation_isdigit("How many LETTERS do you want in your password? ", myPassword.pNumLetters)

        myPassword.hasSymbols = input("Do you want to include symbols? [Y]es or [N]o ").upper()
        if myPassword.hasSymbols == "Y":
            myPassword.randomize_symbols()

        myPassword.randomize_numbers()
        myPassword.randomize_letters()
        myPassword.combine_contents()
        myPassword.randomize_final_password()
        print("Your random password is " + myPassword.finalPassword)
        again = input("Do you want to generate another password? [Y]es or [N]o ").upper()


