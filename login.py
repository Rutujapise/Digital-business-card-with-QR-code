from tkinter import*
#from pillow import imageTk
#functionality 
#def hide():
   # openeye.config(file='closeye.png')
    #passwordEntry.config(show='*')
    #eyeButton.config(command=show)
#def show():
    #openeye.config(file='closeye.png')
    #passwordEntry.config(show='*')
    #eyeButton.config(command=hide)

def reg_page():
    login_window.destroy()
    import reg

def forget_page():
    login_window.destroy()
    import forget

def project_page():
    login_window.destroy()
    import project    
    

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#GUIpart
login_window=Tk()
login_window.geometry('500x660+50+50')
login_window.resizable(0,0)
login_window.title("***Login Page***")


#bgImage=imageTk.photoimage(file='bg.jpg')
#bglabel=Label(root,image=bgImage)
#bglabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Times new roman',23,'bold'),bg='white',fg='blue')
heading.place(x=150,y=100)
#username
usernameEntry=Entry(login_window,width=25,font=('Times new roman',23,'bold'), fg='grey')
usernameEntry.place(x=50,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

#Frame1=Frame(login_window,width=250,height=2,bg='pink')
#Frame1.place(x=50,y=235)

passwordEntry=Entry(login_window,width=25,font=('Times new roman',23,'bold'),fg='grey')
passwordEntry.place(x=50,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

#Frame2=Frame(login_window,width=250,height=2,bg='pink')
#Frame2.place(x=50,y=295)

#openeye=PhotoImage(file='openeye.png')
#eyeButton=Button(login_window,image=openeye ,bd=0,bg='white',activebackground='white',cursor='hand2')
#eyeButton.place(x=800,y=258)

forgeButton=Button(login_window,text='Forgot Password' ,bd=0,bg='white',activebackground='white',
font=('Times new roman',11,'bold underline'),fg='blue',
activeforeground='blue',command=forget_page)
forgeButton.place(x=50,y=310)
loginButten= Button(login_window,text='        Login    ',font=('Open Sans',16,'bold'),fg='white'
                    ,bg='blue',activeforeground='white',activebackground='blue',cursor='hand2',bd=0,width=31,command=project_page) 
loginButten.place(x=50,y=350)

orlabel= Label(login_window,text='-----------------------------OR------------------------',font=('Open Sans', 16), 
               fg='blue',bg='white')
orlabel.place(x=50,y=400)

signuplabel= Label(login_window,text='Dont have an account?',font=('Open Sans', 9,'bold'), fg='blue',bg='white')
signuplabel.place(x=50,y=450)


newaccuntButten= Button(login_window,text='   creat new one    ',font=('Open Sans',9,'bold underline'),fg='white'
                    ,bg='blue',activeforeground='white',activebackground='blue',cursor='hand2',bd=0,command=reg_page) 
newaccuntButten.place(x=300,y=450)
#self massage



login_window.mainloop()