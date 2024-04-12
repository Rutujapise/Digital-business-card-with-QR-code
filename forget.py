from tkinter import*



def login_page():
    forget_window.destroy()
    import login
    
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


forget_window=Tk()
forget_window.geometry('500x660+50+50')
forget_window.resizable(0,0)
forget_window.title("***forgrt password***")


heading=Label(forget_window,text='Reset Password',font=('Times new roman',23,'bold'),bg='white',fg='blue')
heading.place(x=150,y=100)

# USERNAME
usernamelabel=Label(forget_window,text='Username',font=('Times new roman',18,'bold'),bg='white',fg='blue')
usernamelabel.place(x=50,y=185 )
usernameEntry=Entry(forget_window,width=25,font=('Times new roman',23,'bold'))
usernameEntry.place(x=50,y=220)
usernameEntry.insert(0,'   ')
usernameEntry.bind('<FocusIn>',user_enter)
Frame2=Frame(forget_window,width=250,height=2,bg='pink')
Frame2.place(x=50,y=260)
# new password
passwordlabel=Label(forget_window,text='New Password',font=('Times new roman',18,'bold'),bg='white',fg='blue')
passwordlabel.place(x=50,y=270 )
passwordEntry=Entry(forget_window,width=25,font=('Times new roman',23,'bold'))
passwordEntry.place(x=50,y=305)
passwordEntry.insert(0,'   ')
passwordEntry.bind('<FocusIn>',password_enter)
Frame3=Frame(forget_window,width=250,height=2,bg='pink')
Frame3.place(x=50,y=342)
# confirm password
confirmpasswordlabel=Label(forget_window,text='Confirm Password',font=('Times new roman',18,'bold'),bg='white',fg='blue')
confirmpasswordlabel.place(x=50,y=355 )
confirmpasswordEntry=Entry(forget_window,width=25,font=('Times new roman',23,'bold'))
confirmpasswordEntry.place(x=50,y=390)
confirmpasswordEntry.insert(0,'   ')
confirmpasswordEntry.bind('<FocusIn>',user_enter)
Frame4=Frame(forget_window,width=250,height=2,bg='pink')
Frame4.place(x=50,y=427)
#submit
submitButten= Button(forget_window,text='       Submit    ',font=('Open Sans',16,'bold'),
                          fg='white',bg='blue',activeforeground='white',activebackground='blue'
                          ,cursor='hand2',bd=0,width=31, command=login_page) 
submitButten.place(x=50,y=480)





forget_window.mainloop()