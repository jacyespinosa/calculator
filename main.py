from tkinter import *

FONT = ("Arial", 30)

window = Tk()
window.title("Calculator")
window.minsize(width=190, height=200)
window.config(bg="gray")


#SETTING UP THE GUI

#Input/Output Entry
entry = Entry(width=11, bg="white", fg="black", highlightthickness=0, font=FONT, justify="right")
entry.grid(column=0, row=0, columnspan=4)


#Number buttons
one_button = Button(text="1", width=5, height=3, highlightthickness=0, fg='black', command="")
one_button.grid(column=0, row=3)

two_button = Button(text="2", width=5, height=3, highlightthickness=0, fg='black', command="")
two_button.grid(column=1, row=3)

three_button = Button(text="3", width=5, height=3, highlightthickness=0, fg='black', command="")
three_button.grid(column=2, row=3)

four_button = Button(text="4", width=5, height=3, highlightthickness=0, fg='black', command="")
four_button.grid(column=0, row=4)

five_button = Button(text="5", width=5, height=3, highlightthickness=0, fg='black', command="")
five_button.grid(column=1, row=4)

six_button = Button(text="6", width=5, height=3, highlightthickness=0, fg='black', command="")
six_button.grid(column=2, row=4)

seven_button = Button(text="7", width=5, height=3, highlightthickness=0, fg='black', command="")
seven_button.grid(column=0, row=5)

eight_button = Button(text="8", width=5, height=3, highlightthickness=0, fg='black', command="")
eight_button.grid(column=1, row=5)

nine_button = Button(text="9", width=5, height=3, highlightthickness=0, fg='black', command="")
nine_button.grid(column=2, row=5)

zero_button = Button(text="0", width=5, height=3, highlightthickness=0, fg='black', command="")
zero_button.grid(column=0, row=6)

dot_button = Button(text=".", width=5, height=3, highlightthickness=0, fg='black', command="")
dot_button.grid(column=1, row=6)


#Arithmetic Buttons
clear_button = Button(text="C", width=5, height=3, highlightthickness=0, fg='black', command="")
clear_button.grid(column=2, row=6)

plus_button = Button(text="+", width=5, height=3, highlightthickness=0, fg='black', command="")
plus_button.grid(column=3, row=3)

minus_button = Button(text="-", width=5, height=3, highlightthickness=0, fg='black', command="")
minus_button.grid(column=3, row=4)

multiply_button = Button(text="x", width=5, height=3, highlightthickness=0, fg='black', command="")
multiply_button.grid(column=3, row=5)

divide_button = Button(text="/", width=5, height=3, highlightthickness=0, fg='black', command="")
divide_button.grid(column=3, row=6)

equal_button = Button(text="=", width=21, height=3, highlightthickness=0, fg='black', command="")
equal_button.grid(column=0, row=7, columnspan=4)


window.mainloop()