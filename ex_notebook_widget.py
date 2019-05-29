from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import ttk
window=Tk()
window.title('message box')
window.geometry('350x200')
ttk_notebook=ttk.Notebook(window)
tab1=ttk.Frame(ttk_notebook)
tab2=ttk.Frame(ttk_notebook)

ttk_notebook.add(tab1,text='first')
ttk_notebook.add(tab2,text='second')
ttk_notebook.pack(expand=1,fill='both')
window.mainloop()

