from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from GUI_hack import applabel ,appentry,appbutton ,appdropmenu

#---------------------------------------------------------------------------------------
column_headers=['Job number',
'Date',
'Company name',
'Job title',
'Location',
'Salary',
'Aptitude testing',
'Automated interview',
'Technical interview',
'HR interview',
'Job offer']
type_input=['Enter job number',
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

ap_column_headers=['Job number',
    'Date',
    'Company',
    'Job title',
    'Deadline',
    'Numerical reasoning',
    'Verbal reasoning',
    'Inductive resoning',
    'Deductive resoning',
    'Situational judgement test',
    'Work Behaviour assessment',
    'Reading comprehesion test',
    'Completion'
]

ap_type_input=['Enter job number',
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

ai_column_headers=['Job number',
    'Date',
    'Company',
    'Job title',
    'Deadline',
    'Completion'
]

ai_type_input=['Enter job number',
    'Enter date e.g year/month/day ',
    'Enter Company name',
    'Enter job title',
    'Enter deadline date e.g year/month/day',
    'Enter YES if completed, otherwise NO'
    ]

root =Tk()
#Title of window

root.title("Job Applications")

#Size of window 
root.geometry("265x375")

#Window icon 
root.iconbitmap('images/database.ico')
def Newentry():
    return 
def Delete_job():
    return
def Entry_start():

    en =Toplevel(root) #New window 
    en.iconbitmap('images/database.ico') #Window icon
    en.title('New entry') #window title

    #--------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------
        # The labels of all the columns of the database 

    #job_number = Label(en,text='Job number').grid(row=0,column=0,sticky=W)
    label_dict={}
    for i in range(len(column_headers)):
        label_dict[column_headers[i]]= applabel(en,column_headers[i],i,0,W).label_app()
    print(label_dict)

    #---------------------------------------------------------------------------------------
    # The entry boxes all the columns of the database 

    for i in range(len(type_input)):
        appentry(en,60,type_input[i],i,1,W,10,0).entry_app()

    #---------------------------------------------------------------------------------------
    appbutton(en,'Enter',Newentry,11,2,E,0,0).button_app()
    appbutton(en,'Close Window',en.destroy,11,0,W,0,0).button_app()

    btn1 = Button(en,text="Enter", command=Newentry).grid(row=11,column=2,sticky=E)
    btn2 = Button(en,text="Close Window", command=en.destroy).grid(row=11,column=0,sticky=W)
   
    return
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
def Delete_Entry():
    de=Toplevel()
    de.iconbitmap('images/database.ico')
    de.title('Delete entry')
    de.geometry("220x100")

    applabel(de,column_headers[0],0,0,W).label_app()

    #------------------------------------------------------------------------------------------------

    appentry(de,20,type_input[0],0,1,W,0,0).entry_app()

    #-------------------------------------------------------------------------------------------------

    appbutton(de,'Enter',Delete_job,1,1,E,0,0).button_app()
    appbutton(de,'Close Window',de.destroy,1,0,W,0,0).button_app()
    return

def show(window_job,variable_job,x,y,width_size,type_input,y_pad,x_pad,align,in_column_headers,but,disable):

    aplab = applabel(window_job,variable_job.get(),x,y,align)
    apent = appentry(window_job,width_size,type_input[in_column_headers.index(variable_job.get())],x,y+1,align,y_pad,x_pad)
    if disable == True:
        aplab.label_del()
        apent.entry_del()
        but['state'] = NORMAL
    elif disable == False:
        aplab.label_app()
        apent.entry_app()
        but['state'] = DISABLED

def jobapp():
    ja=Toplevel()
    ja.iconbitmap('images/database.ico')
    ja.title('Update entry: Job application')
    ja.geometry("550x405")

    

    applabel(ja,column_headers[0],0,0,W).label_app()

    appentry(ja,60,type_input[0],0,1,W,10,0).entry_app()

    clicked =appdropmenu(ja,column_headers[1:],2,0,W,0,0).dropmenu_app()

    btnjo=appbutton(ja,'Update',lambda :show(ja,clicked,3,0,60,type_input,10,0,W,column_headers,btj,False),2,1,"",0,0)
    btj=btnjo.button_app()
    

    appbutton(ja,'Refresh',lambda: show(ja,clicked,3,0,60,type_input,10,0,W,column_headers,btj,True),4,1,"",0,0).button_app()  

    
    

    appbutton(ja,"Close Window",ja.destroy,4,0,W,0,0).button_app()

    return
def aptest():
    at=Toplevel()
    at.iconbitmap('images/database.ico')
    at.title('Update entry: Aptitude testing')
    at.geometry("550x405")

    applabel(at,ap_column_headers[0],0,0,W).label_app()

    appentry(at,60,ap_type_input[0],0,1,W,10,0).entry_app()

    clicked =appdropmenu(at,ap_column_headers[1:],2,0,"",0,0).dropmenu_app()


    btnjo=appbutton(at,'Update',lambda :show(at,clicked,3,0,60,ap_type_input,10,0,W,ap_column_headers,btj,False),2,1,"",0,0)
    btj=btnjo.button_app()
    

    appbutton(at,'Refresh',lambda: show(at,clicked,3,0,60,ap_type_input,10,0,W,ap_column_headers,btj,True),4,1,"",0,0).button_app()  

    appbutton(at,"Close Window",at.destroy,4,0,W,0,0).button_app()
    
    return
def autointer():
    ai=Toplevel()
    ai.iconbitmap('images/database.ico')
    ai.title('Update entry: Automated interview')
    ai.geometry("550x405")

    applabel(ai,ai_column_headers[0],0,0,W).label_app()

    appentry(ai,60,ai_type_input[0],0,1,W,10,0).entry_app()

    clicked =appdropmenu(ai,ai_column_headers[1:],2,0,W,0,0).dropmenu_app()


    
    btnjo=appbutton(ai,'Update',lambda :show(ai,clicked,3,0,60,ai_type_input,10,0,W,ai_column_headers,btj,False),2,1,"",0,0)
    btj=btnjo.button_app()
    

    appbutton(ai,'Refresh',lambda: show(ai,clicked,3,0,60,ai_type_input,10,0,W,ai_column_headers,btj,True),4,1,"",0,0).button_app()  

    appbutton(ai,"Close Window",ai.destroy,4,0,W,0,0).button_app()
    return
def Update_Entry():
    up=Toplevel()
    up.iconbitmap('images/database.ico')
    up.title('Update entry')
    up.geometry("265x405")
    
    #Update job application button

    appbutton(up,"Job application table",jobapp,0,0,W,50,72.5).button_app()

    # Update aptitude testing  button 

    appbutton (up,"Aptitude testing table",aptest,1,0,W,50,70).button_app()

    # Update automated interview button


    appbutton(up,"Automated interview table",autointer,2,0,W,50,57).button_app()

    
    appbutton(up,'Close Window',up.destroy,3,0,"",0,0).button_app()
    return 

# New entry (Job application) button 

appbutton(root,"New entry",Entry_start,0,0,W,50,100).button_app()

# Update entry (Job application) button 

appbutton(root,"Update",Update_Entry,1,0,W,50,108.4).button_app()

# Delete current entry (Job application) button

appbutton(root,"Delete",Delete_Entry,2,0,W,50,110.5).button_app()


root.mainloop()
