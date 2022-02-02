from tkinter import*
from math import *
import matplotlib.pyplot as plt
import numpy as np

global D,t,graf
D=-1
t="Нет решений!"
graf=False
def lahend():
    global D,t,graf
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        if (float(a.get())==0 and float(b.get())==0 and float(c.get())==0):
            vastus.configure(text=f"Тут не можеть быть 0")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
        elif float(a.get())==0 and float(b.get())!=0 and float(c.get())!=0:
            vastus.configure(text=f"Тут не можеть быть 0")
            a.configure(bg="red")
            graf=False
        else:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f"X1={x1_}, \nX2={x2_}"
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"X1={x1_}"
                graf=True
            else:
                t="Корней нет"
                graf=False
            btn1.configure(text=f"D={D}\n{t}")
            a.configure(bg="lightblue")
            b.configure(bg="lightblue")
            c.configure(bg="lightblue")   
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
        else:
            a.configure(bg="lightblue")
            b.configure(bg="lightblue")
            c.configure(bg="lightblue")
        graf=False
    return graf,D,t

t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn2.config(text="Уменшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn2.config(text="Увеличить окно")
        t=0


def graafik():
    graf,D,t=lahend()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x1 = np.arange(x0-10, x0+10, 0.5)
        y1=a_*x1*x1+b_*x1+c_
        fig = plt.figure()
        plt.plot(x1, y1,'r-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    btn1.configure(text=f"D={D}\n{t}\n{text}")



def kala():
    x1=np.arange(0, 9.5, 0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9, -2.5, 0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3, 9.5, 0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/9)*(x6-7)**2+1.5
    x7=np.arange(-13, -8.5, 0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Кит")
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def prillid():
    x1=np.arange(-9,-1.5,0.5)
    y1=-(1/16)*(x1+5)**2+2
    x2=np.arange(1,9.5,0.5)
    y2=-(1/16)*(x2-5)**2+2
    x3=np.arange(-9,-1.5,0.5)
    y3=(1/4)*(x3+5)**2-3
    x4=np.arange(1,9.5,0.5)
    y4=(1/4)*(x4-5)**2-3
    x5=np.arange(-9,-6.5,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9.5,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1.5,0.5)
    y7=-(0.5)*x7**2+1.5
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("Очки")
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()


def vihmavari():
    x1=np.arange(-12,12.5,0.5)
    y1=-(1/18)*x1**2+12
    x2=np.arange(-4,4.5,0.5)
    y2=-(1/18)*x2**2+6
    x3=np.arange(-12,-4.5,0.5)
    y3=-(1/8)*(x3+8)**2+6
    x4=np.arange(4,12.5,0.5)
    y4=-(1/8)*(x4-8)**2+6
    x5=np.arange(-4,-0,35)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,0.25)
    y6=1.5*(x6+3)**2-10
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Зонтик")
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def konn():
    x = np.linspace(-7,7,100)
    y = -3/49*x**2+8
    plt.plot(x,y)
    x = np.linspace(-7,7,100)
    y = 4/49*x**2+1
    plt.plot(x,y)
    x = np.linspace(-6.8,-2,100)
    y = -0.75*(x+4)**2+11
    plt.plot(x,y)
    x = np.linspace(2,6.8,100)
    y = -0.75*(x-4)**2+11
    plt.plot(x,y)
    x = np.linspace(-5.8,-2.8,100)
    y = -1*(x+4)**2+9
    plt.plot(x,y)
    x = np.linspace(2.8,5.8,100)
    y = -1*(x-4)**2+9
    plt.plot(x,y)
    x = np.linspace(-4,4,100)
    y = 4/9*x**2-5
    plt.plot(x,y)
    x = np.linspace(-5.2,5.2,100)
    y = 4/9*x**2-9
    plt.plot(x,y)
    x = np.linspace(-7,-2.8,100)
    y = -1/16*(x+3)**2-6
    plt.plot(x,y)
    x = np.linspace(2.8,7,100)
    y = -1/16*(x-3)**2-6
    plt.plot(x,y)
    x = np.linspace(-7,0,100)
    y = 1/9*(x+4)**2-11
    plt.plot(x,y)
    x = np.linspace(0,7,100)
    y = 1/9*(x-4)**2-11
    plt.plot(x,y)
    x = np.linspace(-7,-4.5,100)
    y = -1*(x+5)**2
    plt.plot(x,y)
    x = np.linspace(4.5,7,100)
    y = -1*(x-5)**2
    plt.plot(x,y)
    x = np.linspace(-3,3,100)
    y = 2/9*x**2+2
    plt.plot(x,y)
    plt.title("Лягуха")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()


aken=Tk()
aken.geometry("900x400")
aken.title("Kalkulator")
f1=Frame(aken,width=700,height=250)
f1.pack()
lbl=Label(f1,text="Решение квадратного уравнения",height=3,width=35,font="Arial 15",fg="black",bg="lightblue",relief="solid")
lbl.pack()
btn1=Label(f1,text="Решение", height=4,width=25,font="Arial 25",fg="black",bg="yellow")
btn1.pack(side=BOTTOM)
a=Entry(f1,width=2,font="Arial 55",fg="white",bg="grey")
a.pack(side=LEFT)
lbl1=Label(f1,text="x**2",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl1.pack(side=LEFT)
b=Entry(f1,width=2,font="Arial 55",fg="white",bg="grey")
b.pack(side=LEFT)
lbl2=Label(f1,text="x+",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl2.pack(side=LEFT)
c=Entry(f1,width=2,font="Arial 55",fg="white",bg="grey")
c.pack(side=LEFT)
lbl3=Label(f1,text="=0",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl3.pack(side=LEFT)
nupp1=Button(f1,text="Решить",font="Arial 20",width=8,fg="white",bg="#001332",relief=RAISED, command=lahend)
nupp1.pack(side=RIGHT)
nupp2=Button(f1,text="График",font="Arial 20",width=8,fg="white",bg="#001332",relief=RAISED, command=graafik)
nupp2.pack(side=RIGHT)
f2=Frame(aken,width=700,height=250)
f2.pack()

btn2=Button(f2,text="Увеличить окно",font="Arial 26", bg="green", command=veel)
btn2.pack()
var=IntVar()
r1=Radiobutton(f2,text="Кит",variable=var,value=1,font="Arial 26",command=kala)
r2=Radiobutton(f2,text="Очки",variable=var,value=2, font="Arial 26",command=prillid)
r3=Radiobutton(f2,text="Зонтик",variable=var,value=3, font="Arial 26",command=vihmavari)
r4=Radiobutton(f2,text="Лягушка",variable=var,value=3, font="Arial 26",command=konn)
r1.pack()
r2.pack()
r3.pack()
r4.pack()




aken.mainloop()