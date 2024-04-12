from tkinter import *
import qrcode
from PIL  import Image,ImageTk
class qr_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+100+50")
        self.root.title("                                                                                                         Qr Generator")
        self.root.resizable(False,False)

 #------------Employee Qr Code Window--------------
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=700,y=100,width=400,height=500)

        emp_title=Label(qr_Frame,text="Employee Qr Code",font=("goudy old style",30,'bold'),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        
        self.qr_code=Label(qr_Frame,text='No Qr\nAvailable',font=("times new roman",25),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=50,y=140,width=300,height=200)
    
    

       # self.msg=''
        #self.lbl_msg.config(text=self.msg,fg='red')


    def generate(self):
        if self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_department.get()=='':
            self.msg="All Fields are Required!!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\ndepartment:{self.var_department.get()}\ndesignation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code.save("employee_Qr/Emp_"+str(self.var_emp_code.get())+'.png')

            
            #--------------Qr Code Image Update---------------
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

            

            #-------------updating notification------------
            self.msg='Qr Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg='green')




root=Tk()
obj=qr_generator(root)
root.mainloop()