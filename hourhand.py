from tkinter import *
from time import strftime

root = Tk()
root.geometry("300x300")
root.title(" Minute converter ")



def time():
    string = strftime("%H:%M:%S %p\n %D")
    label.config(text=string)
    label.after(1000, time)


label = Label( font=("ds-digital", 20), bg="black", fg="red")
label.pack(anchor="ne")


def Take_input():
    m = inputtxt.get("1.0", "end-1c")
    m=int(m)
    print(m)
    while  m > 60 and m <= 110:

        rm = m - 60

        print("1" "hour", rm, "minutes")
        Output.insert(END, "1 hour")
        Output.insert(END, rm)
        Output.insert(END, "minutes")
        break
    else:
        tm = m / 60
        tmd = tm % 1
        tmw = tm // 1
        tmd = tmd * 60
        if tmw > 0:
            print("%.0f" % tmw, "Hours")
            Output.insert(END, "%.0f" % tmw)
            Output.insert(END,  "Hours")
        if tmd > 0:
            print("%.0f" % tmd, "Minutes")
            Output.insert(END, "%.0f" % tmd, "Minutes")
            Output.insert(END,  "Minutes")

def clearToTextInput():
   Output.delete("1.0","end")
   inputtxt.delete("1.0","end")
l = Label(text="Converting Minutes to Hours",bg="black",fg="white")
inputtxt = Text(root, height=3,
                width=15,
                bg="light yellow")

Output = Text(root, height=3,
              width=25,
              bg="light cyan")

Display = Button(root,fg="red", height=0,
                 width=10,
                 text="Calculate",
                 command=lambda: Take_input())
button=Button(root,height=1,width=10, text="Clear",command=clearToTextInput)



l.pack()
inputtxt.pack()
time()
Display.pack()
Output.pack()
button.pack()

mainloop()
