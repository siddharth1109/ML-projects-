from tkinter import *

root = Tk()
root.title("Welcome")
root.configure(background='lightblue')

# entry variables
name = StringVar()
date = StringVar()
close = StringVar()

# Heading
w2 = Label(root, text="Stock Prediction", fg="Black", bg="lightblue")
w2.config(font=("Forte", 40))
w2.grid(row=0, column=0, columnspan=2, padx=200)
# photo
logo = PhotoImage(file="pic.png", height=283, width=279)
w1 = Label(root, image=logo, bg="lightblue")
w1.grid(row=0, column=3, columnspan=2, rowspan=3, padx=10)

# heading
lab = Label(root, justify=LEFT, text="                     Enter\n 1- Apple  2- Samsung  3- Maruti",
             fg="Black", bg="lightblue")
lab.config(font=("Bradley Hand ITC", 20))
lab.grid(row=1, column=0, padx=100, columnspan=3)



# labels
dateLb = Label(root, text="Date:", fg="navyblue", bg="lightblue")
dateLb.config(font=("Curlz MT", 20))
dateLb.grid(row=3, column=0, pady=10, sticky=W)

forLb = Button(root, text="Forecast:", fg="black", bg="orange")
forLb.config(font=("Curlz MT", 20))
forLb.grid(row=4, column=0, columnspan=2, pady=20, padx=20)

clsLb = Label(root, text="Close Rate:", fg="navyblue", bg="lightblue")
clsLb.config(font=("Curlz MT", 20))
clsLb.grid(row=5, column=0, pady=10, sticky=W)
 
 
 
# entries
nameEn = Entry(root, textvariable=name)
nameEn.grid(row=2, column=0, padx=20, pady=20, columnspan=2)

dateEn = Entry(root, textvariable=date)
dateEn.grid(row=3, column=1, pady=10, columnspan=2)

closeEn = Entry(root, textvariable=close)
closeEn.grid(row=5, column=1, pady=10, columnspan=2)


root.mainloop()
