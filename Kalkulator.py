from tkinter import*
from math import *
import matplotlib.pyplot as plt
import numpy as np

def lahend(a,b,c):
    D=b*b-4*a*c
    if D>=0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        text="Дискриминант:%s\nX1: %s\nX2: %s\n"%(D,x1,x2)        
    else:
        text="Дискриминант:%s\n Данное уравнение не имеет решений"%D 
    return text

def data(value):
    vvod.delete("0.0","end")
    vvod.insert("0.0",value)

def calc():
	try:
		txt1=float(a.get())
		txt2=float(b.get())
		txt3=float(b.get())
		data(solver(txt1, txt2, txt3))
	except ValueError:
		data("Убедись что ты ввёл 3 значения")

def grafik():
    t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.comfig(text="Уменшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="Увеличить окно")
        t=0


def graafik():
    graf,D,t=lahend()
    if graf==True:
        ap=float(a.get())
        bp=float(b.get())
        cp=float(c.get())
        x0=(-bp)/(2*ap)
        y0=ap*x0*x0+bp*x0+c
        x1 = np.arrange(x0-10, x0+10, 0.5)
        y1=ap*x1*x1+bp*x1+c
        fig= plt.figure()
        plt.plot(x1,y1,"r-d")
        plt.tittle("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")

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
    x8=np.arange(-15,-12.5,0,5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=[l]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Кит")
    plt.title("Очки")
    plt.title("Лягуха")




aken=Tk()
aken.title("´Kalkulator")
lbl=Label(aken,text="Решение квадратного уравнения",height=3,width=35,font="Arial 15",fg="black",bg="lightblue",relief="solid")
lbl.pack()
aken.geometry("900x650")
txt1=Entry(aken,width=2,font="Arial 55",fg="white",bg="grey")
txt1.pack(side=LEFT)
lbl1=Label(aken,text="x**2",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl1.pack(side=LEFT)
txt2=Entry(aken,width=2,font="Arial 55",fg="white",bg="grey")
txt2.pack(side=LEFT)
lbl2=Label(aken,text="x+",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl2.pack(side=LEFT)
txt3=Entry(aken,width=2,font="Arial 55",fg="white",bg="grey")
txt3.pack(side=LEFT)
lbl3=Label(aken,text="=0",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl3.pack(side=LEFT)
nupp1=Button(aken,text="Решить",font="Arial 20",width=8,fg="white",bg="#001332",relief=RAISED, command=lahend)
nupp1.pack(side=RIGHT)
nupp2=Button(aken,text="График",font="Arial 20",width=8,fg="white",bg="#001332",relief=RAISED, command=graafik)
nupp2.pack(side=RIGHT)
vvod=Label(aken,text="Решение", height=4,width=25,font="Arial 25",fg="black",bg="yellow")
vvod.pack(side=BOTTOM)
f1=Frame(aken,width=700,height=350)
f1.pack(side=TOP)
f2=Frame(aken,width=700,height=350)
f2.pack(side=BOTTOM)

btn_veel=Button(f2,text="Увеличить окно",font="Arial 26", bg="green", command=veel)
btn_veel.pack(side=TOP)
var=IntVar()
r1=Radiobutton(f2,text="Кит",variable=var,var=1,font="Arial 26")
r2=Radiobutton(f2,text="Очки",variable=var,var=2, font="Arial 26")
r3=Radiobutton(f2,text="Лягуха",variable=var,var=3, font="Calibri 26")







aken.mainloop()