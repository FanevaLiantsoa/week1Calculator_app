from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
display= Entry(frm)

def Clic(value):
    #objet = Label(frm, text=display.insert(END, value))
    
    #objet.pack()
    valeuractuelle = display.get()
    display.delete(0, END)
    display.insert(0, str(valeuractuelle) + str(value))
    
    display.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=10, pady=10)

def Suppr():
    display.delete(0, END)

def Add():
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="add"
    display.delete(0, END)
def Soustr():
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="Soustr"
    display.delete(0, END)
def Mult():
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="Mult"
    display.delete(0, END)
def Div():
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="Div"
    display.delete(0, END)

def Egal():
    m=display.get()
    display.delete(0, END)
    if  condition == "add":
            display.insert(0, l + int(m))
    elif condition == "Soustr":           
            display.insert(0, l - int(m))
    elif condition == "Mult":        
            display.insert(0, l * int(m))
    elif condition == "Div":
            display.insert(0, l / int(m))
    





ttk.Button(frm, text="=", command=Egal).grid(column=3, row=5)
ttk.Button(frm, text="+", command=Add).grid(column=3, row=4)
ttk.Button(frm, text="-", command=Soustr).grid(column=3, row=3)
ttk.Button(frm, text="*", command=Mult).grid(column=3, row=2) 
ttk.Button(frm, text="/", command=Div).grid(column=3,row=1)
ttk.Button(frm, text="Suppr", command=Suppr).grid(column=3, row=0)
ttk.Button(frm, text=".", command=lambda : Clic(".")).grid(column=2, row=5)
ttk.Button(frm, text="3", command=lambda : Clic("3")).grid(column=2, row=4)
ttk.Button(frm, text="6", command=lambda : Clic("6")).grid(column=2, row=3)
ttk.Button(frm, text="9", command=lambda : Clic("9")).grid(column=2, row=2)
ttk.Button(frm, text="sqrt(x)", command=lambda : Clic("sqrt(x)")).grid(column=2, row=1)
#ttk.Button(frm, text="_", command=lambda x: Clic("_")).grid(column=2, row=0)
ttk.Button(frm, text="0", command=lambda : Clic("0")).grid(column=1, row=1)
ttk.Button(frm, text="2", command=lambda : Clic("2")).grid(column=1, row=4)
ttk.Button(frm, text="5", command=lambda : Clic("5")).grid(column=1, row=3)
ttk.Button(frm, text="8", command=lambda : Clic("8")).grid(column=1, row=2)
ttk.Button(frm, text="x^2", command=lambda : Clic("x^2")).grid(column=1, row=1)
#ttk.Button(frm, text="_", command=lambda x: Clic("_")).grid(column=1, row=0)
ttk.Button(frm, text="1", command=lambda : Clic("1")).grid(column=0, row=4)
ttk.Button(frm, text="4", command=lambda  : Clic("4")).grid(column=0, row=3)
ttk.Button(frm, text="7", command=lambda : Clic("7")).grid(column=0, row=2)
ttk.Button(frm, text="1/x", command=lambda : Clic("1/x")).grid(column=0, row=1)
#ttk.Button(frm, text="_").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=6)
root.mainloop()

