from tkinter import *
window=Tk()
window.title("welcome to GUI")
#creting an label widget
Lb1=Label(window,text='hello',font=('Arial Bold',20))
Lb1.grid(column=0,row=0)
#setting window size
window.geometry('350x200')
#adding button widget
txt=Entry(window,width=10)
txt.grid(column=1,row=0)

def clicked():
    res='welcome to'+txt.get()
    Lb1.configure(text=res)
btn=Button(window,text='click me',bg='orange',fg='red',command=clicked)
btn.grid(column=1,row=1)
#get input using entry class(Tkinter text box)'''













window.mainloop()
