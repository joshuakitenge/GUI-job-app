from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql



class New_Entry:
        def __init__(self,new_window,con):
            self.new_window = new_window
            self.con = con
            new_window.iconbitmap('images/database.ico')
            new_window.title('New entry')
            new_window.geometry("620x360")


            #self.job_number = Label(new_window,text='Job number')
            #self.job_number.grid(row=0,column=0,sticky=W)

            self.cur = con.cursor()
            
            #------------------------------------------------------------------------------------------------
            # The names of the columns on the job application - main table 

            self.column_headers=['Job number',
            'Date',
            'Company name',
            'Job title',
            'Location',
            'Salary'
            ]
            # The types of input to put inside the input box 
            self.type_input=['Enter job number',
            'Enter date e.g. year/month/day',
            'Enter company name',
            'Enter job title',
            'Enter Job location, otherwise enter UK',
            'Enter salary in £, otherwise enter NULL'
            ]
            #--------------------------------------------------------------------------------------------------
            self.tables= ['All tables',
            'Job application table',
            'Aptitude Testing table',
            'Automated interview'
            ]

            self.clicked=StringVar()
            self.clicked.set(self.tables[0])
            self.drop_jobapp = OptionMenu(new_window, self.clicked,*self.tables)
            self.drop_jobapp.grid(row=0,column=0,sticky=W,columnspan=2,pady=10)
            #--------------------------------------------------------------------------------------------------

            # Create the labels for all of the column headers 

            self.job_number = Label(new_window,text=self.column_headers[0])
            self.job_number.grid(row=1,column=0,sticky=W)

            self.date = Label(new_window,text=self.column_headers[1])
            self.date.grid(row=2,column=0,sticky=W)

            self.company = Label(new_window,text = self.column_headers[2])
            self.company.grid(row=3,column=0,sticky=W)

            self.job_title = Label(new_window,text = self.column_headers[3])
            self.job_title.grid(row=4,column=0,sticky=W)

            self.location = Label(new_window,text = self.column_headers[4])
            self.location.grid(row=5,column=0,sticky=W)

            self.salary = Label(new_window,text = self.column_headers[5])
            self.salary.grid(row=6,column=0,sticky=W)

            #------------------------------------------------------------------------------------------------
            # Creating the entry boxes for all the column headers 
            width_size = 80

            self.job_num_entry = Entry(new_window,width= width_size)
            self.job_num_entry.grid(row=1,column=1,sticky=W,pady=10)
            self.job_num_entry.insert(0,self.type_input[0])

            self.date_entry = Entry(new_window,width= width_size)
            self.date_entry.grid(row=2,column=1,sticky=W,pady=10)
            self.date_entry.insert(0,self.type_input[1])

            self.company_entry = Entry(new_window,width = width_size)
            self.company_entry.grid(row=3,column=1,sticky=W,pady=10)
            self.company_entry.insert(0,self.type_input[2])

            self.job_title_entry = Entry(new_window,width= width_size)
            self.job_title_entry.grid(row=4,column=1,sticky=W,pady=10)
            self.job_title_entry.insert(0,self.type_input[3])

            self.location_entry = Entry(new_window,width= width_size)
            self.location_entry.grid(row=5,column=1,sticky=W,pady=10)
            self.location_entry.insert(0,self.type_input[4])

            self.salary_entry = Entry(new_window,width= width_size)
            self.salary_entry.grid(row=6,column=1,sticky=W,pady=10)
            self.salary_entry.insert(0,self.type_input[5])
        

        #------------------------------------------------------------------------------------------------------------
        #Enter button and close window button
            self.new_btn_enter = Button(new_window,text="Enter", command= self.Enter_job)
            self.new_btn_enter.grid(row=8,column=1,sticky=E)
            self.new_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
            self.new_btn_close_win.grid(row=8,column=0,sticky=W)
                
        
#
        def Enter_job(self):
            
            job_number = self.job_num_entry.get()
            date = self.date_entry.get()
            company = self.company_entry.get()
            job_title = self.job_title_entry.get()
            location = self.location_entry.get()
            salary = self.salary_entry.get()
            table_entry = self.clicked.get()
            table = self.tables

            if table[0] == table_entry:
            
                if salary != "NULL":
                    query_entry_jobapp = "INSERT INTO job_app VALUES('{}','{}','{}','{}','{}','{}',NULL,NULL,NULL,NULL,NULL)".format(job_number,date,company,job_title,location,salary)
                else:
                    query_entry_jobapp = "INSERT INTO job_app VALUES('{}','{}','{}','{}','{}',NULL,NULL,NULL,NULL,NULL,NULL)".format(job_number,date,company,job_title,location)

                query_entry_AP_testing = "INSERT INTO AP_testing VALUES( '{}','{}','{}','{}',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)".format(job_number,date,company,job_title)
                query_entry_Auto_interview = "INSERT INTO Auto_interview VALUES( '{}','{}','{}','{}',NULL,NULL)".format(job_number,date,company,job_title)
                self.cur.execute(query_entry_jobapp)
                self.cur.execute(query_entry_AP_testing)
                self.cur.execute(query_entry_Auto_interview)

                self.con.commit()
                self.con.close()

                self.entered = Label(self.new_window,text="Rows entered succesfully in {} tables".format(table_entry))
                self.entered.grid(row=7,column=0, columnspan=2)

            elif table[1] == table_entry:
            
                if salary != "NULL":
                    query_entry_jobapp = "INSERT INTO job_app VALUES('{}','{}','{}','{}','{}','{}',NULL,NULL,NULL,NULL,NULL)".format(job_number,date,company,job_title,location,salary)
                else:
                    query_entry_jobapp = "INSERT INTO job_app VALUES('{}','{}','{}','{}','{}',NULL,NULL,NULL,NULL,NULL,NULL)".format(job_number,date,company,job_title,location)
                self.cur.execute(query_entry_jobapp)

                self.con.commit()
                self.con.close()

                self.entered = Label(self.new_window,text="Rows entered succesfully in {} table".format(table_entry))
                self.entered.grid(row=7,column=0, columnspan=2)
                
            elif table[2] == table_entry:
                query_entry_AP_testing = "INSERT INTO AP_testing VALUES( '{}','{}','{}','{}',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)".format(job_number,date,company,job_title)
                
                self.cur.execute(query_entry_AP_testing)
                
                self.con.commit()
                self.con.close()

                self.entered = Label(self.new_window,text="Rows entered succesfully in {} table".format(table_entry))
                self.entered.grid(row=7,column=0, columnspan=2)
            elif table[3] == table_entry:
                query_entry_Auto_interview = "INSERT INTO Auto_interview VALUES( '{}','{}','{}','{}',NULL,NULL)".format(job_number,date,company,job_title)

                self.cur.execute(query_entry_Auto_interview)

                self.con.commit()
                self.con.close()

                self.entered = Label(self.new_window,text="Rows entered succesfully in {} table".format(table_entry))
                self.entered.grid(row=7,column=0, columnspan=2)
            

