from tkinter import *

root = Tk()
root.geometry("300x300")
root.title(" Minute converter ")


def Take_input():
    m = inputtxt.get("1.0", "end-1c")
    m=int(m)
    print(m)
    while  m > 60 and m <= 110:

        rm = m - 60

        print("1" "hour", rm, "minutes")
        Output.insert(END, "1 hour", rm, "minutes")
        break
    else:
        tm = m / 60
        tmd = tm % 1
        tmw = tm // 1
        tmd = tmd * 60
        if tmw > 0:
            print("%.0f" % tmw, "Hours")
            Output.insert(END, "%.0f" % tmw, "Hours")
        if tmd > 0:
            print("%.0f" % tmd, "Minutes")
            Output.insert(END, "%.0f" % tmd, "Minutes")


l = Label(text="Converting Minutes to Hours")
inputtxt = Text(root, height=3,
                width=15,
                bg="light yellow")

Output = Text(root, height=3,
              width=15,
              bg="light cyan")

Display = Button(root,fg="red", height=0,
                 width=10,
                 text="Calculate",
                 command=lambda: Take_input())

l.pack()
inputtxt.pack()

Display.pack()
Output.pack()

mainloop()


