"""
Title:Job Database 

Author:Joshua Kitenge

"""

# imports

from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from delete_entry import Delete_Entry
from new_entry import New_Entry
from update_entry import Update_Entry

# The job database class   

class JobApplicationDatabase:
        def __init__(self,master):
            self.master = master
            master.title("Job applications database") # Title of the window  
            master.geometry("900x500") # The size of the window 
            master.iconbitmap('images/database.ico') # Window icon

            #-----------------------------------------------

            #Creating the main buttons for the master window

            #-----------------------------------------------

            # Creating the button to enter a new entry into the database 

            self.Entry_button = Button(master,text="New Entry",command=lambda :New_Entry(Toplevel(),self.con),padx=100,pady=60,state=DISABLED)
            self.Entry_button.grid(row=2,column=0,columnspan=3) # Defining the position of the button on the window

            # Creating the button to update a entry in the database
 
            self.Update_button = Button(master,text="Update", command =lambda : Update_Entry(Toplevel(),self.con),padx=108.4,pady=60,state=DISABLED ) 
            self.Update_button.grid(row=3,column=0,columnspan=3) # Defining the postion of the button on the window 

            # Creating the button to delete a entry in the database 
            
            self.Delete_button = Button(master,text="Delete",command= lambda: Delete_Entry(Toplevel(),self.con),padx=110.5,pady=60,state=DISABLED)
            self.Delete_button.grid(row=4,column=0,columnspan=3) # Defining the position of the button on the window

            # Creating the button that shows the Job aplications table on the window 

            self.job_app_button = Button(master,text="Job application table",command =self.job_app_table_comm,padx=45,pady=60,state=DISABLED )
            self.job_app_button.grid(row=4,column=3) # Defining the postion of the button on the window

            # Creating the button that shows the Aptitude testing table on the window 

            self.AP_test_button = Button(master,text="Aptitude testing table",command =self.AP_test_table_comm, padx=42.5,pady=60,state=DISABLED )
            self.AP_test_button.grid(row=4,column=4) # Defining the postion of the button on the window

            # Creating the button that shows the Automated interview table on the window 

            self.Auto_inter_button = Button(master,text="Automated interview table",command =self.Auto_inter_table_comm,padx=29.5,pady=60,state=DISABLED )
            self.Auto_inter_button.grid(row=4,column=5) # Defining the postion of the button on the window 

            #--------------------------------
            
            # Creating area to enter password

            #--------------------------------

            # Creating the Label for the password 

            self.password = Label(master,text ="Password")
            self.password.grid(row=0,column=0,sticky=W) # Defining the postion of the label on thw window 
            
            # Creating the entry box for password 

            self.password_entry = Entry(master,width=20)
            self.password_entry.grid(row=0,column=1,sticky=W,pady=10) # Defining the postion of the entry box on the window
            self.password_entry.insert(0,"Enter password") # Entry box message with box 

            # Creating the button for the password 

            self.password_button = Button(master,text="Enter",command = self.password_entry_2)
            self.password_button.grid(row=0,column=2) # Defining the postion of the button on the window 
            



        #-----------------------------------

        # Creating the command for the enter:
        # Access database
        # Show Job Application
        #-----------------------------------

        def password_entry_2(self):

            # Getting the password enter in to the entry box 

            self.password_n = self.password_entry.get()

            # Connecting into the jobs server to access the database on mysql  
            
            con=mysql.connect(host="localhost",
                    user="root",
                    password= self.password_n,
                    database="jobs")

            self.con = con

            # Creating a label underneath the entry box 

            self.password_lab = Label(self.master,text="Password entered succesfully")
            self.password_lab.grid(row=1,column=0, columnspan=3) # Defining the postion of the label on the window 
            self.password_entry.delete(0,END) # Deleting the password enter after enter successfully 

            # Activating the button once password is enter successfully 

            self.Delete_button['state'] = NORMAL
            self.Entry_button['state'] = NORMAL
            self.Update_button['state'] = NORMAL 
            self.job_app_button['state'] = NORMAL 
            self.AP_test_button['state'] = NORMAL 
            self.Auto_inter_button['state'] = NORMAL 


            # Creating to execute the commands  

            cursor = con.cursor()

            # Executing the SQL commands in the parenthese 

            cursor.execute("SELECT * FROM job_app")

            # Fetching the data from the Job application table 

            rows = cursor.fetchall() 

            # Defining the column headers of the Job application table 

            ja_column_headers=['Job number',
                        'Date',
                        'Company',
                        'Job_title',
                        'Location',
                        'Salary',
                        'Aptitude_testing',
                        'Automated_interview',
                        'Technical_interview',
                        'HR_interview',
                        'Job_Offer']

            # Creating a list from numbers corresponding to the column headers starting from 1 

            column_amount= tuple([i for i in range(1,len(ja_column_headers)+1)])

            # Creating a frame to place the Job application table in 

            self.master_frame_enter = tk.LabelFrame(self.master,text= "Job applications table")
            self.master_frame_enter.grid(row=1,rowspan=3 ,column=3,columnspan=3) # Defining the position of the frame on the window  
            
            # Creating another frame to place the job application table in  

            frame2 = tk.Frame(self.master_frame_enter)
            frame2.grid(row=3, column=0, sticky=tk.NW) # Definging the position of the the frame within the master frame
            
            # Creating a canvas to place the Job application table on 

            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3) # Defining the postion of the canvas within the frame2
            
            # Creating a vertical scrollbar linked to the canvas

            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=3,sticky=tk.NS) # Defining the postion of the y scrollbar on the frame2 
            canvas.configure(yscrollcommand=vsbar.set) # Setting the command for the y scrollbar

            # Creating a horizontal scrollbar linked to the canvas

            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW) # Defining the postion of the x scrollbar
            canvas.configure(xscrollcommand=hsbar.set) # Setting the commands for the x scrollbar

            # Creating a frame for the Job application table  

            database_frame = tk.Frame(canvas)

            # Creating the table for the job applications table 

            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3) # Defining the postion of the table on the database_rrame  
            
            #Defining the sizes of the columns

            wid = 80
            wid2 = 125
            wid3 = 180
            wid4 = 200

            # Setting the width of the columns

            tv.column(1,width = wid,minwidth = wid)
            tv.column(2,width = wid,minwidth = wid)
            tv.column(3,width = wid3,minwidth = wid)
            tv.column(4,width = wid4,minwidth = wid)
            tv.column(5,width = wid,minwidth = wid)
            tv.column(6,width = wid,minwidth = wid)
            tv.column(7,width = wid2,minwidth = wid)
            tv.column(8,width = wid2,minwidth = wid)
            tv.column(9,width = wid2,minwidth = wid)
            tv.column(10,width = wid,minwidth = wid)
            tv.column(11,width = wid,minwidth = wid)

            # Setting the the names of the columns to the table

            tv.heading(1,text=ja_column_headers[0])
            tv.heading(2,text=ja_column_headers[1])
            tv.heading(3,text=ja_column_headers[2])
            tv.heading(4,text=ja_column_headers[3])
            tv.heading(5,text=ja_column_headers[4])
            tv.heading(6,text=ja_column_headers[5])
            tv.heading(7,text=ja_column_headers[6])
            tv.heading(8,text=ja_column_headers[7])
            tv.heading(9,text=ja_column_headers[8])
            tv.heading(10,text=ja_column_headers[9])
            tv.heading(11,text=ja_column_headers[10])

            # Unpacking the data into table

            for i in rows:
                tv.insert('','end',values=i)

            # Checking if the table is empty and returning 1 to prevent error 

            rows_check = rows.copy()

            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)

            # Creating a window to place the database in 

            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            

            # Define the scrollable region as entire canvas with only the desired
            
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return 

        def job_app_table_comm(self):
            
            # Connecting into the jobs server to access the database on mysql

            con=mysql.connect(host="localhost",
                user="root",
                password= self.password_n,
                database="jobs")

            # Creating a cursor to execute commands 

            cursor = con.cursor()

            # Executing the SQL commands in the parenthese

            cursor.execute("SELECT * FROM job_app") 
            
            # Fetching  the data from the Job application table 

            rows = cursor.fetchall() 
            
            # Defining the column headers form the job application table

            ja_column_headers=['Job number',
                        'Date',
                        'Company',
                        'Job_title',
                        'Location',
                        'Salary',
                        'Aptitude_testing',
                        'Automated_interview',
                        'Technical_interview',
                        'HR_interview',
                        'Job_Offer']
            
            # Creating a list from number corresponding to the column headers starting from 1  

            column_amount= tuple([i for i in range(1,len(ja_column_headers)+1)])

            # Creating a frame to place the Job applications table in  

            self.master_frame_jobapp = tk.LabelFrame(self.master,text= "Job applications table")
            self.master_frame_jobapp.grid(row=1,rowspan=3 ,column=3,columnspan=3) # Defining the position of the frame on the window 
            
            # Creating another frame to place the job application table in 

            frame2 = tk.Frame(self.master_frame_jobapp)
            frame2.grid(row=3, column=0, sticky=tk.NW) # Defining the the position of frame within the master frame
            
            # Creating a canvas to place The Job application on 

            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3) # Defining the psotion of the canvas within frame2

            # Creating a vertical scrollbar linked to the canvas

            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview) 
            vsbar.grid(row=0, column=3,sticky=tk.NS) # Defining the postion of the y scrollbar on the frame2
            canvas.configure(yscrollcommand=vsbar.set) # Setting the command for the y scrollbar

            # Creating a horizontal scrollbar linked to the canvas

            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW) # Defining the postion of the x scrollbar on the frame2
            canvas.configure(xscrollcommand=hsbar.set) # Setting the command for the x scrollbar

            # Creating a frame for the Aptitude testing table

            database_frame = tk.Frame(canvas)

            # Creating the table for the Aptitude testings table 

            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3) # Defining the position of the table on the database_frame
            
            # Defining the sizes of the columns

            wid = 80
            wid2 = 125
            wid3 = 180
            wid4 = 200
            
            # Setting the width of the columns

            tv.column(1,width = wid,minwidth = wid)
            tv.column(2,width = wid,minwidth = wid)
            tv.column(3,width = wid3,minwidth = wid)
            tv.column(4,width = wid4,minwidth = wid)
            tv.column(5,width = wid,minwidth = wid)
            tv.column(6,width = wid,minwidth = wid)
            tv.column(7,width = wid2,minwidth = wid)
            tv.column(8,width = wid2,minwidth = wid)
            tv.column(9,width = wid2,minwidth = wid)
            tv.column(10,width = wid,minwidth = wid)
            tv.column(11,width = wid,minwidth = wid)

            # Setting the the names of the columns to the table

            tv.heading(1,text=ja_column_headers[0])
            tv.heading(2,text=ja_column_headers[1])
            tv.heading(3,text=ja_column_headers[2])
            tv.heading(4,text=ja_column_headers[3])
            tv.heading(5,text=ja_column_headers[4])
            tv.heading(6,text=ja_column_headers[5])
            tv.heading(7,text=ja_column_headers[6])
            tv.heading(8,text=ja_column_headers[7])
            tv.heading(9,text=ja_column_headers[8])
            tv.heading(10,text=ja_column_headers[9])
            tv.heading(11,text=ja_column_headers[10])

            # Unpacking the data into table

            for i in rows:
                tv.insert('','end',values=i)
            
            # Checking if the table is empty and returning 1 to prevent error 
            
            rows_check = rows.copy()

            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)
            
            # Creating a window to place the database in

            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            
            # Define the scrollable region as entire canvas with only the desired
            
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return

        def AP_test_table_comm(self):
            
            # Connecting into the jobs server to access the database on mysql
            
            con=mysql.connect(host="localhost",
                user="root",
                password= self.password_n,
                database="jobs")

            # Creating a cursor to execute commands 

            cursor = con.cursor()

            # Executing the SQL commands in the parenthese

            cursor.execute("SELECT * FROM AP_testing") 

            # Fetching  the data from the Aptitude testing table 

            rows = cursor.fetchall() 
            
            # Defining the column headers form the Aptitude testing table

            ap_column_headers=['Job_number',
            'Date',
            'Company',
            'Job_title',
            'Deadline',
            'Numerical_reasoning',
            'Verbal_reasoning',
            'Inductive_reasoning',
            'Deductive_reasoning',
            'Situational_Judgement_test',
            'Work_Behaviour_assessment',
            'Reading_Comprehesion_test',
            'Completion'
            ]

            # Creating a list from number corresponding to the column headers starting from 1

            column_amount= tuple([i for i in range(1,len(ap_column_headers)+1)])

            # Creating a frame to place the Job applications table in

            self.master_frame_aptest = tk.LabelFrame(self.master,text= "Aptitude testing table")
            self.master_frame_aptest.grid(row=1,rowspan=3 ,column=3,columnspan=3) # Defining the position of the frame on the window

            # Creating another frame to place the job application table in 

            frame2 = tk.Frame(self.master_frame_aptest)
            frame2.grid(row=3, column=0, sticky=tk.NW) # Defining the the position of frame within the master frame

            # Defining the psotion of the canvas within frame2
            
            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3) # Defining the psotion of the canvas within frame2
            
            # Creating a vertical scrollbar linked to the canvas

            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=3,sticky=tk.NS) # Defining the postion of the y scrollbar on the frame2
            canvas.configure(yscrollcommand=vsbar.set) # Setting the command for the y scrollbar

            # Creating a horizontal scrollbar linked to the canvas

            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW) # Defining the postion of the x scrollbar on the frame2
            canvas.configure(xscrollcommand=hsbar.set) # Setting the command for the x scrollbar

            # Creating a frame for the Job application table

            database_frame = tk.Frame(canvas)

            # Creating the table for the job applications table

            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3) # Defining the postion of the table on the database_frame

            # Defining the sizes of the columns
            
            wid = 80
            wid2 = 100
            wid3 = 180
            wid4 = 200

            # Setting the width of the columns
            
            tv.column(1,width = wid,minwidth = wid)
            tv.column(2,width = wid,minwidth = wid)
            tv.column(3,width = wid,minwidth = wid)
            tv.column(4,width = wid,minwidth = wid)
            tv.column(5,width = wid3,minwidth = wid)
            tv.column(6,width = wid3,minwidth = wid)
            tv.column(7,width = wid3,minwidth = wid)
            tv.column(8,width = wid3,minwidth = wid)
            tv.column(9,width = wid3,minwidth = wid)
            tv.column(10,width = wid3,minwidth = wid)
            tv.column(11,width = wid3,minwidth = wid)
            tv.column(12,width = wid3,minwidth = wid)
            tv.column(13,width = wid2,minwidth = wid)

            # Setting the the names of the columns to the table
            
            tv.heading(1,text=ap_column_headers[0])
            tv.heading(2,text=ap_column_headers[1])
            tv.heading(3,text=ap_column_headers[2])
            tv.heading(4,text=ap_column_headers[3])
            tv.heading(5,text=ap_column_headers[4])
            tv.heading(6,text=ap_column_headers[5])
            tv.heading(7,text=ap_column_headers[6])
            tv.heading(8,text=ap_column_headers[7])
            tv.heading(9,text=ap_column_headers[8])
            tv.heading(10,text=ap_column_headers[9])
            tv.heading(11,text=ap_column_headers[10])
            tv.heading(12,text=ap_column_headers[11])
            tv.heading(13,text=ap_column_headers[12])

            # Unpacking the data into table

            for i in rows:
                tv.insert('','end',values=i)
            
            # Checking if the table is empty and returning 1 to prevent error 

            rows_check = rows.copy()

            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)
            
            # Creating a window to place the database in

            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.

            # Define the scrollable region as entire canvas with only the desired
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return         

        def Auto_inter_table_comm(self):
            
            # Connecting into the jobs server to access the database on mysql
            
            con=mysql.connect(host="localhost",
                user="root",
                password= self.password_n,
                database="jobs")

            # Creating a cursor to execute commands

            cursor = con.cursor()

            # Executing the SQL commands in the parenthese

            cursor.execute("SELECT * FROM Auto_interview") 

            # Fetching  the data from the Aptitude testing table 
            
            rows = cursor.fetchall() 

            # Defining the column headers form the Automated interview table

            ai_column_headers=['Job number',
            'Date',
            'Company',
            'Job_title',
            'Deadline',
            'Completion'
            ]

            # Creating a list from number corresponding to the column headers starting from 1

            column_amount= tuple([i for i in range(1,len(ai_column_headers)+1)])

            # Creating a frame to place the Automated interview table in

            self.master_frame_aptest = tk.LabelFrame(self.master,text= "Automated interview table")
            self.master_frame_aptest.grid(row=1,rowspan=3 ,column=3,columnspan=3) # Defining the position of the frame on the window

            # Creating another frame to place the job application table in 

            frame2 = tk.Frame(self.master_frame_aptest)
            frame2.grid(row=3, column=0, sticky=tk.NW)
            
            # Defining the psotion of the canvas within frame2

            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3)

            # Creating a vertical scrollbar linked to the canvas

            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=3,sticky=tk.NS)  # Defining the postion of the y scrollbar on the frame2
            canvas.configure(yscrollcommand=vsbar.set)  # Setting the command for the y scrollbar

            # Creating a horizontal scrollbar linked to the canvas

            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW)  # Defining the postion of the x scrollbar on the frame2
            canvas.configure(xscrollcommand=hsbar.set)  # Setting the command for the x scrollbar

            # Creating a frame for the Job application table

            database_frame = tk.Frame(canvas)

            # Creating the table for the job applications table

            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3)

            # Defining the sizes of the columns
            
            wid = 120

            # Setting the width of the columns

            tv.column(1,width = wid,minwidth = wid)
            tv.column(2,width = wid,minwidth = wid)
            tv.column(3,width = wid,minwidth = wid)
            tv.column(4,width = wid,minwidth = wid)
            tv.column(5,width = wid,minwidth = wid)
            tv.column(6,width = wid,minwidth = wid)

            # Setting the the names of the columns to the table

            tv.heading(1,text=ai_column_headers[0])
            tv.heading(2,text=ai_column_headers[1])
            tv.heading(3,text=ai_column_headers[2])
            tv.heading(4,text=ai_column_headers[3])
            tv.heading(5,text=ai_column_headers[4])
            tv.heading(6,text=ai_column_headers[5])

            # Unpacking the data into table

            for i in rows:
                tv.insert('','end',values=i)

            # Checking if the table is empty and returning 1 to prevent error
            
            rows_check = rows.copy()
            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)
            
            # Creating a window to place the database in

            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            

            # Define the scrollable region as entire canvas with only the desired
            
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return         



        


#----------------------------------------

# Running the Job application database    

#----------------------------------------

root = Tk()
my_gui = JobApplicationDatabase(root)
root.mainloop()
