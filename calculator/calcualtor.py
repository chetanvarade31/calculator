
from tkinter import *
from PIL import ImageTk, Image 

win = Tk()

eqn = "" 

def btn_click(item):
    global eqn
    
    eqn = eqn + str(item)
    var1.set(eqn)  
    

def btn_clear():
    global eqn
    eqn = ""
    
    var1.set("")  

def back():
    
    x = entery1.get()
    y = len(x)
    global v
    v = y - 1
    
    x = entery1.delete(v)
    global eqn
    
    k = entery1.get()
    eqn = k
     
def btn_equal():
    try : 

        global eqn

        eqn = eval(str(eqn))
        eqn = str(eqn)
        var1.set(eqn)
        #eqn = ""
        
    except SyntaxError as s:

        print("invalid")

eqn = ""    

win.geometry("365x482")
win.maxsize(365, 482)

win.title("CALCULATOR")


var1 = StringVar()

IMG = Image.open("pk.png")

photo = ImageTk.PhotoImage(IMG)

canava = Canvas(win, width= 365 ,height= 482)
canava.create_image(0,0,image = photo)



entery1 = Entry(win, width= 17,font = ("Helvetica",23,"bold"),bg= "LightPink1",fg= 'black',textvariable= var1,bd= "8",highlightcolor= "maroon2",highlightthickness= 4)
entery1.place(x= 24,y = 20)


clear_button = Button(win, text= "c",font = ("Helvetica"),bg= "LightPink1",height= 2,width= 9,fg= "black",bd= "6",cursor="hand2",command= lambda :btn_clear())
clear_button = clear_button.place(x= 20,y= 97)

del_button = Button(win, text= " DEL ",font = ("Helvetica"),bg= "LightPink1",height= 2,width= 8,fg= "black",bd= "6",cursor= "hand2",command= lambda : back())
del_button.place(x = 147, y= 97)

division_btn = Button(win,text= "/",font = ("Helvetica"),bg= "LightPink1",fg= "black",height= "2",width=6,bd= "6",cursor= "hand2",command= lambda :btn_click("/"))
division_btn = division_btn.place(x= 262,y=97)

one = Button(win, text= "1",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height=2,width=5,cursor= "hand2",command= lambda : btn_click(1))
one = one.place(x=20,y = 175)

two = Button(win,text= "2",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height=2, width= 5,cursor= "hand2",command= lambda : btn_click(2))
two = two.place(x=101 ,y= 175)

three = Button(win, text= "3",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height= 2,width= 5,cursor="hand2",command= lambda : btn_click(3))
three = three.place(x= 182, y= 175)


multiplication = Button(win, text= "*",font=("Helvetica"),bg= "LightPink1",fg= "black",bd="6",height= 2,width=6,cursor= "hand2",command= lambda : btn_click("*"))
multiplication = multiplication.place(x= 262,y = 175)

four = Button(win,text= "4",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height= 2,width= 5,cursor="hand2",command= lambda : btn_click(4))
four = four.place(x = 20, y =250 )

five = Button(win,text= "5",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height= 2 ,width= 5,cursor="hand2",command= lambda : btn_click(5))
five = five.place(x = 101,y= 250)

six = Button(win,text= "6",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height= 2,width= 5,cursor="hand2",command= lambda : btn_click(6))
six = six.place(x = 182, y= 250)

plus = Button(win, text= "+",font=("Helvetica"),bg= "LightPink1",fg = "black",bd= "6",height= 2,width=6,cursor="hand2",command= lambda : btn_click("+"))
plus = plus.place(x=262, y= 250)

seven  = Button(win, text= "7",font=("Helvetica"),bg = "maroon2",fg="black",bd= "6",height= 2,width= 5,cursor="hand2",command= lambda : btn_click(7))
seven = seven.place(x= 20 ,y = 325)

eight = Button(win,text= "8",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height= 2 ,width= 5,cursor="hand2",command= lambda : btn_click(8))
eight = eight.place(x = 101 , y = 325)

nine = Button(win, text= "9",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height= 2,width= 5,cursor="hand2",command= lambda :btn_click(9))
nine = nine.place(x = 182, y = 325)

minus = Button(win, text= "-",font=("Helvetica"),bg= "LightPink1",fg= "black",bd= "6",height= 2,width= 6,command= lambda : btn_click("-"))
minus = minus.place(x = 262,y = 325)

zero = Button(win, text= "0",font=("Helvetica"),bg= "maroon2",fg= "black",bd= "6",height= 2 ,width= 9,cursor="hand2",command= lambda : btn_click(0))
zero = zero.place(x = 20 ,y = 403)

dot = Button(win, text= ".",font=("Helvetica"),bg= "LightPink1",fg= "black",bd= "6",height= 2,width= 8,cursor="hand2",command= lambda : btn_click("."))
dot = dot.place(x =147, y= 403 )

equal = Button(win, text= "=",font=("Helvetica"),bg= "LightPink1",fg= "black",bd= "6",height= 2,width= 6,cursor="hand2",command= lambda : btn_equal())
equal = equal.place(x = 262 , y = 403)


canava.pack()
win.mainloop()