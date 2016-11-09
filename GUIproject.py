# Nikolei Advani, 11/8/16
# This program runs a working calculator
import tkinter

root = tkinter.Tk()
root.title("Calculator")


# All of these functions make the buttons work
def click9():
    temp = input.get()
    temp += "9"
    input.set(temp)


def click8():
    eight = input.get()
    eight += "8"
    input.set(eight)


def click7():
    seven = input.get()
    seven += "7"
    input.set(seven)


def click6():
    six = input.get()
    six += "6"
    input.set(six)


def click5():
    five = input.get()
    five += "5"
    input.set(five)


def click4():
    four = input.get()
    four += "4"
    input.set(four)


def click3():
    three = input.get()
    three += "3"
    input.set(three)


def click2():
    two = input.get()
    two += "2"
    input.set(two)


def click1():
    one = input.get()
    one += "1"
    input.set(one)


def clickplus():
    plus = input.get()
    plus += "+"
    input.set(plus)


def clickminus():
    minus = input.get()
    minus += "-"
    input.set(minus)


def clickequals():
    equals = input.get()
    equals = eval(equals)
    input.set(equals)


def clicksign():
    sign = input.get()
    sign = eval(sign) * -1
    input.set(sign)


def clickAC():
    input.set("")


def clickpercent():
    percent = input.get()
    percent = eval(percent) * 0.01
    input.set(percent)


def clickdivide():
    divide = input.get()
    divide += "/"
    input.set(divide)


def clickmultiply():
    multiply = input.get()
    multiply += "*"
    input.set(multiply)


def clickzero():
    zero = input.get()
    zero += "0"
    input.set(zero)


def clickdecimal():
    decimal = input.get()
    decimal += "."
    input.set(decimal)

# The following three lines of code create the entry field of the calculator
input = tkinter.StringVar()
screen = tkinter.Entry(root, textvariable = input)
screen.grid(column=1, row=1, columnspan = 4)
# The following lines of code create and label functioning buttons on the calculator
buttonAC = tkinter.Button(root, text = "AC", command = clickAC)
buttonAC.grid(column = 1, row = 2)

buttonplusminus = tkinter.Button(root, text = "+/-", command = clicksign)
buttonplusminus.grid(column = 2, row = 2)

buttonpercent = tkinter.Button(root, text = "%", command = clickpercent)
buttonpercent.grid(column = 3, row = 2)

buttondivide = tkinter.Button(root, text = "/", command = clickdivide)
buttondivide.grid(column = 4, row = 2)

button7 = tkinter.Button(root, text = "7", command = click7)
button7.grid(column = 1, row = 3)

button8 = tkinter.Button(root, text = "8", command = click8)
button8.grid(column = 2, row = 3)

button9 = tkinter.Button(root, text = "9", command = click9)
button9.grid(column = 3, row = 3)

buttonmultiply = tkinter.Button(root, text = "X", command = clickmultiply)
buttonmultiply.grid(column = 4, row = 3)

button4 = tkinter.Button(root, text = "4", command = click4)
button4.grid(column = 1, row = 4)

button5 = tkinter.Button(root, text = "5", command = click5)
button5.grid(column = 2, row = 4)

button6 = tkinter.Button(root, text = "6", command = click6)
button6.grid(column = 3, row = 4)

buttonsubtract = tkinter.Button(root, text = "-", command = clickminus)
buttonsubtract.grid(column = 4, row = 4)

button1 = tkinter.Button(root, text = "1", command = click1)
button1.grid(column = 1, row = 5)

button2 = tkinter.Button(root, text = "2", command = click2)
button2.grid(column = 2, row = 5)

button3 = tkinter.Button(root, text = "3", command = click3)
button3.grid(column = 3, row = 5)

buttonaddition = tkinter.Button(root, text = "+", command = clickplus)
buttonaddition.grid(column = 4, row = 5)

button0 = tkinter.Button(root, text = "0", command = clickzero)
button0.grid(column = 1, row = 6)

button0 = tkinter.Button(root, text = ".", command = clickdecimal)
button0.grid(column = 3, row = 6)

button0 = tkinter.Button(root, text = "=", command = clickequals)
button0.grid(column = 4, row = 6)


root.mainloop()
