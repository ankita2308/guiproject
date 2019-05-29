from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("welcome to my class")
window.geometry("350x200")
combo=Combobox(window)
combo['values']=(1,2,3,4,5,'Text')
combo.current(1)#sets the selected item
combo.grid(column=0,row=0)

#to create checkbox
'''chk_state=BooleanVar()#IntVar() o/p is 0 and 1 form
chk_state.set(True)
chk=Checkbutton(window,text='Choose',var=chk_state)
chk.grid(column=0,row=1)
'''
#create radio button
rad1=Radiobutton(window,text='first',value=1)
rad2=Radiobutton(window,text='second',value=2)
rad3=Radiobutton(window,text='third',value=3)
rad1.grid(column=1,row=0)
rad2.grid(column=2,row=0)
rad3.grid(column=3,row=0)



window.mainloop()
