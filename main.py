from tkinter import *

FONT = ("Arial", 30)

window = Tk()
window.title("Calculator")
window.minsize(width=190, height=200)
window.config(bg="gray")

num1 = []
num2 = []
num = []
operation = ""
operations = ["+", "-", "*", "/"]
total = 0


'''
When one of the operations is clicked, clear() function will be called and would clear the entry screen.
'''
def clear():
    entry.delete("0", END)


'''
Everytime the user clicks C (clear), the all the variables will reset to the initial value.
'''
def click_clear():
    global num
    global num1
    global num2
    global total
    num1 = []
    num2 = []
    num = []
    total = 0

    entry.delete('0', END)


'''
When a user clicks on one of the number buttons using the GUI, that specific 'number' function will be called with the
use of 'command' option from tkinter. 
First, it will check if there are already numbers/operations/decimals in the global num variable, if so, that specific
number will be appended and would update the entry screen in the GUI to show that specific number along with the other
items in the global num. Else, that specific number would just be appended to the global num.
'''
#NUMBER FUNCTIONS
def one():
    global num
    if "." in num:
        num.append("1")
        entry.insert(string="1", index=END)
    else:
        num.append("1")
        entry.insert(string="1", index=END)


def two():
    global num
    if "." in num:
        num.append("2")
        entry.insert(string="2", index=END)
    else:
        num.append("2")
        entry.insert(string="2", index=END)


def three():
    global num
    if "." in num:
        num.append("3")
        entry.insert(string="3", index=END)
    else:
        num.append("3")
        entry.insert(string="3", index=END)


def four():
    global num
    if "." in num:
        num.append("4")
        entry.insert(string="4", index=END)
    else:
        num.append("4")
        entry.insert(string="4", index=END)


def five():
    global num
    if "." in num:
        num.append("5")
        entry.insert(string="5", index=END)
    else:
        num.append("5")
        entry.insert(string="5", index=END)


def six():
    global num
    if "." in num:
        num.append("6")
        entry.insert(string="6", index=END)
    else:
        num.append("6")
        entry.insert(string="6", index=END)


def seven():
    global num
    if "." in num:
        num.append("7")
        entry.insert(string="7", index=END)
    else:
        num.append("7")
        entry.insert(string="7", index=END)


def eight():
    global num
    if "." in num:
        num.append("8")
        entry.insert(string="8", index=END)
    else:
        num.append("8")
        entry.insert(string="8", index=END)


def nine():
    global num
    if "." in num:
        num.append("9")
        entry.insert(string="9", index=END)
    else:
        num.append("9")
        entry.insert(string="9", index=END)


def zero():
    global num
    num.append("0")
    entry.insert(string="0", index=END)


def dot():
    global num
    num.append(".")
    entry.insert(string=".", index=END)


#SETTING UP THE GUI

#Input/Output Entry
entry = Entry(width=11, bg="white", fg="black", highlightthickness=0, font=FONT, justify="right")
entry.grid(column=0, row=0, columnspan=4)


#Number buttons
one_button = Button(text="1", width=5, height=3, highlightthickness=0, fg='black', command=one)
one_button.grid(column=0, row=3)

two_button = Button(text="2", width=5, height=3, highlightthickness=0, fg='black', command=two)
two_button.grid(column=1, row=3)

three_button = Button(text="3", width=5, height=3, highlightthickness=0, fg='black', command=three)
three_button.grid(column=2, row=3)

four_button = Button(text="4", width=5, height=3, highlightthickness=0, fg='black', command=four)
four_button.grid(column=0, row=4)

five_button = Button(text="5", width=5, height=3, highlightthickness=0, fg='black', command=five)
five_button.grid(column=1, row=4)

six_button = Button(text="6", width=5, height=3, highlightthickness=0, fg='black', command=six)
six_button.grid(column=2, row=4)

seven_button = Button(text="7", width=5, height=3, highlightthickness=0, fg='black', command=seven)
seven_button.grid(column=0, row=5)

eight_button = Button(text="8", width=5, height=3, highlightthickness=0, fg='black', command=eight)
eight_button.grid(column=1, row=5)

nine_button = Button(text="9", width=5, height=3, highlightthickness=0, fg='black', command=nine)
nine_button.grid(column=2, row=5)

zero_button = Button(text="0", width=5, height=3, highlightthickness=0, fg='black', command=zero)
zero_button.grid(column=0, row=6)

dot_button = Button(text=".", width=5, height=3, highlightthickness=0, fg='black', command=dot)
dot_button.grid(column=1, row=6)


#Arithmetic Buttons
clear_button = Button(text="C", width=5, height=3, highlightthickness=0, fg='black', command=click_clear)
clear_button.grid(column=2, row=6)

plus_button = Button(text="+", width=5, height=3, highlightthickness=0, fg='black', command="add")
plus_button.grid(column=3, row=3)

minus_button = Button(text="-", width=5, height=3, highlightthickness=0, fg='black', command="subtract")
minus_button.grid(column=3, row=4)

multiply_button = Button(text="x", width=5, height=3, highlightthickness=0, fg='black', command="multiply")
multiply_button.grid(column=3, row=5)

divide_button = Button(text="/", width=5, height=3, highlightthickness=0, fg='black', command="divide")
divide_button.grid(column=3, row=6)

equal_button = Button(text="=", width=21, height=3, highlightthickness=0, fg='black', command="")
equal_button.grid(column=0, row=7, columnspan=4)


window.mainloop()