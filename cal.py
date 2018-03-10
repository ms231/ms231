from tkinter import *
from tkinter import ttk

a1=0
b1=0
c1=0
d1=0
e1=0
f1=0
g1=0
h1=0
i1=0
j1=0
l1=0
m1=0
n1=0

def dis(event):
	z.delete(0,'end')
	z.insert(0,' ')

def adis(event):
	a1=a1+1
	z.delete(0,'end')
	z.insert(0,1)

def bdis(event):
	b1=b1+1
	z.delete(0,'end')
	z.insert(0,2)

def cdis(event):
	c1=c1+1
	z.delete(0,'end')
	z.insert(0,3)

def ddis(event):
	d1=d1+1
	z.delete(0,'end')
	z.insert(0,4)

def edis(event):
	e1=e1+1
	z.delete(0,'end')
	z.insert(0,5)

def fdis(event):
	f1=f1+1	
	z.delete(0,'end')
	z.insert(0,6)

def gdis(event):
	g1=g1+1
	z.delete(0,'end')
	z.insert(0,7)

def hdis(event):
	h1=h1+1	
	z.delete(0,'end')
	z.insert(0,8)

def idis(event):
	i1=i1+1
	z.delete(0,'end')
	z.insert(0,9)

def jdis(event):
	j1=j1+1
	z.delete(0,'end')
	z.insert(0,0)

def kdis(event):
	k1=k1+1
	z.delete(0,'end')
	z.insert(0,'+')

def ldis(event):
	l1=l1+1
	z.delete(0,'end')
	z.insert(0,'*')

def mdis(event):
	m1=m1+1
	z.delete(0,'end')
	z.insert(0,'-')

def ndis(event):
	n1=n1+1
	z.delete(0,'end')
	z.insert(0,'/')

root=Tk()

#y1=Entry(root,width=5).grid(row=0,column=2,sticky=NE)
#x1=Entry(root,width=5).grid(row=0,column=3,sticky=NE)
#z3=Entry(root,width=5).grid(row=0,column=4,sticky=NE)
#y=Entry(root,width=5).grid(row=0,column=5,sticky=NE)
z=Entry(root,width=5)
z.grid(row=0,column=6,sticky=NE)

a=Button(root,text='7',width=5)
a.bind("<Button-1>",gdis)
a.grid(row=2,column=0,sticky=W)

b=Button(root,text='8',width=5)
b.bind("<Button-1>",hdis)
b.grid(row=2,column=1,sticky=W)

c=Button(root,text='9',width=5)
c.bind("<Button-1>",idis)
c.grid(row=2,column=2,sticky=W)

j=Button(root,text='/',width=5)
j.bind("<Button-1>",ndis)
j.grid(row=2,column=3,sticky=W)

d=Button(root,text='4',width=5)
d.bind("<Button-1>",ddis)
d.grid(row=3,column=0,sticky=W)

e=Button(root,text='5',width=5)
e.bind("<Button-1>",edis)
e.grid(row=3,column=1,sticky=W)

f=Button(root,text='6',width=5)
f.bind("<Button-1>",fdis)
f.grid(row=3,column=2,sticky=W)

k=Button(root,text='*',width=5)
k.bind("<Button-1>",ldis)
k.grid(row=3,column=3,sticky=W)

g=Button(root,text='1',width=5)
g.bind("<Button-1>",adis)
g.grid(row=4,column=0,sticky=W)

h=Button(root,text='2',width=5)
h.bind("<Button-1>",bdis)
h.grid(row=4,column=1,sticky=W)

i=Button(root,text='3',width=5)
i.bind("<Button-1>",cdis)
i.grid(row=4,column=2,sticky=W)

l=Button(root,text='+',width=5)
l.bind("<Button-1>",kdis)
l.grid(row=4,column=3,sticky=W)

m=Button(root,text='AC',width=5)
m.bind("<Button-1>",dis)
m.grid(row=5,column=0,sticky=W)

n=Button(root,text='0',width=5)
n.bind("<Button-1>",jdis)
n.grid(row=5,column=1,sticky=W)

o=Button(root,text='=',width=5)
o.bind("<Button-1>",dis)
o.grid(row=5,column=2,sticky=W)

p=Button(root,text='-',width=5)
p.bind("<Button-1>",mdis)
p.grid(row=5,column=3,sticky=W)



root.mainloop()
