from tkinter import *
import tkinter.messagebox

root=Tk()

root.title("TIC-TAC-TOE GAME")

click=True

def check(but):
	global click
	if but['text']==' ' and click==True:
		but['text']='X'
		click=False

	elif but['text']==' ' and click==False:
		but['text']='O'
		click=True

	elif (but1['text']=='X' and but2['text']=='X' and but3['text']=='X' or 
		but4['text']=='X' and but5['text']=='X' and but6['text']=='X' or 
		but7['text']=='X' and but8['text']=='X' and but9['text']=='X' or 
		but1['text']=='X' and but5['text']=='X' and but9['text']=='X' or 
		but3['text']=='X' and but5['text']=='X' and but7['text']=='X' or 
		but1['text']=='X' and but4['text']=='X' and but7['text']=='X' or 
		but2['text']=='X' and but5['text']=='X' and but8['text']=='X' or 
		but3['text']=='X' and but6['text']=='X' and but9['text']=='X') :
		tkinter.messagebox.showinfo("WINNER IS X","YOU HAVE WON THE GAME OF TIC-TAC-TOE") 

	elif (but1['text']=='O' and but2['text']=='O' and but3['text']=='O' or 
                but4['text']=='O' and but5['text']=='O' and but6['text']=='O' or
                but7['text']=='O' and but8['text']=='O' and but9['text']=='O' or
                but1['text']=='O' and but5['text']=='O' and but9['text']=='O' or
                but3['text']=='O' and but5['text']=='O' and but7['text']=='O' or
                but1['text']=='O' and but4['text']=='O' and but7['text']=='O' or
                but2['text']=='O' and but5['text']=='O' and but8['text']=='O' or
                but3['text']=='O' and but6['text']=='O' and but9['text']=='O') :
                tkinter.messagebox.showinfo("WINNER IS O","YOU HAVE WON THE GAME OF TIC-TAC-TOE")
	else:      
                tkinter.messagebox.showinfo("NO ONE WINS","THE GAME OF TIC-TAC-TOE IS A DRAW")


but=StringVar()


but1=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but1))
but1.grid(row=0,column=0)

but2=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but2))
but2.grid(row=0,column=1)

but3=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but3))
but3.grid(row=0,column=2)

but4=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but4))
but4.grid(row=1,column=0)

but5=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but5))
but5.grid(row=1,column=1)

but6=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but6))
but6.grid(row=1,column=2)

but7=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but7))
but7.grid(row=2,column=0)

but8=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but8))
but8.grid(row=2,column=1)

but9=Button(root,text=" ",font=('arial',20,'bold'),width=3,height=2,justify='right',bd=5,command=lambda:check(but9))
but9.grid(row=2,column=2)


root.mainloop()
