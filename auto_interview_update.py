from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql


class Auto_Interview_Update:
    def __init__ (self,new_window,con):
        self.new_window = new_window
        self.con = con
        new_window.iconbitmap('images/database.ico')
        new_window.title('Update entry: Automated Interview')
        new_window.geometry("550x405")
        self.cur = con.cursor()

        self.column_headers=['Job number',
        'Date',
        'Company',
        'Job_title',
        'Deadline',
        'Completion'
        ]
  
        self.type_input= ['Enter job number',
        'Enter date e.g year/month/day ',
        'Enter Company name',
        'Enter job title',
        'Enter deadline date e.g year/month/day',
        'Enter YES if completed, otherwise NO'
        ]
        self.width_size = 60 
        self.job_number = Label(new_window,text=self.column_headers[0])
        self.job_number.grid(row=0,column=0,sticky=W)

        self.job_num_entry = Entry(new_window,width= self.width_size)
        self.job_num_entry.grid(row=0,column=1,sticky=W,columnspan=2,pady=10)
        self.job_num_entry.insert(0,self.type_input[0])


        self.clicked=StringVar()
        self.clicked.set(self.column_headers[1:][0])
        self.drop_auto_interview = OptionMenu(new_window, self.clicked,*self.column_headers[1:])
        self.drop_auto_interview.grid(row=2,column=0,sticky=W,pady=10)

        self.update_input_varaible_button = Button(new_window,text="Update input variable", command = self.update_input_varaible_show)
        self.update_input_varaible_button.grid(row=2,column=1,columnspan=2)

        self.update_del_input_varaible_button = Button(new_window,text="Refresh", command = self.update_input_varaible_del)
        self.update_del_input_varaible_button.grid(row=5,column=1)

        self.upd_btn_enter = Button(new_window,text="Enter", command= self.Enter_update)
        self.upd_btn_enter.grid(row=5,column=2,sticky=E)
        
        self.upd_btn_close_win = Button(new_window,text="Close Window", command=new_window.destroy)
        self.upd_btn_close_win.grid(row=5,column=0,sticky=W)


    def update_input_varaible_show(self):

        column_head = self.clicked.get()
        self.updated_label = Label(self.new_window,text = column_head)
        self.updated_label.grid(row=3,column=0,sticky=W)
    
        self.updated_entry = Entry(self.new_window,width= self.width_size)
        self.updated_entry.grid(row=3,column=1,sticky=W,pady=10)
        self.updated_entry.insert(0,self.type_input[self.column_headers.index(column_head)])
        self.update_input_varaible_button['state'] = DISABLED

    def update_input_varaible_del(self):
        self.updated_entry.destroy()
        self.updated_label.destroy()
        self.entered.destroy()
        self.update_input_varaible_button['state'] = NORMAL

    def Enter_update(self):
        column_head = self.clicked.get()
        job_number = self.job_num_entry.get()
        update = self.updated_entry.get()


        query = "UPDATE Auto_interview SET {} = '{}' WHERE Job_number='{}'".format(column_head,update,job_number)

        self.cur.execute(query)
        
        self.con.commit()

        self.entered = Label(self.new_window,text="Job application {} succesfully updated {} in Automated interview table".format(job_number,column_head))
        self.entered.grid(row=4,column=0, columnspan=3)