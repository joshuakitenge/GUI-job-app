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
        btn.grid(row= self.x_postion,column= self.y_postion)
    def button_app_var(self):
        btn = Button(self.window_job,text= self.button_text,command= lambda : self.button_func,padx=self.x_pad,pady=self.y_pad)
        btn.grid(row=self.x_postion,column=self.y_postion)

class applabel:

    def __init__(self,window_job,label_text,x_postion,y_postion,align):
        self.window_job = window_job
        self.label_text = label_text
        self.x_postion = x_postion
        self.y_postion = y_postion
        self.align = align

    def label_app(self):
        job_number = Label(self.window_job,text=self.label_text)
        job_number.grid(row=self.x_postion,column=self.y_postion,sticky=self.align)

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
        job_number_e = Entry(self.window_job,width= self.width_size)
        job_number_e.grid(row=self.x_postion,column=self.y_postion,sticky=self.align,pady=self.y_pad)
        job_number_e.insert(0,self.type_input)
        

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
        clicked=StringVar()
        clicked.set(self.column_headers)
        drop_jobapp = OptionMenu(self.window_job, clicked,*self.column_headers)
        drop_jobapp.grid(row=self.x_postion,column=self.y_postion,sticky=self.align,pady=self.y_pad)
        

























