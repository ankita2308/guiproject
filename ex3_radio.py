from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
window=Tk()
window.title("welcome to my class")
window.geometry("350x200")
selected=IntVar()
rad1=Radiobutton(window,text='first',value=1,variable=selected)
rad2=Radiobutton(window,text='second',value=2,variable=selected)
rad3=Radiobutton(window,text='third',value=3,variable=selected)
def clicked():
    print(selected.get())
btn=Button(window,text='click me',command=clicked)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
btn.grid(column=0,row=1)
txt=scrolledtext.ScrolledText(window,width=30,height=10)#to create scroll

txt.grid(column=0,row=2)
window.mainloop()
