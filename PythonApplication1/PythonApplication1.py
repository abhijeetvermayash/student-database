import tkinter 
from tkinter import *
from tkinter import ttk
import pymysql
class student:
    def __init__(self, root):
        self.root=root
        self.root.title("STUDENT DATA BASE MANAGEMENT PART 1")
        self.root.geometry("1350x750+0+0")

        #=========================all variable===================================#

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.search_by=StringVar()
        self.search_text=StringVar()






        #=========Manage_frame=======================#

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Manage_Frame.place(x=20,y=100,width=500,height=560)


        m_title=Label(Manage_Frame,text="MANAGE STUDENTS",font=("comic sans",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll no",font=("comic sans",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        textroll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textroll.grid(row=1,column=1,pady=10,padx=10)

        
        lbl_Name=Label(Manage_Frame,text="Name",font=("comic sans",20,"bold"))
        lbl_Name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        textName=Entry(Manage_Frame,textvariable=self.name_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textName.grid(row=2,column=1,pady=10,padx=10)

        lbl_email=Label(Manage_Frame,text="email",font=("comic sans",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        textemail=Entry(Manage_Frame,textvariable=self.email_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textemail.grid(row=3,column=1,pady=10,padx=10)

        lbl_Gender=Label(Manage_Frame,text="Gender",font=("comic sans",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,state='readonly',font=(25))
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)

        lbl_contact=Label(Manage_Frame,text="Contact",font=("comic sans",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        textcontact=Entry(Manage_Frame,textvariable=self.contact_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textcontact.grid(row=5,column=1,pady=10,padx=10)

        
        #=========button_frame=======================#

        button_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="white")
        button_Frame.place(x=10,y=450,width=450)

        Addbtn=Button(button_Frame,text='ADD',width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Delbtn=Button(button_Frame,text='DEL',width=10,command=self.del_row).grid(row=0,column=1,padx=10,pady=10)
        updatebtn=Button(button_Frame,text='UPDATE',width=10,command=self.update_data).grid(row=0,column=2,padx=10,pady=10)
        Clrbtn=Button(button_Frame,text='CLEAR',width=10,command=self.clear_fun).grid(row=0,column=3,padx=10,pady=10)
       
        #=========detail_frame=======================#

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Detail_Frame.place(x=550,y=100,width=750,height=560)

        
        lbl_search=Label(Detail_Frame,text="Search",font=("comic sans",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,state='readonly',font=(10))
        combo_search['values']=("rollno","name","contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        textsearch=Entry(Detail_Frame,textvariable=self.search_text,font=("comic sans",10,"bold"),bd=5,relief=GROOVE)
        textsearch.grid(row=0,column=2,pady=10,padx=10)

        searchbtn=Button(Detail_Frame,command=self.fetch_some,text='SEARCH',width=10).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text='SHOW ALL',width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #==============table_frame=============================#

        table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="white")
        table_Frame.place(x=0,y=100,width=740,height=450)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_Frame,column=("roll","name","email","gender","contact"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("roll",text="roll No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="email")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table['show']='headings'

        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    def add_students(self):
        com=pymysql.connect(host='localhost',user='root',password='8579081636',database='stm')
        cur=com.cursor()
        try:
            cur.execute("insert into studs values(%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.name_var.get(),self.email_var.get(),
                                                                self.gender_var.get(),self.contact_var.get()
                                                              ))
            self.clear_fun()
            print("ok")
        except Exception as e:
            print("Exception: ",e)
       
        com.commit()
        self.fetch_data()
        self.clear_fun()
        com.close()
    
    def add_table(self):
        connection=pymysql.connect(host='localhost',user='root',password='8579081636',database='stm')
        cursor=connection.cursor()
        sql_query="""create table abhi(
        _id int,name varchar(20))"""
        try:
           cursor.execute(sql_query)
           print("ok")
        except Exception as e:
           print("Exception: ",e)

        connection.close()

    def del_row(self):
        com=pymysql.connect(host='localhost',user='root',password='8579081636',database='stm')
        cur=com.cursor()
        try:
            cur.execute("delete from studs where rollno=%s",self.Roll_No_var.get())
            print("ok")
        except Exception as e:
            print("Exception: ",e)
       
        com.commit()
        self.fetch_data()
        self.clear_fun()
        com.close()

    def show_all(self):
        com=pymysql.connect(host='localhost',user='root',password='8579081636',database='stm')
        cur=com.cursor()
        try:
            cur.execute("select * from studs")
            print("ok")
        except Exception as e:
            print("Exception: ",e)
       
        com.commit()
        com.close()

    def fetch_data(self):
         com=pymysql.connect(host='localhost',user='root',password='8579081636',database='stm')
         cur=com.cursor()
         try:
             cur.execute("select * from studs")
             rows=cur.fetchall()
             if (rows!=0):
                 self.student_table.delete(*self.student_table.get_children())
                 for row in rows:
                     self.student_table.insert('',END,values=row)
                 com.commit()
             print("ok")
         except Exception as e:
            print("Exception: ",e)
         com.close()

    def clear_fun(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        print("okayyy")

    def update_data(self):
        com=pymysql.connect(host='localhost',user='root',password='8579081636',database='stm')
        cur=com.cursor()
        try:
            cur.execute("update studs set name=%s,email=%s,gender=%s,contact=%s where rollno=%s",(self.name_var.get(),self.email_var.get(),
                                                                self.gender_var.get(),self.contact_var.get(),self.Roll_No_var.get()
                                                              ))
            self.clear_fun()
            print("fine")
        except Exception as e:
            print("Exception: ",e)
       
        com.commit()
        self.fetch_data()
        self.clear_fun()
        com.close()

    def fetch_some(self):
         com=pymysql.connect(host='localhost',user='root',password='8579081636',database='stm')
         cur=com.cursor()
         try:
             cur.execute("select * from studs where " + str(self.search_by.get())+ " LIKE " + "'%"+str(self.search_text.get())+"%'")
             rows=cur.fetchall()
             if (rows!=0):
                 self.student_table.delete(*self.student_table.get_children())
                 print("if")
                 for row in rows:
                     self.student_table.insert('',END,values=row)
                     print("nice")
                 com.commit()
             print("yesss")
         except Exception as e:
            print("Exception: ",e)
         com.close()



        
        


       


   

   


       
         




root=Tk()
ob=student(root)
root.mainloop()



