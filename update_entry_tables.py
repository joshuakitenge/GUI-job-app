"""
Title: Job application data -> Update entry -> Update entey in tables 

Author: Joshua Kitenge

"""
# Imports

from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

# Update tables class

class Update_tables:
    def __init__ (self,new_window,con,column_headers,type_input,table_name,table_title_name):
        self.new_window = new_window # Creating a new window - using Toplevel() in Update_entry
        self.con = con # Defining the Conection to the jobs database on my sql
        self.column_headers = column_headers # Defining the instance of the column headers of the tables within the class 
        self.type_input = type_input # Defining the instance of the types of input for the column headers entry boxes within the class
        self.table_name = table_name # The table names as written on jobs database 
        self.table_title_name = table_title_name # The table names for the name of the window 

        new_window.iconbitmap('images/database.ico') # Setting the new logo to the window
        new_window.title('Update entry: {}'.format(table_title_name)) # Setting the title for the new window
        new_window.geometry("570x405") # The size if the new window

        # Creating a cursor to execute sql commands

        self.cur = con.cursor()

        # Defining the width size of the entry boxes 

        self.width_size = 60

        # Creating the label for the job number 
         
        self.job_number = Label(new_window,text=self.column_headers[0])
        self.job_number.grid(row=0,column=0,sticky=W) # Defining the postion of label on the window 

        # Creating the entry box for job number 

        self.job_num_entry = Entry(new_window,width= self.width_size)
        self.job_num_entry.grid(row=0,column=1,sticky=W,columnspan=2,pady=10) # Defining the position of the entry box on the window 
        self.job_num_entry.insert(0,self.type_input[0]) # Setting the type of input to input into entry box  

        # Creating a drop down menu

        self.clicked=StringVar()  # Defining primative type of the variable selected
        self.clicked.set(self.column_headers[1:][0]) # Setting an intial variable to be in the drop down menu
        self.drop_jobapp = OptionMenu(new_window, self.clicked,*self.column_headers[1:])
        self.drop_jobapp.grid(row=2,column=0,sticky=W,pady=10) # Defining the postion of drop down menu on the window

        # This button updates the label and entry box to the one selected in the drop down menu 

        self.update_input_varaible_button = Button(new_window,text="Update input variable", command = self.update_input_varaible_show)
        self.update_input_varaible_button.grid(row=2,column=1,columnspan=2) # Defining the postion of button on the window

        # This button refreshes the label and entry box once command has been committed
     
        self.update_del_input_varaible_button = Button(new_window,text="Refresh", command = self.update_input_varaible_del)
        self.update_del_input_varaible_button.grid(row=5,column=1) # Defining the postion of button on the window

        # This button commits the enter into the jobs database table
      
        self.upd_btn_enter = Button(new_window,text="Enter", command= self.Enter_update)
        self.upd_btn_enter.grid(row=5,column=2,sticky=E) # Defining the postion of button on the window

        # This button closes the window 
        
        self.upd_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
        self.upd_btn_close_win.grid(row=5,column=0,sticky=W) # Defining the postion of button on the window
    
    #-------------------------------------------

    # Creating the commmand to update the 
    # label and entry box once update button is 
    # pressed.
     
    #-------------------------------------------

    def update_input_varaible_show(self):
        
        # Getting the selected drop down menu table
         
        column_head = self.clicked.get()

        # Creating the label using the string from the drop down menu

        self.updated_label = Label(self.new_window,text = column_head)
        self.updated_label.grid(row=3,column=0,sticky=W) # Defining the postion of label on the window

        # Creating the entry box for the new label  

        self.updated_entry = Entry(self.new_window,width= self.width_size)
        self.updated_entry.grid(row=3,column=1,sticky=W,pady=10) # Defining the postion of entry box on the window
        self.updated_entry.insert(0,self.type_input[self.column_headers.index(column_head)]) # Setting the type of input in the entry box for the new label
        self.update_input_varaible_button['state'] = DISABLED # Deactivating the update button once label and entry box is updated  
    
    #---------------------------------------------

    # Creating the command for the refresh button
    # to destroy the label , entry box and the 
    # completion message 
 
    #---------------------------------------------

    def update_input_varaible_del(self):
        
        # Destroying the entry box 

        self.updated_entry.destroy()

        # Destroying the label 

        self.updated_label.destroy()

        # Destroying completion message
         
        self.entered.destroy()
        
        # Reactivating the update button 

        self.update_input_varaible_button['state'] = NORMAL

    #--------

    # Creating the command for the enter button
    # to commit the job.  

    #--------

    def Enter_update(self):
        
        # Getting the column header from the drop down menu 

        column_head = self.clicked.get()

        # Getting the job nummber from the entry box   

        job_number = self.job_num_entry.get()

        # Getting the entry that was updated 

        updated_entry = self.updated_entry.get()

        # Defining the table names as written on the jobs database

        table_name = self.table_name

        # Defining the table names (nicer format)
     
        table_title_name = self.table_title_name

        # Creating the query using updated parameters

        query = "UPDATE {} SET {} = '{}' WHERE Job_number='{}'".format(table_name,column_head,updated_entry,job_number)

        # Executing the query 

        self.cur.execute(query)
        
        # Commiting the query 
         
        self.con.commit()

        # Creating label with a completion message 

        self.entered = Label(self.new_window,text="Job application {} succesfully updated {} in {} table".format(job_number,column_head,table_title_name),pady=10)
        self.entered.grid(row=4,column=0, columnspan=3) # Defining the position of the label on the window  

