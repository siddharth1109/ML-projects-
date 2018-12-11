import sqlite3 as sq
from tkinter import *

# function
class app:
    def __init__(self):
        self.conn = sq.connect("books.db")
        self.cursor = self.conn.cursor()
        self.id_selected = 0
        
        
    def connect(self):
        self.cursor.execute("""CREATE TABLE if not exists books(id INTEGER PRIMARY KEY,
        title text, 
        author text, year INTEGER,isbn INTEGER )""")
        self.conn.commit()
        
    def insert(self):
        t1.delete(0, END)
        title = v1.get().strip()
        author = v2.get().strip()
        years = v3.get()
        isbn = v4.get()


        newbook = (None, title, author, years, isbn)
        self.cursor.execute("INSERT INTO books VALUES(?,?,?,?,?)", newbook)
        self.conn.commit()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        self.view()
        
    def update(self):
       t1.delete(0, END)
       title = v1.get().strip()
       author = v2.get().strip()
       years = v3.get()
       isbn = v4.get()
        

       self.cursor.execute("update books set title=?,author=?\
                        ,years=?,isbn =? where id=?",
                        (title, author, years, isbn, self.id_selected))
       self.conn.commit()
       self.view()
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       t1.delete(0, END) 
       
    def delete(self):
        self.cursor.execute("delete from books where id=?", (self.id_selected,))
        self.conn.commit()
        self.view()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        t1.delete(0, END) 
#         self.conn.close()
       
    def search(self):
        title = e1.get().strip()
        author = e2.get().strip()
        years = e3.get()
        isbn = e4.get()
        
        if title == "":
            tite = None
        if author == "":
            author = None
        if years == 0:
            years = None
        if isbn == 0:
            isbn = None
        
        self.cursor.execute("Select * from books where id = ? or title=? or author = ? or \
                            years=? or isbn=?", (None, title, author, years, isbn))
        
        rows = self.cursor.fetchall()
        t1.delete(0, END)
        if rows != []:
            for row in rows:
                t1.insert(END, row)
        else:
            t1.insert(END, "Not found")
                
        
        
        
    def view(self):
        self.cursor.execute("Select * from books; ")
        rows = self.cursor.fetchall()
        t1.delete(0, END)
        for row in rows:
            t1.insert(END, row)
        

    def close(self):
        self.conn.close()

    
    def clear(self):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)


    def get_selected_row(self,event):
        index = t1.curselection()[0]
        selected_tuple = t1.get(index)
        self.id_selected = selected_tuple[0]
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])      
    
    
bookdata = app()



root = Tk()
root.configure(bg="pink")
bookdata.connect()
# labels
titleLb = Label(root, text="Title",bg = "pink",fg = "white")
titleLb.grid(row=0, column=0, padx=20)

authorLb = Label(root, text="Author",bg = "pink",fg = "white")
authorLb.grid(row=0, column=2, padx=20)

yearLb = Label(root, text="Year",bg = "pink",fg = "white")
yearLb.grid(row=1, column=0, padx=20)

isbnLb = Label(root, text="ISBN",bg = "pink",fg = "white")
isbnLb.grid(row=1, column=2, padx=20)

# entry
v1 = StringVar(root, value=" ")
v2 = StringVar(root, value=" ")
v3 = IntVar(root, value=0)
v4 = IntVar(root, value=0)

e1 = Entry(root, textvariable=v1,bg = "lightblue",fg = "white")
e2 = Entry(root, textvariable=v2,bg = "lightblue",fg = "white")
e3 = Entry(root, textvariable=v3,bg = "lightblue",fg = "white")
e4 = Entry(root, textvariable=v4,bg = "lightblue",fg = "white")
e1.grid(row=0, column=1)
e2.grid(row=0, column=3)
e3.grid(row=1, column=1)
e4.grid(row=1, column=3)

# listox

t1 = Listbox(root, height=12,bg = "lightblue", width=60)
t1.bind('<<ListboxSelect>>', bookdata.get_selected_row)

t1.grid(row=2, column=0, columnspan=4, rowspan=5)

# scrollbar
vsb = Scrollbar(orient="vertical", command=t1.yview,bg = "pink")
t1.configure(yscrollcommand=vsb.set)
vsb.grid(row=2, column=5, sticky=N + S, rowspan=5)

# buttons
b1 = Button(root,bg = "pink",fg = "white", text="View all", height=2, width=20, command=bookdata.view)
b2 = Button(root,bg = "pink",fg = "white", text="Search entry", height=2, width=20, command=bookdata.search)
b3 = Button(root,bg = "pink",fg = "white", text="Add entry", height=2, width=20, command=bookdata.insert)
b4 = Button(root,bg = "pink",fg = "white", text="Update selected", height=2, width=20, command=bookdata.update)
b5 = Button(root,bg = "pink",fg = "white", text="Delete selected", height=2, width=20, command=bookdata.delete)
b6 = Button(root,bg = "pink",fg = "white", text="clear", height=2, width=20, command=bookdata.clear)
b1.grid(row=2, column=6)
b2.grid(row=3, column=6)
b3.grid(row=4, column=6)
b4.grid(row=5, column=6)
b5.grid(row=6, column=6)
b6.grid(row=0, column=6)


root.mainloop()
