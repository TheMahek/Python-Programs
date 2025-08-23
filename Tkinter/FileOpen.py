from tkinter.filedialog import askopenfile
from tkinter.colorchooser import askcolor
from tkinter import *

root=Tk(className="File Open And Choose Color")

root.geometry("750x500")

def showFile():
    filename=askopenfile()
    print(filename)

def showColor():
    color=askcolor()
    print(color)

btn=Button(root,text="Open File",command=showFile)
btnColor=Button(root,text="Choose Color",command=showColor)

btn.place(x=50,y=50)
btnColor.place(x=50,y=100)

root.mainloop()