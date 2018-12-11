from tkinter import *
root = Tk()
root.configure(background='navyblue')

# entry variables
name = StringVar()
percent = StringVar()
backlog = StringVar()
intern = StringVar()
firstround = StringVar()
commskills = StringVar()

# photo
logo = PhotoImage(file="download.png", height=200, width=220)
w1 = Label(root, image=logo).grid(row=0, column=3, columnspan=2)
# Heading
w2 = Label(root, justify=LEFT, text="Nucleus Computers Ltd.", fg="white", bg="navyblue")
w2.config(font=("Elephant", 20))
w2.grid(row=0, column=0, columnspan=2, padx=200)

# labels
nameLb = Label(root, text="Name", fg="white", bg="navyblue")
nameLb.grid(row=1, column=0, pady=10, sticky=W)

percentageLb = Label(root, text="PERCENTAGE", fg="white", bg="navyblue")
percentageLb.grid(row=2, column=0, pady=10, sticky=W)

backlogLb = Label(root, text="BACKLOG", fg="white", bg="navyblue")
backlogLb.grid(row=3, column=0, pady=10, sticky=W)

internLb = Label(root, text="INTERNSHIP", fg="white", bg="navyblue")
internLb.grid(row=4, column=0, pady=10, sticky=W)

frLb = Label(root, text="FIRST ROUND", fg="white", bg="navyblue")
frLb.grid(row=5, column=0, pady=10, sticky=W)


cmskillsLb = Label(root, text="COMMUNICATION SKILLS", fg="white", bg="navyblue")
cmskillsLb.grid(row=6, column=0, pady=10, sticky=W)

resultLb = Label(root, text="RESULT", fg="white", bg="navyblue")
resultLb.grid(row=7, column=0, pady=10)

destreeLb = Label(root, text="DecisionTree", fg="white", bg="navyblue")
destreeLb.grid(row=8, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="RandomForest", fg="white", bg="navyblue")
ranfLb.grid(row=9, column=0, pady=10, sticky=W)

# entries

nameEn = Entry(root, textvariable=name)
nameEn.grid(row=1, column=2)

perEn = Entry(root, textvariable=percent)
perEn.grid(row=2, column=2)

bklEn = Entry(root, textvariable=backlog)
bklEn.grid(row=3, column=2)

intEn = Entry(root, textvariable=intern)
intEn.grid(row=4, column=2)

frEn = Entry(root, textvariable=firstround)
frEn.grid(row=5, column=2)

comsEn = Entry(root, textvariable=commskills)
comsEn.grid(row=6, column=2)
a = float(perEn.get()) * 1000
# print(a)
# functions
def decisiontree():
    if(float(perEn.get()) >= 65 and int(intEn.get()) >= 1 and int(bklEn.get()) <= 2
       and float(frEn.get()) >= 70 and float(comsEn.get()) >= 75 ):
        t1.insert(END, "Hired")
        t2.insert(END, "Hired")
    else:
        t1.insert(END, "Not Hired")
        t2.insert(END, "Not Hired")
        

# buttons

dst = Button(root, text="DecisionTree", command=decisiontree,bg="blue",fg="white")
dst.grid(row=2, column=3)

rnf = Button(root, text="Randomforest", command=decisiontree,bg="blue",fg="white")
rnf.grid(row=3, column=3)

#textfileds
t1 = Text(root, height=1, width=20,bg="navyblue",fg="white")
t1.grid(row=8, column=1)

 
t2 = Text(root, height=1, width=20,bg="navyblue",fg="white")
t2.grid(row=9, column=1)


root.mainloop()
