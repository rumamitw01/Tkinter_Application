from tkinter import *
def calculate():
    result=eval(equ.get())
    equ.set(equ.get()+"=\n"+str(result))

def show(buttonString):
    content=equ.get()
    if content=="0":
        content=""
    equ.set(content+buttonString)

def backspace():
    equ.set(str(equ.get()[:-1]))

def clear():
    equ.set("0")

root=Tk()
root.title("計算器")

equ=StringVar()
equ.set("0")

label=Label(root,textvariable=equ,width=40,height=2,relief="raised",anchor=SE)
clearButton=Button(root,text="C",fg="blue",width=5,command=clear)
btnDEL=Button(root,text="DEL",width=5,command=backspace)
btnR=Button(root,text="%",width=5,command=lambda:show("%"))
btnDiv=Button(root,text="/",width=5,command=lambda:show("/"))
btn7=Button(root,text="7",width=5,command=lambda:show("7"))
btn8=Button(root,text="8",width=5,command=lambda:show("8"))
btn9=Button(root,text="9",width=5,command=lambda:show("9"))
btnM=Button(root,text="*",width=5,command=lambda:show("*"))
btn4=Button(root,text="4",width=5,command=lambda:show("4"))
btn5=Button(root,text="5",width=5,command=lambda:show("5"))
btn6=Button(root,text="6",width=5,command=lambda:show("6"))
btnS=Button(root,text="-",width=5,command=lambda:show("-"))
btn1=Button(root,text="1",width=5,command=lambda:show("1"))
btn2=Button(root,text="2",width=5,command=lambda:show("2"))
btn3=Button(root,text="3",width=5,command=lambda:show("3"))
btnP=Button(root,text="+",width=5,command=lambda:show("+"))
btn0=Button(root,text="0",width=15,command=lambda:show("0"))
btnD=Button(root,text=".",width=5,command=lambda:show("."))
btnE=Button(root,text="=",width=5,bg="yellow",command=lambda:calculate())

label.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
clearButton.grid(row=1,column=0)

btnDEL.grid(row=1,column=1)
btnR.grid(row=1,column=2)
btnDiv.grid(row=1,column=3)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btnM.grid(row=2,column=3)
btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btnS.grid(row=3,column=3)
btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnP.grid(row=4,column=3)
btn0.grid(row=5,column=0,columnspan=2)
btnD.grid(row=5,column=2)
btnE.grid(row=5,column=3)

root.mainloop()