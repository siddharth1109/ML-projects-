from tkinter import *


root = Tk()
root.title("Welcome")
# entry variables 
year = StringVar()
month = StringVar()
day = StringVar()
hour = StringVar()
pm = StringVar()
dew = StringVar()
temp = StringVar()
pres = StringVar()
wdir = StringVar()
wspd = StringVar()

# background photo 


# pick a .gif image file you have in the working directory
image1 = PhotoImage(file="giphy.gif")
# w = image1.width()
# h = image1.height()
# 
# root.geometry("%dx%d+0+0" % (w, h))

# tk.Frame has no image argument
# so use a label as a panel/frame
panel1 = Label(root, image=image1)
panel1.place(x=0, y=0, relwidth=1, relheight=1)
# panel1.grid(row=0, column=1,columnspan = 3,sticky = N+W)



# Heading
w2 = Label(root, justify=LEFT, text="For how many hours will it rain today")
w2.config(font=("Elephant", 32))
w2.grid(row=0, column=0, columnspan=2, padx=150, pady=50)

# lables
yearlb = Label(root, text="YEAR", fg="white", bg="navyblue")
yearlb.grid(row=1, column=0, pady=10, sticky=W)

monthlb = Label(root, text="MONTH", fg="white", bg="navyblue")
monthlb.grid(row=2, column=0, pady=10, sticky=W)

daylb = Label(root, text="DAY", fg="white", bg="navyblue")
daylb.grid(row=3, column=0, pady=10, sticky=W)

hourlb = Label(root, text="HOUR", fg="white", bg="navyblue")
hourlb.grid(row=4, column=0, pady=10, sticky=W)

pmlb = Label(root, text="PM 2.5", fg="white", bg="navyblue")
pmlb.grid(row=5, column=0, pady=10, sticky=W)


dewlb = Label(root, text="DEW POINT", fg="white", bg="navyblue")
dewlb.grid(row=6, column=0, pady=10, sticky=W)

templb = Label(root, text="TEMPERATURE", fg="white", bg="navyblue")
templb.grid(row=7, column=0, pady=10, sticky=W)

preslb = Label(root, text="PRESSURE", fg="white", bg="navyblue")
preslb.grid(row=8, column=0, pady=10, sticky=W)

wdirlb = Label(root, text="WIND DIRECTION", fg="white", bg="navyblue")
wdirlb.grid(row=9, column=0, pady=10, sticky=W)

wspdlb = Label(root, text="WINDSPEED", fg="white", bg="navyblue")
wspdlb.grid(row=10, column=0, pady=10, sticky=W)

hrainlb = Label(root, text="HOURS OF RAIN ", fg="white", bg="navyblue")
hrainlb.grid(row=11, column=0, pady=10, sticky=W)

hsnowlb = Label(root, text="HOURS OF SNOW", fg="white", bg="navyblue")
hsnowlb.grid(row=12, column=0, pady=10, sticky=W)

# enteries

yearEn = Entry(root, textvariable=year)
yearEn.grid(row=1, column=2)

monthEn = Entry(root, textvariable=month)
monthEn.grid(row=2, column=2)

dayEn = Entry(root, textvariable=day)
dayEn.grid(row=3, column=2)

hourEn = Entry(root, textvariable=hour)
hourEn.grid(row=4, column=2)

pmEn = Entry(root, textvariable=pm)
pmEn.grid(row=5, column=2)

dewEn = Entry(root, textvariable=dew)
dewEn.grid(row=6, column=2)

tempEn = Entry(root, textvariable=temp)
tempEn.grid(row=7, column=2)

presEN = Entry(root, textvariable=pres)
presEN.grid(row=8, column=2)

wdirEn = Entry(root, textvariable=wdir)
wdirEn.grid(row=9, column=2)

WspdEn = Entry(root, textvariable=wspd)
WspdEn.grid(row=10, column=2)

# function
def calc():
    pass

# buttons
cal = Button(root, text="    Go for it!     ", command=calc, bg="white", fg="red")
cal.grid(row=5, column=3, padx=20, rowspan=2)
cal.config(font=("Elephant", 12))


# textfileds
t1 = Text(root, height=1, width=20, bg="white", fg="red")
t1.grid(row=11, column=1)

 
t2 = Text(root, height=1, width=20, bg="white", fg="red")
t2.grid(row=12, column=1)


root.mainloop()
