Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import Tk
>>> from tkinter import Button
>>> from tkinter import LEFT
>>> root = Tk()
>>> root.title("Date and Time")
''
>>> root.geometry("500x200+500+300")
''
>>> root.resizable(False,False)
''
>>> btnDate = Button(root,text="Date")
>>> btnTime = Button(root,text="Time")
>>> btnDateTime = Button(root,text="DateTime")
>>> btnDate.pack(side=LEFT,padx=20)
>>> btnTime.pack(side=LEFT,padx=20)
>>> btnDateTime.pack(side=LEFT,padx=20)
>>> def f1():
	import datetime
	import tkinter.messagebox
	d = datetime.datetime.now().date()
	tkinter.messagebox.showinfo('Date',str(d))

	
>>> def f2():
	from datetime import datetime
	from tkinter import messagebox
	t = datetime.now().time()
	messagebox.showwarning("Time",str(t))

	
>>> def f3():
	from datetime import datetime
	from tkinter import messagebox
	dt = datetime.now()
	messagebox.showerror("Date n Time",str(dt))

	
>>> btnDate = Button(root,text="Date",command=f1())
>>> btnTime = Button(root,text="Time",command=f2())
>>> btnDateTime = Button(root,text="DateTime",command=f3())
>>> root.mainloop()
>>> 