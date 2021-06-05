Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import messagebox
>>> root = Tk()
>>> root.geometry("500x200+500+300")
''
>>> root.title("Square Finder")
''
>>> def sqr():
	try:
		s1 = entNumber.get()
		num = float(s1)
		res = num*num
		messagebox.showinfo("Result","square="+str(res))
	except ValueError:
		messagebox.showerror("Issue","Incorrect Input")
		entNumber.delete(0,END)
		entNumber.focus()

		
>>> lblNumber = Label(root,text="Enter a number")
>>> lblNumber.place(x=10,y=10)
>>> entNumber = Entry(root,bd=5)
>>> entNumber.place(x=100,y=10)
>>> btnSquare = Button(root,text="Square",command=sqr)
>>> btnSquare.place(x=100,y=50)
>>> root.mainloop()
