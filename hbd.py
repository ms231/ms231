from tkinter import *

def fun(event):
	m=str(e1.get())
	op=str('Happy Birthday To ')+str(m)
	e2.delete(0,END)
	e2.insert(0,op)	

def clear(event):
	op=str(' ')
	e1.delete(0,END)
	e2.delete(0,END)	

root=Tk()

root.title('WISHING OTHERS')

#root.geometry('600x300+50+50')

l1=Label(root,text='ENTER YOUR NAME',font=('arial',18,'bold'))
l1.grid(row=0,column=0)

e1=Entry(root,font=('arial',14,'bold'),width=20)
e1.grid(row=1,column=0)

b1=Button(root,text='SAVE',width=5,height=2,font=('arial',10,'bold'))
b1.bind("<Button-1>",fun)
b1.grid(row=2,column=0)

Label(root,text='\n').grid(row=3,column=0)

l2=Label(root,text='YOUR MESSAGE IS HERE',font=('arial',18,'bold'))
l2.grid(row=4,column=0)

Label(root,text='\n').grid(row=5,column=0)

e2=Entry(root,font=('arial',15,'bold'),width=45)
e2.grid(row=6,column=0)

Label(root,text='\n').grid(row=7,column=0)

b2=Button(root,text='CLEAR',width=5,height=2,font=('arial',10,'bold'))
b2.bind("<Button-1>",clear)
b2.grid(row=8,column=0)

Label(root,text='\n').grid(row=9,column=0)

root.mainloop()
