"""
Title: Job application data -> Deleting an entry 

Author: Joshua Kitenge

"""

 # Imports
from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

# The Delete entry class 

class Delete_Entry:
        def __init__(self,new_window,con):
            self.new_window = new_window  # Creating a new window - using Toplevel() in GUI_job_app_2
            self.con = con  # Defining the Conection to the jobs database on my sql 
            new_window.iconbitmap('images/database.ico') # Setting the new logo to the window 
            new_window.title('Delete entry') # Setting the title for the new window  
            new_window.geometry("250x100") # The size if the new window 

            
            # Creating a cursor to execute sql commands
             
            self.cur = con.cursor()

            #-----------------------------------------

            # Creating the interface to delete entries 

            #-----------------------------------------

            # Creating the label for job number
             
            self.job_number = Label(new_window,text='Job number')
            self.job_number.grid(row=0,column=0,sticky=W) # Defining the position of the label on the window  
            
            # Creating the entry box for the job number 

            self.job_num_entry = Entry(new_window,width=20)
            self.job_num_entry.grid(row=0,column=1) # Defining the position of the entry box on window 
            self.job_num_entry.insert(0,'Enter job number') # Entry box message within box 

            # Creating the Enter button 

            self.del_btn_enter = Button(new_window,text="Enter", command=self.Delete_job)
            self.del_btn_enter.grid(row=2,column=1,sticky=E) #  Defining the position of the enter button 

            # Creating the close window button 

            self.del_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
            self.del_btn_close_win.grid(row=2,column=0,sticky=W) # Defining the position of the close window button 
        
        #----------------------------------------------

        # Creating the command for enter to delete entry
         
        #----------------------------------------------
        
        def Delete_job(self):
            
            # Getting the job number enter in entry box 

            job_number = self.job_num_entry.get()

            # Querying the job number to delete job application on mysql from job database -  
            # Deleted in all tables : "ON DELETE SET CASCADE"     

            query_delete = "DELETE FROM job_app WHERE job_number = '{}'".format(job_number)

            # Executing the delete command

            self.cur.execute(query_delete)

            # Commiting the delete command to job database 

            self.con.commit()
            
            # Creating the Label when commit is successfully deleted from table    
             
            self.deleted = Label(self.new_window,text="Job number {} succesfully deleted ".format(job_number))
            self.deleted.grid(row=1,column=0, columnspan=2) # Defining the position of the label on the window 

