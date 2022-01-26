from tkinter import*
import math

def discr(a,b,c):
	D=b*b -4*a*c
	if D >= 0:
		x1 = (-b + sqrt(D)) / (2*a)
		x2 = (-b - sqrt(D)) / (2*a)
		text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)        
	else:
		text = "The discriminant is: %s \n This equation has no solutions" % D 
	return text

def data(value):
	"""Функция берёт числа из полей"""
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

aken=Tk()
aken.title("´Kalkulator")
lbl=Label(aken,text="Решение квадратного уравнения",height=3,width=35,font="Arial 15",fg="black",bg="lightblue",relief="solid")
lbl.pack()
aken.geometry("900x400")
txt1=Entry(aken,width=2,font="Arial 55",fg="white",bg="grey")
txt1.place(x=155,y=110)
lbl1=Label(aken,text="x**2",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl1.place(x=255,y=100)
txt2=Entry(aken,width=2,font="Arial 55",fg="white",bg="grey")
txt2.place(x=355,y=110)
lbl2=Label(aken,text="x+",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl2.place(x=455,y=100)
txt3=Entry(aken,width=2,font="Arial 55",fg="white",bg="grey")
txt3.place(x=535,y=110)
lbl3=Label(aken,text="=0",height=3,width=5,font="Arial 20",fg="black",bg="white")
lbl3.place(x=630,y=100)
nupp=Button(aken,text="Решить",font="Arial 20",width=8,fg="white",bg="#001332",relief=RAISED)
nupp.place(x=697,y=125)
vvod=Label(aken,text="Решение", height=4,width=60,font="Arial 20",fg="black",bg="yellow")
vvod.pack(side=BOTTOM)

aken.mainloop()