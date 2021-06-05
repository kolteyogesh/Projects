Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import messagebox
>>> root = Tk()
>>> root.title("Carpenter Requirements")
''
>>> root.geometry("500x300+500+300")
''
>>> need = Label(root,text='Carpenter Needed for!!',font=('arial',18,'bold'))
>>> need.grid(row=0,column=0,columnspan=3)
>>> newfur = IntVar()
>>> newFur = Checkbutton(root,text="New Furniture",variable=newfur,font=('arial',14))
>>> newFur.grid(row=1,column=0,sticky=W)
>>> repfur = IntVar()
>>> repairFur = Checkbutton(root,text="Repair Furniture",variable=repfur,font=('arial',14))
>>> repairFur.grid(row=2,column=0,sticky=W)
>>> modfur = IntVar()
>>> modifyFur = Checkbutton(root,text="Modify Furniture",variable=modfur,font=('arial',14))
>>> modifyFur.grid(row=3,column=0,sticky=W)
>>> def f1():
	msg = ""
	if newfur.get() == 1:
		msg = msg + 'New Furniture'+'\n'
	if repfur.get() == 1:
		msg = msg + 'Repair Furniture'+'\n'
	if modfur.get() == 1:
		msg = msg + 'Modify Furniture'+'\n'
	messagebox.showinfo('Carpenter Needed for',msg)

	
>>> submit = Button(root,text="Submit",font=('arial',18,'bold'),command=f1)
>>> submit.grid(row=4,column=0,columnspan=3)
>>> root.mainloop()
