from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from delete_entry import Delete_Entry
from new_entry import New_Entry
from update_entry import Update_Entry


class JobApplicationDatabase:
        def __init__(self,master):
            self.master = master
            master.title("Job applications database")
            master.geometry("265x450") 



            #New_Entry(Toplevel()
            self.Entry_button = Button(master,text="New Entry",command=lambda :New_Entry(Toplevel(),self.con),padx=100,pady=50,state=DISABLED)
            self.Entry_button.grid(row=2,column=0,columnspan=3)

            # Update entry (Job application) button 
            self.Update_button = Button(master,text="Update", command =lambda : Update_Entry(Toplevel(),self.con),padx=108.4,pady=50,state=DISABLED ) 
            self.Update_button.grid(row=3,column=0,columnspan=3)

            # Delete current entry (Job application) button
            
            self.Delete_button = Button(master,text="Delete",command= lambda: Delete_Entry(Toplevel(),self.con),padx=110.5,pady=50,state=DISABLED)
            self.Delete_button.grid(row=4,column=0,columnspan=3)

            
            # Creating entry for password 

            self.password = Label(master,text ="Password")
            self.password.grid(row=0,column=0,sticky=W)
            
            self.password_entry = Entry(master,width=20)
            self.password_entry.grid(row=0,column=1,sticky=W,pady=10)
            self.password_entry.insert(0,"Enter password")

            self.password_button = Button(master,text="Enter",command = self.password_entry_2)
            self.password_button.grid(row=0,column=2)

        def password_entry_2(self):
            password_n = self.password_entry.get()
            #self.password = password

            con=mysql.connect(host="localhost",
                    user="root",
                    password= password_n,
                    database="jobs")

            self.con = con

            self.cur = con.cursor()

            self.password_lab = Label(self.master,text="Password entered succesfully")
            self.password_lab.grid(row=1,column=0, columnspan=3)
            self.password_entry.delete(0,END)
            self.Delete_button['state'] = NORMAL
            self.Entry_button['state'] = NORMAL
            self.Update_button['state'] = NORMAL
            return 


        


#-------------------------------------------------------------------------------------------------------------------    


root = Tk()
my_gui = JobApplicationDatabase(root)
root.mainloop()