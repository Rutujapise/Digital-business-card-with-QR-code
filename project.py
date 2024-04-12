from tkinter import *
import qrcode
from PIL  import Image,ImageTk
class qr_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+100+50")
        self.root.title("                                                                                                                                           Qr Generator")
        self.root.resizable(False,False)

        title=Label(self.root,text="  Qr Code Generator",font=("times new roman",40,'bold'),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        #------------Employee Details Window--------------
        #------------variables------------------------
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
        self.var_gender=StringVar()
        self.var_Email=StringVar()
        self.var_Contact_No=StringVar()
        self.var_Address=StringVar()


        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=20,y=100,width=950,height=550)

        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",30,'bold'),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        Label_emp_code=Label(emp_Frame,text="Employee ID :",font=("times new roman",20,'bold'),bg='white').place(x=30,y=70)
        Label_name=Label(emp_Frame,text="Name :",font=("times new roman",20,'bold'),bg='white').place(x=30,y=140)
        Label_department=Label(emp_Frame,text="Department :",font=("times new roman",20,'bold'),bg='white').place(x=30,y=210)
        Label_designation=Label(emp_Frame,text="Designation:",font=("times new roman",20,'bold'),bg='white').place(x=30,y=280)
        Label_Gender=Label(emp_Frame,text="Gender:",font=("times new roman",20,'bold'),bg='white').place(x=500,y=70)
        Label_email=Label(emp_Frame,text="Email ID :",font=("times new roman",20,'bold'),bg='white').place(x=500,y=210)
        Label_contact_no=Label(emp_Frame,text="Contact NO :",font=("times new roman",20,'bold'),bg='white').place(x=500,y=140)
        Label_address=Label(emp_Frame,text="Address :",font=("times new roman",20,'bold'),bg='white').place(x=500,y=280)
 
        txt_emp_code=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=70)
        txt_name=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_name,bg='lightyellow').place(x=200,y=140)
        txt_department=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_department,bg='lightyellow').place(x=200,y=210)
        txt_designation=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_designation,bg='lightyellow').place(x=200,y=280)
        txt_Gender=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_gender,bg='lightyellow').place(x=650,y=70)
        txt_email=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_Email,bg='lightyellow').place(x=650,y=210)
        txt_contact_no=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_Contact_No,bg='lightyellow').place(x=650,y=140)
        txt_address=Entry(emp_Frame,font=("times new roman",20),textvariable=self.var_Address,bg='lightyellow').place(x=650,y=280)

        btn_generate=Button(emp_Frame,text='Qr Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=250,y=400,width=200,height=50)
        btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=550,y=400,width=150,height=50)

        self.msg="All Fields are Required!!!"
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20,'bold'),bg='white',fg='red')
        self.lbl_msg.place(x=350,y=480)
        
        #------------Employee Qr Code Window--------------
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=990,y=100,width=400,height=550)

        emp_title=Label(qr_Frame,text="Employee Qr Code",font=("goudy old style",30,'bold'),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        
        self.qr_code=Label(qr_Frame,text='No Qr\nAvailable',font=("times new roman",25),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=50,y=180,width=300,height=300)
    
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.var_gender.set('')
        self.var_Email.set('')
        self.var_Contact_No.set('')
        self.var_Address.set('')


        self.msg=''
        self.lbl_msg.config(text=self.msg,fg='red')


    def generate(self):
        if self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_department.get()=='' or self.var_gender.get()=='' or self.var_Email.get()=='' or self.var_Contact_No.get()=='' or self.var_Address.get()=='':
            self.msg="All Fields are Required!!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nDesignation:{self.var_designation.get()}\nGender:{self.var_gender.get()}\nEmail:{self.var_Email.get()}\nContact_no:{self.var_Contact_No.get()}\nAddress :{self.var_Address.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code.save("employee_Qr/Emp_"+str(self.var_emp_code.get())+'.png')

            
            #--------------Qr Code Image Update---------------
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

            

            #-------------updating notification------------
            self.msg='Qr Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg='green')
            
            #image
            #image=PhotoImage(file='C:\Users\Dell\Pictures\Camera Roll')
            #root.create_image(0,0,anchor=NW,image=image)
            
root=Tk()
obj=qr_generator(root)
root.mainloop()
