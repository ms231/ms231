from tkinter import *
from tkinter import ttk

def fsum(event):
	n3=int(c.get())
	if n3==1:
		gsum(event)
	if n3==2:
		hsum(event)
	if n3==3:
		isum(event)
	if n3==4:
		jsum(event)


def gsum(event):
	n1=float(m.get())
	n2=float(n.get())
	sum=n1+n2
	z.delete(0,'end')
	z.insert(0,sum)

def hsum(event):
	n1=float(m.get())
	n2=float(n.get())
	mul=n1*n2
	z.delete(0,'end')
	z.insert(0,mul)

def isum(event):
	n1=float(m.get())
	n2=float(n.get())
	sub=n1-n2
	z.delete(0,'end')
	z.insert(0,sub)

def jsum(event):
	n1=float(m.get())
	n2=float(n.get())
	d=n1/n2
	z.delete(0,'end')
	z.insert(0,d)


root=Tk()

root.geometry("600x280+50+50")
root.title("MY FIRST SIMPLE CALCULATOR")

Label(root,text="ENTER THE FIRST NUMBER",font=('arial',10,'bold')).grid(row=0,column=0,sticky=W)
m=Entry(root,width=20,font=('arial',10,'bold'))
m.grid(row=0,column=1,sticky=W)

Label(root,text="ENTER THE SECOND NUMBER",font=('arial',10,'bold')).grid(row=1,column=0,sticky=W)
n=Entry(root,width=20,font=('arial',10,'bold'))
n.grid(row=1,column=1,sticky=W)

Label(root,text="\n").grid(row=2,column=0,sticky=W)

Label(root,text="ENTER 1 FOR ADDITION",font=('arial',10,'bold')).grid(row=3,column=1,sticky=W)

Label(root,text="ENTER 2 FOR MULTIPLICATION",font=('arial',10,'bold')).grid(row=4,column=1,sticky=W)

Label(root,text="ENTER 3 FOR SUBTRACTION",font=('arial',10,'bold')).grid(row=5,column=1,sticky=W)

Label(root,text="ENTER 4 FOR DIVISION",font=('arial',10,'bold')).grid(row=6,column=1,sticky=W)

Label(root,text="\n").grid(row=7,column=0,sticky=W)

Label(root,text="ENTER YOUR CHOICE",font=('arial',10,'bold')).grid(row=8,column=0,sticky=W)

c=Entry(root,width=20,font=('arial',10,'bold'))
c.grid(row=8,column=1,sticky=W)

l=Button(root,text="SAVE",font=('arial',10,'bold'))
l.bind("<Button-1>",fsum)
l.grid(row=8,column=2,sticky=W)


Label(root,text="FINAL RESULT ",font=('arial',10,'bold')).grid(row=9,column=0,sticky=W)

z=Entry(root,width=20,font=('arial',10,'bold'))
z.grid(row=9,column=1,sticky=W)

root.mainloop()
