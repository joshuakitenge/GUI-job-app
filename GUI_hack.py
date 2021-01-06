from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

class appbutton:
    def __init__(self,window_job,button_text,button_func,x_postion,y_postion,align,y_pad,x_pad):
        self.window_job = window_job
        self.button_text = button_text
        self.button_func = button_func
        self.x_postion = x_postion
        self.y_postion = y_postion
        self.align = align
        self.y_pad = y_pad
        self.x_pad = x_pad

    def button_app(self):
        
        btn = Button(self.window_job,text= self.button_text,command= self.button_func,padx=self.x_pad,pady=self.y_pad)
        btn.grid(row= self.x_postion,column= self.y_postion,sticky=self.align)
        return btn

    
    

class applabel:

    def __init__(self,window_job,label_text,x_postion,y_postion,align):
        self.window_job = window_job
        self.label_text = label_text
        self.x_postion = x_postion
        self.y_postion = y_postion
        self.align = align

    def label_app(self):
        #global my_label
        self.my_label = Label(self.window_job,text=self.label_text)
        self.my_label.grid(row=self.x_postion,column=self.y_postion,sticky=self.align)
        return
    
    def label_del(self):
        self.my_label.destroy()




class appentry:
    def __init__(self,window_job,width_size,type_input,x_postion,y_postion,align,y_pad,x_pad):
        self.window_job = window_job
        self.width_size = width_size
        self.type_input = type_input
        self.x_postion = x_postion
        self.y_postion = y_postion
        self.align = align
        self.y_pad = y_pad
        self.x_pad = x_pad

    def entry_app(self):
        global job_number_e
        job_number_e = Entry(self.window_job,width= self.width_size)
        job_number_e.grid(row=self.x_postion,column=self.y_postion,sticky=self.align,pady=self.y_pad)
        job_number_e.insert(0,self.type_input)
    def entry_del(self):
        job_number_e.destroy()

        

class appdropmenu:

    def __init__(self,window_job,column_headers,x_postion,y_postion,align,y_pad,x_pad):
        self.window_job = window_job
        self.column_headers = column_headers
        self.x_postion = x_postion
        self.y_postion = y_postion
        self.align = align
        self.y_pad = y_pad
        self.x_pad = x_pad

    def dropmenu_app(self):
        #global clicked
        clicked=StringVar()
        clicked.set(self.column_headers[0])
        drop_jobapp = OptionMenu(self.window_job, clicked,*self.column_headers)
        drop_jobapp.grid(row=self.x_postion,column=self.y_postion,sticky=self.align,pady=self.y_pad)
        return clicked























