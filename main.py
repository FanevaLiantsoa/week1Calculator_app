from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root)
frm.grid()
display= Entry(frm)
clear_on_next_press = False
def Clic(value):
    #objet = Label(frm, text=display.insert(END, value))
    global clear_on_next_press
    if clear_on_next_press:
        display.delete(0, END)
        clear_on_next_press = False
    #objet.pack()
    valeuractuelle = display.get()
    display.delete(0, END)
    display.insert(0, str(valeuractuelle) + str(value))
    
    display.grid(column=0, row=0, columnspan=3, rowspan=2, sticky="nsew", padx=10, pady=10)

def Suppr():
    display.delete(0, END)

def Add():
    global clear_on_next_press
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="add"
    display.delete(0, END)
def Soustr():
    global clear_on_next_press
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="Soustr"
    display.delete(0, END)
def Mult():
    global clear_on_next_press
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="Mult"
    display.delete(0, END)
def Div():
    global clear_on_next_press
    k=display.get()
    global l
    global condition
    l= int(k)
    condition="Div"
    display.delete(0, END)

def Egal():
    global clear_on_next_press
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
    clear_on_next_press = True

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
for col in range(4):
    frm.columnconfigure(col, weight=1)
for row in range(6):
    frm.rowconfigure(row, weight=1)
frm.grid(row=0, column=0, sticky="nsew")

s = ttk.Style()
s.configure('my1.TButton', font=('Helvetica', 15), foreground='blue')
t = ttk.Style()
t.configure('my2.TButton', font=('Helvetica', 15), foreground='red')
u = ttk.Style()
u.configure('my3.TButton', font=('Helvetica', 15), foreground='green')
v = ttk.Style()
v.configure('my4.TButton', font=('Helvetica', 15), foreground='grey')

ttk.Button(frm, style='my.TButton' , text="=", command=Egal).grid(column=3, row=5, sticky="nsew")
ttk.Button(frm, style='my3.TButton' ,text="+", command=Add).grid(column=3, row=4,sticky="nsew")
ttk.Button(frm, style='my3.TButton' ,text="-", command=Soustr).grid(column=3, row=3,sticky="nsew")
ttk.Button(frm, style='my3.TButton' ,text="*", command=Mult).grid(column=3, row=2,sticky="nsew") 
ttk.Button(frm, style='my3.TButton' ,text="/", command=Div).grid(column=3,row=1,sticky="nsew")
ttk.Button(frm, style='my2.TButton' ,text="Suppr", command=Suppr).grid(column=3, row=0,sticky="nsew")
ttk.Button(frm, style='my.TButton' ,text=".", command=lambda : Clic(".")).grid(column=2, row=5,sticky="nsew")
ttk.Button(frm, style='my1.TButton' ,text="3", command=lambda : Clic("3")).grid(column=2, row=4,sticky="nsew")
ttk.Button(frm, style='my1.TButton' ,text="6", command=lambda : Clic("6")).grid(column=2, row=3,sticky="nsew")
ttk.Button(frm, style='my1.TButton' ,text="9", command=lambda : Clic("9")).grid(column=2, row=2,sticky="nsew")
ttk.Button(frm, style='my.TButton' ,text="sqrt(x)", command=lambda : Clic("sqrt(x)")).grid(column=1, row=5,sticky="nsew")
#ttk.Button(frm, text="_", command=lambda x: Clic("_")).grid(column=2, row=0)
ttk.Button(frm, style='my1.TButton' ,text="0", command=lambda : Clic("0")).grid(column=1, row=5,sticky="nsew")
ttk.Button(frm, style='my1.TButton' ,text="2", command=lambda : Clic("2")).grid(column=1, row=4,sticky="nsew")
ttk.Button(frm, style='my1.TButton'  ,text="5", command=lambda : Clic("5")).grid(column=1, row=3,sticky="nsew")
ttk.Button(frm, style='my1.TButton' ,text="8", command=lambda : Clic("8")).grid(column=1, row=2,sticky="nsew")
#ttk.Button(frm, text="x^2", command=lambda : Clic("x^2")).grid(column=1, row=1,sticky="nsew")
#ttk.Button(frm, text="_", command=lambda x: Clic("_")).grid(column=1, row=0)
ttk.Button(frm, style='my1.TButton' ,text="1", command=lambda : Clic("1")).grid(column=0, row=4,sticky="nsew")
ttk.Button(frm, style='my1.TButton' ,text="4", command=lambda  : Clic("4")).grid(column=0, row=3,sticky="nsew")
ttk.Button(frm, style='my1.TButton' ,text="7", command=lambda : Clic("7")).grid(column=0, row=2,sticky="nsew")
#ttk.Button(frm, text="1/x", command=lambda : Clic("1/x")).grid(column=0, row=1,sticky="nsew")
#ttk.Button(frm, text="_").grid(column=0, row=0)
ttk.Button(frm, style='my.TButton' ,text="Quit", command=root.destroy).grid(column=3, row=6,sticky="nsew")
root.mainloop()

