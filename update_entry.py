from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

from update_entry_tables import Update_tables

class Update_Entry:
    def __init__(self,new_window,con):
            self.new_window = new_window
            self.con = con
            new_window.iconbitmap('images/database.ico')
            new_window.title('Update entry')
            new_window.geometry("265x405") 

            #---------------------------------------------------------------------------------------------
            # job application

            self.ja_column_headers=['Job number',
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
            self.ja_type_input=['Enter job number',
            'Enter date e.g. year/month/day',
            'Enter company name',
            'Enter job title',
            'Job location',
            'Enter salary in £',
            'Enter due date for aptitude test(s) e.g year/month/day',
            'Enter due date for automated interview e.g year/month/day',
            'Enter date for technical interview e.g year/month/day',
            'Enter date for HR interview e.g year/month/day',
            'Enter current job status'
            ]
            #---------------------------------------------------------------------------------------------
            # Aptitdue testing
            self.ap_column_headers=['Job_number',
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
            self.ap_type_input=['Enter job number',
            'Enter date e.g year/month/day ',
            'Enter Company name',
            'Enter job title',
            'Enter deadline date e.g year/month/day',
            'Enter YES if completed, otherwise NO',
            'Enter YES if completed, otherwise NO',
            'Enter YES if completed, otherwise NO',
            'Enter YES if completed, otherwise NO',
            'Enter YES if completed, otherwise NO',
            'Enter YES if completed, otherwise NO',
            'Enter YES if completed, otherwise NO',
            'Enter YES if completed, otherwise NO',
            ]
            #---------------------------------------------------------------------------------------------
            # Automated interview
            self.ai_column_headers=['Job number',
            'Date',
            'Company',
            'Job_title',
            'Deadline',
            'Completion'
            ]

            self.ai_type_input= ['Enter job number',
            'Enter date e.g year/month/day ',
            'Enter Company name',
            'Enter job title',
            'Enter deadline date e.g year/month/day',
            'Enter YES if completed, otherwise NO'
            ]
            #---------------------------------------------------------------------------------------------



            #New_Entry(Toplevel()
            self.job_app_button = Button(new_window,text="Job application table",command= lambda: Update_tables(Toplevel(),self.con,self.ja_column_headers,self.ja_type_input,'job_app','Job application'),padx=72.5,pady=50)
            self.job_app_button.grid(row=0,column=0)

            # Update entry (Job application) button 
            self.Ap_testing_button = Button(new_window,text="Aptitude testing table", command = lambda: Update_tables(Toplevel(),self.con,self.ap_column_headers,self.ap_type_input,'AP_testing','Aptitude testing'),padx=70,pady=50 ) 
            self.Ap_testing_button.grid(row=1,column=0)

            # Delete current entry (Job application) button
            
            self.Auto_interview_button = Button(new_window,text="Automated interview table",command = lambda: Update_tables(Toplevel(),self.con,self.ai_column_headers,self.ai_type_input,'Auto_interview','Automated interview') ,padx=57,pady=50)
            self.Auto_interview_button.grid(row=2,column=0)

            self.upd_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
            self.upd_btn_close_win.grid(row=3,column=0,sticky=W)

    #def jobapp(self):
        #return
    #def aptest(self):
        #return
    #def autointer(self):
        #return
