from tkinter import *

root=Tk()
#root.geometry("300x340+50+50")
root.title("CALCULATOR")

def btnClick(number):
	global op
	op=op+str(number)
	text.set(op)


def clear():
	global op
	op=''
	text.set('')

def equal():
	global op
	sums=str(eval(op))
	text.set(sums)
	op=''

op=''
text=StringVar()

f1=Frame(root,bd=4,relief='raise')
f1.pack(side=TOP)

e1=Entry(f1,textvariable=text,font=('arial',18,'bold'),width=16,bd=4,justify='right')
e1.grid(row=0,column=0)

f2=Frame(root,bd=4,relief='raise')
f2.pack(side=BOTTOM)

b7=Button(f2,text='7',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(7))
b7.grid(row=0,column=0)
b8=Button(f2,text='8',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(8))
b8.grid(row=0,column=1)
b9=Button(f2,text='9',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(9))
b9.grid(row=0,column=2)
bplus=Button(f2,text='+',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick('+'))
bplus.grid(row=0,column=3)

b4=Button(f2,text='4',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(4))
b4.grid(row=1,column=0)
b5=Button(f2,text='5',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(5))
b5.grid(row=1,column=1)
b6=Button(f2,text='6',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(6))
b6.grid(row=1,column=2)
bsub=Button(f2,text='-',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick('-'))
bsub.grid(row=1,column=3)

b1=Button(f2,text='1',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(1))
b1.grid(row=2,column=0)
b2=Button(f2,text='2',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(2))
b2.grid(row=2,column=1)
b3=Button(f2,text='3',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(3))
b3.grid(row=2,column=2)
bmul=Button(f2,text='*',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick('*'))
bmul.grid(row=2,column=3)

bc=Button(f2,text='C',font=('arial',16,'bold'),fg='black',width=3,command=clear)
bc.grid(row=3,column=0)
b0=Button(f2,text='0',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick(0))
b0.grid(row=3,column=1)
beq=Button(f2,text='=',font=('arial',16,'bold'),fg='black',width=3,command=equal)
beq.grid(row=3,column=2)
bdiv=Button(f2,text='/',font=('arial',16,'bold'),fg='black',width=3,command=lambda:btnClick('/'))
bdiv.grid(row=3,column=3)

root.mainloop()
