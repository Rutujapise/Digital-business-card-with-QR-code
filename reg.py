from tkinter import *
#from PIL import ImageTk

def login_page():
    signup_windoW.destroy()
    import login

def email_enter(event):
    if emailentry.get()=='Username':
        emailentry.delete(0,END)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)


def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def confirmpassword_enter(event):
    if confirmpasswordEntry.get()=='Password':
        confirmpasswordEntry.delete(0,END)

signup_windoW=Tk()

#GUIpart
#signup_windoW=Tk()
signup_windoW.geometry('500x660+50+50')
signup_windoW.resizable(0,0)
signup_windoW.title("***REGISTRATION PAGE***")




#Frame=Frame(signup_windoW)
#Frame.place(x=50,y=235)

heading=Label(signup_windoW,text='CRATE AN ACCOUNT',font=('Times new roman',18,'bold'),bg='white',fg='blue')
heading.place(x=100,y=50)
#EMAIL
emaillabel=Label(signup_windoW,text='Email',font=('Times new roman',18,'bold'),bg='white',fg='blue')
emaillabel.place(x=50,y=105 )
emailentry=Entry(signup_windoW,width=25,font=('Times new roman',23,'bold'))
emailentry.place(x=50,y=140)
emailentry.insert(0,' ')
emailentry.bind('<FocusIn>',email_enter)
Frame1=Frame(signup_windoW,width=250,height=2,bg='pink')
Frame1.place(x=50,y=179)
# USERNAME
usernamelabel=Label(signup_windoW,text='Username',font=('Times new roman',18,'bold'),bg='white',fg='blue')
usernamelabel.place(x=50,y=185 )
usernameEntry=Entry(signup_windoW,width=25,font=('Times new roman',23,'bold'))
usernameEntry.place(x=50,y=220)
usernameEntry.insert(0,'   ')
usernameEntry.bind('<FocusIn>',user_enter)
Frame2=Frame(signup_windoW,width=250,height=2,bg='pink')
Frame2.place(x=50,y=260)
#password
passwordlabel=Label(signup_windoW,text='Password',font=('Times new roman',18,'bold'),bg='white',fg='blue')
passwordlabel.place(x=50,y=270 )
passwordEntry=Entry(signup_windoW,width=25,font=('Times new roman',23,'bold'))
passwordEntry.place(x=50,y=305)
passwordEntry.insert(0,'   ')
passwordEntry.bind('<FocusIn>',password_enter)
Frame3=Frame(signup_windoW,width=250,height=2,bg='pink')
Frame3.place(x=50,y=342)
# confirm password
confirmpasswordlabel=Label(signup_windoW,text='Confirm Password',font=('Times new roman',18,'bold'),bg='white',fg='blue')
confirmpasswordlabel.place(x=50,y=355 )
confirmpasswordEntry=Entry(signup_windoW,width=25,font=('Times new roman',23,'bold'))
confirmpasswordEntry.place(x=50,y=390)
confirmpasswordEntry.insert(0,'   ')
confirmpasswordEntry.bind('<FocusIn>',user_enter)
Frame4=Frame(signup_windoW,width=250,height=2,bg='pink')
Frame4.place(x=50,y=427)
# chechbutten
ternsanconditions= Checkbutton(signup_windoW,text='I agree to the Terms & Condition',font=('Open Sans',9,'bold' )
                               ,fg='blue',bg='white',activeforeground='white',activebackground='white') 
ternsanconditions.place(x=50,y=440)
#regstritionButten
regstritionButten= Button(signup_windoW,text='       Regsiter   ',font=('Open Sans',16,'bold'),
                          fg='white',bg='blue',activeforeground='white',activebackground='blue'
                          ,cursor='hand2',bd=0,width=31,command= login_page) 
regstritionButten.place(x=50,y=480)
#alreadyaccount
alreadyaccount=Label(signup_windoW,text="Don't have an account?",font=('Open Sans',9,'bold','underline'),
                     fg='blue',bg='white',bd=0,activeforeground='white',activebackground='blue',cursor='hand2') 
alreadyaccount.place(x=50,y=600)
#login
loginButten= Button(signup_windoW,text='     login   ',font=('Open Sans',9,'bold underline'),
                          fg='white',bg='blue',activeforeground='white',activebackground='blue'
                          ,cursor='hand2', command= login_page) 
loginButten.place(x=350,y=600)

#bgImage=imageTk.photoimage(file='bg.jpg')
#bglabel=Label(root,image=bgImage)
#bglabel.place(x=0,y=0)

signup_windoW.mainloop()
