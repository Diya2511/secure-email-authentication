import random
import smtplib
import mysql.connector
from tkinter import *

# enter your password in place of password field and username in place of user  for your sql account

con = mysql.connector.connect(host="localhost",password="1234",user="root",database="EmailAuthentication")


cur = con.cursor()



class StudentInterface:
    def __init__(self,regId):
        
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Secured Email Authentication")
        
        
        # creating heading label
        label1 = Label(self.root, text="Student Interface",fg="Blue",font="italic",pady=20)
        label1.place(x=260,y=50)
        
        
        label2 = Label(self.root, text="Registration Number",fg="red",font="italic",pady=20)
        label2.place(x=100,y=110)
        
        
        label3 = Label(self.root, text="Student Name",fg="red",font="italic",pady=20)
        label3.place(x=100,y=160)
        
        
        label4 = Label(self.root, text="Student Email",fg="red",font="italic",pady=20)
        label4.place(x=100,y=210)
        
        
        label5 = Label(self.root, text="Student Contact",fg="red",font="italic",pady=20)
        label5.place(x=100,y=260)
        
        

        label6 = Label(self.root, text="Student Course",fg="red",font="italic",pady=20)
        label6.place(x=100,y=310)
        
        try:
            
            
            cur.execute("select * from student_details where registration_id = %s" % regId)
            result=cur.fetchone()
            
            label7 = Label(self.root,text=str(result[0]),fg="black",font="italic",pady=20)
            label7.place(x=330,y=110)
            
            label8 = Label(self.root,text=str(result[2]),fg="black",font="italic",pady=20)
            label8.place(x=330,y=160)
            
            label9 = Label(self.root,text=str(result[3]),fg="black",font="italic",pady=20)
            label9.place(x=330,y=210)
            
            label10 = Label(self.root,text=str(result[4]),fg="black",font="italic",pady=20)
            label10.place(x=330,y=260)
            
            label11 = Label(self.root,text=str(result[5]),fg="black",font="italic",pady=20)
            label11.place(x=330,y=310)

        
        except:
            print("mysql exception occured")

        
        
        self.root.mainloop()
        

    

class StudentRegister:
    # constructor
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title("Secured Email Authentication")
        
        self.registration=StringVar()
        self.password=StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        self.course = StringVar()

        # creating heading label
        label1 = Label(self.root, text="Student Login",fg="Blue",font="italic",pady=30)
        label1.place(x=260,y=50)

        # creating registration id label
        label2 = Label(self.root, text="Enter registration id",fg="red",font=('calibre',10,'bold'))
        label2.place(x=170,y=150)
        
        # creating password label
        label3 = Label(self.root, text="Enter password",fg="red",font=('calibre',10,'bold'))
        label3.place(x=170,y=190)
        
        # creating name label
        label4 = Label(self.root, text="Enter name",fg="red",font=('calibre',10,'bold'))
        label4.place(x=170,y=230)
        
        # creating email label
        label5 = Label(self.root, text="Enter email",fg="red",font=('calibre',10,'bold'))
        label5.place(x=170,y=270)
        
        # creating contact label
        label6 = Label(self.root, text="Enter contact",fg="red",font=('calibre',10,'bold'))
        label6.place(x=170,y=310)
        
        # creating course label
        label7 = Label(self.root, text="Enter course",fg="red",font=('calibre',10,'bold'))
        label7.place(x=170,y=350)

        # id input field
        reg_entry = Entry(self.root, textvariable = self.registration, font=('calibre',10,'normal'))
        reg_entry.place(x=310,y=150)
        
        # password input field
        pass_entry = Entry(self.root,textvariable = self.password, font=('calibre',10,'normal'))
        pass_entry.place(x=310,y=190)
        
        # name input field
        name_entry = Entry(self.root,textvariable = self.name, font=('calibre',10,'normal'))
        name_entry.place(x=310,y=230)
        
        # email input field
        email_entry = Entry(self.root,textvariable = self.email, font=('calibre',10,'normal'))
        email_entry.place(x=310,y=270)
        
        # contact input field
        contact_entry = Entry(self.root,textvariable = self.contact, font=('calibre',10,'normal'))
        contact_entry.place(x=310,y=310)
        
        # course input field
        course_entry = Entry(self.root,textvariable = self.course, font=('calibre',10,'normal'))
        course_entry.place(x=310,y=350)
        
        # creating button for student registration
        btn1 = Button(self.root, text = 'Register', bd = '6',fg="white",bg="brown",command=self.register)
        btn1.place(x=290,y=390)  
        
        self.label8 = Label(self.root,fg="blue",font=('calibre',10,'bold'))
        self.label8.place(x=290,y=450)
        
        
        # creating second label
        label9 = Label(self.root, text="Login",fg="red",font=('calibre',10,'bold'))
        label9.place(x=230,y=500)
        
        # creating button for student login
        btn2 = Button(self.root, text = 'Login', bd = '6',fg="white",bg="brown",command=self.login)
        btn2.place(x=290,y=490) 
         

        self.root.mainloop()
        
        
    # login function definition
    def login(self):
        self.root.destroy()
        StudentLogin()
        
            
            
    def register(self):
        reg = int(self.registration.get())
        password = str(self.password.get())
        name = str(self.name.get())
        email = str(self.email.get())
        contact = str(self.contact.get())
        course = str(self.course.get())
         
        try:
            cur.execute("select * from student_details where registration_id = %s"%reg)
            result = cur.fetchall()
            if len(result)==1:  
                self.label8.config(text="user already exists")
            else:
                try:
                    query = "insert into student_details values(%s,%s,%s,%s,%s,%s)"
                    tuple = (reg,password,name,email,contact,course)
                    cur.execute(query,tuple)
                    con.commit()
                    self.label8.config(text="registered successfully")
                except :
                    self.label8.config(text="Failed to register")
        except:
            print("mysql exception occured")



class EnterOtp:
    def __init__(self,number,regId):
        # creating root
        self.root = Tk()
        self.root.geometry("400x500")
        self.root.title("Secured Email Authentication")
        self.number=number
        self.regId = regId
        
        
        self.otp=StringVar()

        # creating heading label
        label1 = Label(self.root, text="Enter Otp Interface",fg="Blue",font="italic",pady=50)
        label1.place(x=160,y=50)
        
        # creating second label
        label3 = Label(self.root, text="Enter otp",fg="red",font=('calibre',10,'bold'))
        label3.place(x=70,y=130)
        
          
        # password input field
        otp_entry = Entry(self.root,textvariable = self.otp, font=('calibre',10,'normal'))
        otp_entry.place(x=210,y=130)
        
        
        # creating button for student login
        btn2 = Button(self.root, text = 'Varify', bd = '6',fg="white",bg="brown",command=self.varify)
        btn2.place(x=130,y=200)  
        

        self.root.mainloop()
        
    def varify(self):
        otpass = int(self.otp.get())
        if otpass==self.number:
            
            print(otpass==self.number)
            self.password = StringVar()
            
            # creating second label
            label2 = Label(self.root, text="Enter new Password",fg="red",font=('calibre',10,'bold'))
            label2.place(x=70,y=260)
            
            
            # password input field
            otp_entry = Entry(self.root,textvariable = self.password, font=('calibre',10,'normal'))
            otp_entry.place(x=210,y=260)
            
            # creating button for student login
            btn3 = Button(self.root, text = 'Set Password', bd = '6',fg="white",bg="brown",command=self.set)
            btn3.place(x=130,y=320)
            
    def set(self):
        newPass = str(self.password.get())
        try:
            cur.execute("update student_details set password = \'%s\' where registration_id = %s"%(newPass,self.regId))
            con.commit()
            label4 = Label(self.root, text="Password set successfully",fg="red",font=('calibre',10,'bold'))
            label4.place(x=70,y=370)
            label5 = Label(self.root, text="Run again to login with new password",fg="red",font=('calibre',10,'bold'))
            label5.place(x=70,y=410)
        except:
            print("sql exception occured")
        
 

class StudentForgot:
    # constructor
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("400x500")
        self.root.title("Secured Email Authentication")
        
        
        # Generate a random number between 1 and 100
        self.number = random.randint(123456, 987654)
        
        
        self.registration=StringVar()

        # creating heading label
        label1 = Label(self.root, text="Forgot Password",fg="Blue",font="italic",pady=50)
        label1.place(x=160,y=50)

        # creating first label
        label2 = Label(self.root, text="Enter registration id",fg="red",font=('calibre',10,'bold'))
        label2.place(x=70,y=180)
        
       

        # id input field
        reg_entry = Entry(self.root,textvariable = self.registration, font=('calibre',10,'normal'))
        reg_entry.place(x=210,y=180)
      
        # creating button for student login
        btn2 = Button(self.root, text = 'Send Otp', bd = '6',fg="white",bg="brown",command=self.sendOtp)
        btn2.place(x=130,y=320)  
        
        
        self.label4 = Label(self.root,fg="blue",font=('calibre',10,'bold'))
        self.label4.place(x=280,y=370)
         

        self.root.mainloop()
        
        
    def sendOtp(self):
        try:
            self.reg = self.registration.get()
            cur.execute("select * from student_details where registration_id = %s" %self.reg)
            result=cur.fetchone()
            email = str(result[3])
            print(email)
            # sending otp
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()

            try:
                server.login('dummyprofile813@gmail.com','teemxnufdqtxevmc')
                server.sendmail('dummyprofile813@gmail.com',email,"your otp is %s"%self.number)
                print("mail sent successfully")
                self.root.destroy()
                EnterOtp(self.number,self.reg)
            except Exception as e:
                print(e)
            server.quit()
            
            
        except:
            print("sql error")



class StudentLogin:
    # constructor
    def __init__(self):
        # creating root
        self.root = Tk()
        self.root.geometry("400x500")
        self.root.title("Secured Email Authentication")
        
        self.registration=StringVar()
        self.password=StringVar()

        # creating heading label
        label1 = Label(self.root, text="Student Login",fg="Blue",font="italic",pady=50)
        label1.place(x=160,y=50)

        # creating first label
        label2 = Label(self.root, text="Enter registration id",fg="red",font=('calibre',10,'bold'))
        label2.place(x=70,y=180)
        
        # creating second label
        label3 = Label(self.root, text="Enter password",fg="red",font=('calibre',10,'bold'))
        label3.place(x=70,y=250)

        # id input field
        reg_entry = Entry(self.root,textvariable = self.registration, font=('calibre',10,'normal'))
        reg_entry.place(x=210,y=180)
        
        # password input field
        pass_entry = Entry(self.root,textvariable = self.password, font=('calibre',10,'normal'))
        pass_entry.place(x=210,y=250)
        
        # creating button for student login
        btn2 = Button(self.root, text = 'Login', bd = '6',fg="white",bg="brown",command=self.login)
        btn2.place(x=130,y=320)  
        
        
        # creating button for student forgot password
        btn4 = Button(self.root, text = 'Forgot Password', bd = '6',fg="white",bg="brown",command=self.forgot)
        btn4.place(x=200,y=320)
        
        self.label4 = Label(self.root,fg="blue",font=('calibre',10,'bold'))
        self.label4.place(x=280,y=370)
        
        # creating second label
        label5 = Label(self.root, text="Register yourself",fg="red",font=('calibre',10,'bold'))
        label5.place(x=70,y=430)
        
        # creating button for student login
        btn3 = Button(self.root, text = 'Register', bd = '6',fg="white",bg="brown",command=self.register)
        btn3.place(x=190,y=420)  

        self.root.mainloop()
        
        
    # login function definition
    def login(self):
        reg = int(self.registration.get())
        password = str(self.password.get())
         
        try:
            cur.execute("select * from student_details where registration_id = %s"%reg)
            result = cur.fetchall()
            if len(result)==1:
                if password==result[0][1]:
                    self.registration_number = reg
                    self.root.destroy()
                    StudentInterface(self.registration_number)
                else:
                    self.label4.config(text="wrong password")
            else:
                self.label4.config(text="student is not registered")
        except:
            print("mysql exception occured")
            
            
    def register(self):
        self.root.destroy()
        StudentRegister()
        
    def forgot(self):
        self.root.destroy()
        StudentForgot()
    
    
        

a = StudentLogin()


con.close()