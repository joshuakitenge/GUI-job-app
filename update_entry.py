"""
Title: Job application data -> Update entry 

Author: Joshua Kitenge

"""

# Imports 

from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from update_entry_tables import Update_tables

#  The update entry class 

class Update_Entry:
    def __init__(self,new_window,con):
            self.new_window = new_window # Creating a new window - using Toplevel() in GUI_job_app_2
            self.con = con # Defining the Conection to the jobs database on my sql
            new_window.iconbitmap('images/database.ico') # Setting the new logo to the window
            new_window.title('Update entry') # Setting the title for the new window
            new_window.geometry("265x405") # The size if the new window 

            # The column headers for the Job applications table 

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

            # The types of input to put inside the entry boxes for the Job application table

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
           
            # The column headers for the Aptitdue testing table 
            
            self.ap_column_headers=['Job_number',
            'Date',
            'Company',
            'Job_title',
            'Deadline',
            'Numerical_reasoning',
            'Verbal_reasoning',
            'Inductive_reasoning',
            'Deductive_reasoning',
            'Situation_Judgement_test',
            'Work_Behaviour_assessment',
            'Reading_Comprehesion_test',
            'Completion'
            ]

            # The types of input to put inside the entry boxes in the Aptitude testing table

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
            
            # The column headers for the Automated interview table
            
            self.ai_column_headers=['Job number',
            'Date',
            'Company',
            'Job_title',
            'Deadline',
            'Completion'
            ]

            # The types of input to put inside the entry boxes in the Automated interview table 

            self.ai_type_input= ['Enter job number',
            'Enter date e.g year/month/day ',
            'Enter Company name',
            'Enter job title',
            'Enter deadline date e.g year/month/day',
            'Enter YES if completed, otherwise NO'
            ]
            
            #Update entry (Job application) button

            self.job_app_button = Button(new_window,text="Job application table",command= lambda: Update_tables(Toplevel(),self.con,self.ja_column_headers,self.ja_type_input,'job_app','Job application'),padx=72.5,pady=50)
            self.job_app_button.grid(row=0,column=0) # Defining the postion of the button on the window 

            # Update entry (Aptitude testing) button
             
            self.Ap_testing_button = Button(new_window,text="Aptitude testing table", command = lambda: Update_tables(Toplevel(),self.con,self.ap_column_headers,self.ap_type_input,'AP_testing','Aptitude testing'),padx=70,pady=50 ) 
            self.Ap_testing_button.grid(row=1,column=0) # Defining the postion of the button on the window 

            # Update entry (Automated interview) button
            
            self.Auto_interview_button = Button(new_window,text="Automated interview table",command = lambda: Update_tables(Toplevel(),self.con,self.ai_column_headers,self.ai_type_input,'Auto_interview','Automated interview') ,padx=57,pady=50)
            self.Auto_interview_button.grid(row=2,column=0) # Defining the postion of the button on the window 
            
            # Close window button 
            
            self.upd_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
            self.upd_btn_close_win.grid(row=3,column=0,sticky=W) # Defining the postion of the button on the window 

 
