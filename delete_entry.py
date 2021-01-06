from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql



class Delete_Entry:
        def __init__(self,new_window,con):
            self.new_window = new_window
            self.con = con
            new_window.iconbitmap('images/database.ico')
            new_window.title('Delete entry')
            new_window.geometry("250x100")


            self.job_number = Label(new_window,text='Job number')
            self.job_number.grid(row=0,column=0,sticky=W)

            self.cur = con.cursor()
            
            #------------------------------------------------------------------------------------------------

            self.job_num_entry = Entry(new_window,width=20)
            #self.job_num_entry = job_num_entry

            self.job_num_entry.grid(row=0,column=1)
            self.job_num_entry.insert(0,'Enter job number')

            self.del_btn_enter = Button(new_window,text="Enter", command=self.Delete_job)
            self.del_btn_enter.grid(row=2,column=1,sticky=E)
            self.del_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
            self.del_btn_close_win.grid(row=2,column=0,sticky=W)
        
        
#
        def Delete_job(self):

            job_number = self.job_num_entry.get() 

            query_delete = "DELETE FROM job_app WHERE job_number = '{}'".format(job_number)

            self.cur.execute(query_delete)

            self.con.commit()
            self.con.close()

            self.deleted = Label(self.new_window,text="Row deleted succesfully")
            self.deleted.grid(row=1,column=0, columnspan=2)


