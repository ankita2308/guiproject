from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import ttk
window=Tk()
window.title('message box')
window.geometry('350x200')
def clicked():
    messagebox.showinfo("message title","message containt")
btn=Button(window,text="click me",command=clicked)
btn.grid(column=0,row=1)

style=ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar",background='yellow')
bar=Progressbar(window,length=200,style='black.Horizontal.TProgressbar')

bar['value']=80
bar.grid(column=1,row=0)





window.mainloop()
