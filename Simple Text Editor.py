from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter.scrolledtext import ScrolledText

def newFile():
    text.delete("1.0",END)
    root.title("Untitled")

def openFile():
    global filename
    filename=askopenfilename()
    if filename=="":
        return
    with open(filename,"r") as fileObj:
        content=fileObj.read()
    text.delete("1.0",END)
    text.insert(END,content)
    root.title(filename)

def saveAsFile():
    global filename
    textContent=text.get("1.0",END)
    filename=asksaveasfilename()
    if filename=="":
        return
    with open(filename,"w") as output:
        output.write(textContent)
        root.title(filename)

filename="Untitled"
root=Tk()
root.title(filename)
root.geometry("300x180")

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open File ...",command=openFile)
filemenu.add_command(label="Save As ...",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)

text=ScrolledText(root,undo=True)
text.pack(fill=BOTH,expand=True)
root.bind("<KP_Enter>",lambda event:text.insert(END,"\n"))

root.mainloop()