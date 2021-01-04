from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from job_app_update import Job_App_Update
from ap_testing_update import AP_Testing_Update
from auto_interview_update import Auto_Interview_Update

class Update_Entry:
    def __init__(self,new_window,con):
            self.new_window = new_window
            self.con = con
            new_window.iconbitmap('images/database.ico')
            new_window.title('Update entry')
            new_window.geometry("265x405") 

            #New_Entry(Toplevel()
            self.job_app_button = Button(new_window,text="Job application table",command= lambda: Job_App_Update(Toplevel(),self.con),padx=72.5,pady=50)
            self.job_app_button.grid(row=0,column=0)

            # Update entry (Job application) button 
            self.Ap_testing_button = Button(new_window,text="Aptitude testing table", command = lambda: AP_Testing_Update(Toplevel(),self.con),padx=70,pady=50 ) 
            self.Ap_testing_button.grid(row=1,column=0)

            # Delete current entry (Job application) button
            
            self.Auto_interview_button = Button(new_window,text="Automated interview table",command = lambda: Auto_Interview_Update(Toplevel(),self.con) ,padx=57,pady=50)
            self.Auto_interview_button.grid(row=2,column=0)

            self.upd_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
            self.upd_btn_close_win.grid(row=3,column=0,sticky=W)

    #def jobapp(self):
        #return
    #def aptest(self):
        #return
    #def autointer(self):
        #return
