Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("***********  DIGITAL CLOCK  **********")
***********  DIGITAL CLOCK  **********
>>> from tkinter import * #Importing modules
>>> from time import strftime
>>> root = Tk() #Creates tkinter window
>>> root.title("Digital Computer Clock")#Add title to tkinter window
''
>>> def time():    #function used to display time on the Label
	string = strftime("%H:%M:%S %p")
	lbl.config(text=string)
	lbl.after(1000,time)

	
>>> lbl = Label(root,font=('arial',160,'bold'),bg='black',fg='white')
>>> lbl.pack(anchor='center',fill:'both',expand=1)
SyntaxError: invalid syntax
>>> lbl.pack(anchor='center',fill='both',expand=1)
>>> time()
>>> #Styling the label widgets which displays clock # Pack method in tkinter packs into rows or columns.Positions Label #Time function is called # Runs the application program
>>> 