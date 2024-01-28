from tkinter import *

def button_press(num):
    global  equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global  equation_text
    try:
      total = str(eval(equation_text))
      equation_label.set(total)
      equation_text= total

    except SyntaxError :
        equation_label.set("Invalid equation")
        equation_text =""

    except ZeroDivisionError :
        equation_label.set("Not defined")
        equation_text=""

def clear():
    global equation_text
    equation_label.set("")
    equation_text= ""

window = Tk()
window.title("CALCULATOR")
window.geometry("450x450")  # for size of GUI
window.config(bg="#F2F1EB")
equation_text = ""

equation_label = StringVar()

icon = PhotoImage(file='calculator-tool.png')
window.iconphoto(True,icon)

label = Label(window, textvariable=equation_label, font=('Consolas', 20), bg="white",
              width=20, height=2)
label.pack()

frame = Frame(window)
frame.config(bg="#EEE7DA")
frame.pack()

button1 = Button(frame, text=1, height=2 , width=6, font=35,
                 command=lambda: button_press(1))

button1.grid(row=0, column=0)


button2 = Button(frame, text=2, height=2 , width=6, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)


button3 = Button(frame, text=3, height=2 , width=6, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=2 , width=6, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=2 , width=6, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=2 , width=6, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=2 , width=6, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=2 , width=6, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=2 , width=6, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=2 , width=6, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=2 , width=6, font=35,
                 command=lambda: button_press('+'),bg="#EEE7DA")
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=2 , width=6, font=35,
                 command=lambda: button_press('-'),bg="#EEE7DA")
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=2 , width=6, font=35,
                 command=lambda: button_press('*'),bg="#EEE7DA")
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=2 , width=6, font=35,
                 command=lambda: button_press('/'),bg="#EEE7DA")
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=2 , width=6, font=35,
                 command=equals,bg="#EEE7DA")
equal.grid(row=4, column=2)

decimal = Button(frame, text='.', height=2 , width=6, font=35,
                 command=lambda: button_press('.'),bg="#EEE7DA")
decimal.grid(row=3, column=1)

Modulous = Button(frame, text='MOD', height=2 , width=6, font=35,
                 command=lambda: button_press('%'),bg="#EEE7DA")
Modulous.grid(row=4, column=3)

clear = Button(frame, text='C', height=2 , width=6, font=35,
                 command= clear,bg="#EEE7DA")
clear.grid(row=4,column=0)

button00 = Button(frame, text='00', height=2 , width=6, font=35,
                 command=lambda: button_press('00'))
button00.grid(row=3, column=2)




window.mainloop()
