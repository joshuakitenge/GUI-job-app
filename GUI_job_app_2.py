from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from delete_entry import Delete_Entry
from new_entry import New_Entry
from update_entry import Update_Entry


class JobApplicationDatabase:
        def __init__(self,master):
            self.master = master
            master.title("Job applications database")
            master.geometry("900x500")
            master.iconbitmap('images/database.ico')



            #New_Entry(Toplevel()
            self.Entry_button = Button(master,text="New Entry",command=lambda :New_Entry(Toplevel(),self.con),padx=100,pady=60,state=DISABLED)
            self.Entry_button.grid(row=2,column=0,columnspan=3)

            # Update entry (Job application) button 
            self.Update_button = Button(master,text="Update", command =lambda : Update_Entry(Toplevel(),self.con),padx=108.4,pady=60,state=DISABLED ) 
            self.Update_button.grid(row=3,column=0,columnspan=3)

            # Delete current entry (Job application) button
            
            self.Delete_button = Button(master,text="Delete",command= lambda: Delete_Entry(Toplevel(),self.con),padx=110.5,pady=60,state=DISABLED)
            self.Delete_button.grid(row=4,column=0,columnspan=3)

            self.job_app_button = Button(master,text="Job application table",command =self.job_app_table_comm,padx=45,pady=60,state=DISABLED )
            self.job_app_button.grid(row=4,column=3)

            self.AP_test_button = Button(master,text="Aptitude testing table",command =self.AP_test_table_comm, padx=42.5,pady=60,state=DISABLED )
            self.AP_test_button.grid(row=4,column=4)

            self.Auto_inter_button = Button(master,text="Automated interview table",command =self.Auto_inter_table_comm,padx=29.5,pady=60,state=DISABLED )
            self.Auto_inter_button.grid(row=4,column=5)

            
            # Creating entry for password 

            self.password = Label(master,text ="Password")
            self.password.grid(row=0,column=0,sticky=W)
            
            self.password_entry = Entry(master,width=20)
            self.password_entry.grid(row=0,column=1,sticky=W,pady=10)
            self.password_entry.insert(0,"Enter password")

            self.password_button = Button(master,text="Enter",command = self.password_entry_2)
            self.password_button.grid(row=0,column=2)
            # button to switch tables 



            

        def password_entry_2(self):
            self.password_n = self.password_entry.get()
            #self.password = password

            con=mysql.connect(host="localhost",
                    user="root",
                    password= self.password_n,
                    database="jobs")

            self.con = con

            self.cur = con.cursor()

            self.password_lab = Label(self.master,text="Password entered succesfully")
            self.password_lab.grid(row=1,column=0, columnspan=3)
            self.password_entry.delete(0,END)
            self.Delete_button['state'] = NORMAL
            self.Entry_button['state'] = NORMAL
            self.Update_button['state'] = NORMAL 
            self.job_app_button['state'] = NORMAL 
            self.AP_test_button['state'] = NORMAL 
            self.Auto_inter_button['state'] = NORMAL 




            cursor = con.cursor()

            cursor.execute("SELECT * FROM job_app") 
            #print('''Result of "SELECT * FROM student":''')
            rows = cursor.fetchall() 
            #for r in result:
                #print(r[0])

            #cursor.close()
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


            column_amount= tuple([i for i in range(1,12)])



            #my_label = Label(root,text="HI there is pizza here").grid(row = 0 ,column = 0)
            self.master_frame_enter = tk.LabelFrame(self.master,text= "Job applications table")
            self.master_frame_enter.grid(row=1,rowspan=3 ,column=3,columnspan=3)#sticky=tk.NSEW)
            #master_frame.columnconfigure(0, weight=1)

            # tables buttons 



            frame2 = tk.Frame(self.master_frame_enter)
            frame2.grid(row=3, column=0, sticky=tk.NW)
            

            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3)
            


            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=3,sticky=tk.NS)
            canvas.configure(yscrollcommand=vsbar.set)

            # Create a horizontal scrollbar linked to the canvas.
            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW)
            canvas.configure(xscrollcommand=hsbar.set)

            database_frame = tk.Frame(canvas)


            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3)
            #tv.place(x=0,y=0)

            #vert= Scale(root,from_=0,to=len(rows[0:]))
            #vert.grid(row= 0, column=0)

            #for i in range(len(ja_column_headers)-1):
            wid = 80
            wid2 = 125
            wid3 = 180
            wid4 = 200
            #widm=100
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



            for i in rows:
                tv.insert('','end',values=i)
            

            ROWS_DISP = 13  
            COLS_DISP = 6

            rows_check = rows.copy()
            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)

            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            #print('canvas.bbox(tk.ALL): {}'.format(bbox))

            # Define the scrollable region as entire canvas with only the desired
            # number of rows and columns displayed.
            w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
            dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return 

        def job_app_table_comm(self):
            
            con=mysql.connect(host="localhost",
                user="root",
                password= self.password_n,
                database="jobs")


            cursor = con.cursor()

            cursor.execute("SELECT * FROM job_app") 
            #print('''Result of "SELECT * FROM student":''')
            rows = cursor.fetchall() 
            #for r in result:
                #print(r[0])

            #cursor.close()
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


            column_amount= tuple([i for i in range(1,12)])



            #my_label = Label(root,text="HI there is pizza here").grid(row = 0 ,column = 0)
            self.master_frame_jobapp = tk.LabelFrame(self.master,text= "Job applications table")
            self.master_frame_jobapp.grid(row=1,rowspan=3 ,column=3,columnspan=3)#sticky=tk.NSEW)
            #master_frame.columnconfigure(0, weight=1)

            # tables buttons 



            frame2 = tk.Frame(self.master_frame_jobapp)
            frame2.grid(row=3, column=0, sticky=tk.NW)
            

            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3)
            


            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=3,sticky=tk.NS)
            canvas.configure(yscrollcommand=vsbar.set)

            # Create a horizontal scrollbar linked to the canvas.
            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW)
            canvas.configure(xscrollcommand=hsbar.set)

            database_frame = tk.Frame(canvas)


            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3)
            #tv.place(x=0,y=0)

            #vert= Scale(root,from_=0,to=len(rows[0:]))
            #vert.grid(row= 0, column=0)

            #for i in range(len(ja_column_headers)-1):
            wid = 80
            wid2 = 125
            wid3 = 180
            wid4 = 200
            #widm=100
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



            for i in rows:
                tv.insert('','end',values=i)
            

            ROWS_DISP = 13  
            COLS_DISP = 6
            rows_check = rows.copy()
            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)
            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            #print('canvas.bbox(tk.ALL): {}'.format(bbox))

            # Define the scrollable region as entire canvas with only the desired
            # number of rows and columns displayed.
            w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
            dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return

        def AP_test_table_comm(self):
            
            
            con=mysql.connect(host="localhost",
                user="root",
                password= self.password_n,
                database="jobs")


            cursor = con.cursor()

            cursor.execute("SELECT * FROM AP_testing") 
            
            rows = cursor.fetchall() 
            #for r in result:
                #print(r[0])

            #cursor.close()
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


            column_amount= tuple([i for i in range(1,14)])



            #my_label = Label(root,text="HI there is pizza here").grid(row = 0 ,column = 0)
            self.master_frame_aptest = tk.LabelFrame(self.master,text= "Aptitude testing table")
            self.master_frame_aptest.grid(row=1,rowspan=3 ,column=3,columnspan=3)#sticky=tk.NSEW)
            #master_frame.columnconfigure(0, weight=1)

            # tables buttons 



            frame2 = tk.Frame(self.master_frame_aptest)
            frame2.grid(row=3, column=0, sticky=tk.NW)
            

            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3)
            


            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=3,sticky=tk.NS)
            canvas.configure(yscrollcommand=vsbar.set)

            # Create a horizontal scrollbar linked to the canvas.
            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW)
            canvas.configure(xscrollcommand=hsbar.set)

            database_frame = tk.Frame(canvas)


            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3)
            #tv.place(x=0,y=0)

            #vert= Scale(root,from_=0,to=len(rows[0:]))
            #vert.grid(row= 0, column=0)

            #for i in range(len(ja_column_headers)-1):
            wid = 80
            wid2 = 125
            wid3 = 180
            wid4 = 200
            #widm=100
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
            tv.column(12,width = wid,minwidth = wid)
            tv.column(13,width = wid,minwidth = wid)
            #tv.column(14,width = wid,minwidth = wid)


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
            #tv.heading(14,text=ap_column_headers[13])



            for i in rows:
                tv.insert('','end',values=i)
            

            ROWS_DISP = 9  
            COLS_DISP = 6

            rows_check = rows.copy()
            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)

            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            #print('canvas.bbox(tk.ALL): {}'.format(bbox))

            # Define the scrollable region as entire canvas with only the desired
            # number of rows and columns displayed.
            w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
            dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return         

        def Auto_inter_table_comm(self):
            
            
            con=mysql.connect(host="localhost",
                user="root",
                password= self.password_n,
                database="jobs")


            cursor = con.cursor()

            cursor.execute("SELECT * FROM Auto_interview") 
            
            rows = cursor.fetchall() 
            rows_check = rows.copy()
            if len(rows_check) == 0:
                COLS = 1
                ROWS = 1
            else:
                COLS = len(rows[0])
                ROWS = len(rows)
            #for r in result:
                #print(r[0])

            #cursor.close()
            ai_column_headers=['Job number',
            'Date',
            'Company',
            'Job_title',
            'Deadline',
            'Completion'
            ]


            column_amount= tuple([i for i in range(1,7)])



            #my_label = Label(root,text="HI there is pizza here").grid(row = 0 ,column = 0)
            self.master_frame_aptest = tk.LabelFrame(self.master,text= "Automated interview table")
            self.master_frame_aptest.grid(row=1,rowspan=3 ,column=3,columnspan=3)#sticky=tk.NSEW)
            #master_frame.columnconfigure(0, weight=1)

            # tables buttons 



            frame2 = tk.Frame(self.master_frame_aptest)
            frame2.grid(row=3, column=0, sticky=tk.NW)
            

            canvas = tk.Canvas(frame2)
            canvas.grid(row=0, column=0,columnspan=3)
            


            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=3,sticky=tk.NS)
            canvas.configure(yscrollcommand=vsbar.set)

            # Create a horizontal scrollbar linked to the canvas.
            hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
            hsbar.grid(row=1, column=0, columnspan=3,sticky=tk.EW)
            canvas.configure(xscrollcommand=hsbar.set)

            database_frame = tk.Frame(canvas)


            tv= ttk.Treeview(database_frame,columns=column_amount, show="headings",height=str(len(rows)))
            tv.grid(row=0,column=0,columnspan=3)
            #tv.place(x=0,y=0)

            #vert= Scale(root,from_=0,to=len(rows[0:]))
            #vert.grid(row= 0, column=0)

            #for i in range(len(ja_column_headers)-1):
            wid = 80
            wid2 = 125
            wid3 = 180
            wid4 = 200
            #widm=100
            tv.column(1,width = wid,minwidth = wid)
            tv.column(2,width = wid,minwidth = wid)
            tv.column(3,width = wid3,minwidth = wid)
            tv.column(4,width = wid4,minwidth = wid)
            tv.column(5,width = wid,minwidth = wid)
            tv.column(6,width = wid,minwidth = wid)

            #tv.column(14,width = wid,minwidth = wid)


            tv.heading(1,text=ai_column_headers[0])
            tv.heading(2,text=ai_column_headers[1])
            tv.heading(3,text=ai_column_headers[2])
            tv.heading(4,text=ai_column_headers[3])
            tv.heading(5,text=ai_column_headers[4])
            tv.heading(6,text=ai_column_headers[5])



            for i in rows:
                tv.insert('','end',values=i)
            

            ROWS_DISP = 6  
            COLS_DISP = 6
            #COLS = len(rows[0])
            #ROWS = len(rows)

            canvas.create_window((0,0), window=database_frame, anchor=tk.NW)

            database_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            #print('canvas.bbox(tk.ALL): {}'.format(bbox))

            # Define the scrollable region as entire canvas with only the desired
            # number of rows and columns displayed.
            w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
            dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
            canvas.configure(scrollregion=bbox, width=600, height=250)           
            
            return         



        


#-------------------------------------------------------------------------------------------------------------------    


root = Tk()
my_gui = JobApplicationDatabase(root)
root.mainloop()