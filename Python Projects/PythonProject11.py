Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import messagebox
>>> root = Tk()
>>> root.title("Yoga Requirements")
''
>>> root.geometry("500x300+500+300")
''
>>> yoga = Label(root,text="Yoga!!",font=('arial',18,'bold'))
>>> yoga.grid(row=0,column=0,columnspan=3)
>>> reason = IntVar()
>>> reason.set(1)
>>> looseweight = Radiobutton(root,text='Loose Weight',variable=reason,value=1,font=('arial',14))
>>> stamina = Radiobutton(root,text='Stamina Building',variable=reason,value=2,font=('arial',14))
>>> looseweight.grid(row=1,column=0)
>>> stamina.grid(row=1,column=1)
>>> def f1():
	if(reason.get() == 1):
		messagebox.showinfo('Reason for Yoga','Loose Weight')
	else:
		messagebox.showinfo('Reason for Yoga','Stamina Building')

		
>>> submit = Button(root,text='Submit',font=('arial',14,'bold'),command=f1)
>>> submit.grid(row=2,column=0,columnspan=3)
>>> root.mainloop()
