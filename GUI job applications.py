from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

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
    global column_header
    global type_input 
    en =Toplevel(root) #New window 
    en.iconbitmap('images/database.ico') #Window icon
    en.title('New entry') #window title
    #---------------------------------------------------------------------------------------
        # The labels of all the columns of the database 

    job_number = Label(en,text='Job number').grid(row=0,column=0,sticky=W)
    date = Label(en,text='Date').grid(row=1,column=0,sticky=W)
    company = Label(en,text ='Company name').grid(row=2,column=0,sticky=W)
    job_title = Label(en,text='Job title').grid(row=3,column=0,sticky=W) 
    location = Label(en,text='Location').grid(row=4,column=0,sticky=W) 
    salary = Label(en,text='Salary').grid(row=5,column=0,sticky=W) 
    aptitude_testing = Label(en,text='Aptitude testing').grid(row=6,column=0,sticky=W) 
    automated_interview = Label(en,text='Automated interview').grid(row=7,column=0,sticky=W) 
    technical_interview = Label(en,text='Technical interview').grid(row=8,column=0,sticky=W) 
    hr_interview = Label(en,text='HR interview').grid(row=9,column=0,sticky=W) 
    job_offer = Label(en,text='Job offer').grid(row=10,column=0,sticky=W) 
    #---------------------------------------------------------------------------------------
    column_headers=['Date',
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
    'Enter job current job status'
    ]

    #---------------------------------------------------------------------------------------
    # The entry boxes all the columns of the database 
    width_size = 60
    job_number_e = Entry(en,width= width_size)
    job_number_e.grid(row=0,column=1,sticky=W,pady=10)
    job_number_e.insert(0,"Enter job number")

    date_e = Entry(en,width= width_size)
    date_e.grid(row=1,column=1,sticky=W,pady=10)
    date_e.insert(0,'Enter date e.g year/month/day')

    company_e = Entry(en,width = width_size)
    company_e.grid(row=2,column=1,sticky=W,pady=10)
    company_e.insert(0,'Enter company name')

    job_title_e = Entry(en,width= width_size)
    job_title_e.grid(row=3,column=1,sticky=W,pady=10)
    job_title_e.insert(0,'Enter job title')

    location_e = Entry(en,width= width_size)
    location_e.grid(row=4,column=1,sticky=W,pady=10)
    location_e.insert(0,'Job location')

    salary_e = Entry(en,width= width_size)
    salary_e.grid(row=5,column=1,sticky=W,pady=10)
    salary_e.insert(0,'Enter salary in £')

    aptitude_testing_e = Entry(en,width=width_size)
    aptitude_testing_e.grid(row=6,column=1,sticky=W,pady=10)
    aptitude_testing_e.insert(0,'Enter due date for aptitude testings e.g year/month/day')

    automated_interview_e = Entry(en,width= width_size)
    automated_interview_e.grid(row=7,column=1,sticky=W,pady=10)
    automated_interview_e.insert(0,'Enter due date for automated interview e.g year/month/day')
    
    technical_interview_e = Entry(en,width= width_size)
    technical_interview_e.grid(row=8,column=1,sticky=W,pady=10)
    technical_interview_e.insert(0,'Enter date for technical interview e.g year/month/day') 

    hr_interview_e = Entry(en,width= width_size)
    hr_interview_e.grid(row=9,column=1,sticky=W,pady=10)
    hr_interview_e.insert(0,'Enter date for HR interview e.g year/month/day')

    job_offer_e = Entry(en,width=width_size)
    job_offer_e.grid(row=10,column=1,sticky=W,pady=10) 
    job_offer_e.insert(0,'Enter job current job status')
    #---------------------------------------------------------------------------------------

    



    btn1 = Button(en,text="Enter", command=Newentry).grid(row=11,column=2,sticky=E)
    btn2 = Button(en,text="Close Window", command=en.destroy).grid(row=11,column=0,sticky=W)
    return
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
def Delete_Entry():
    de=Toplevel()
    de.iconbitmap('images/database.ico')
    de.title('Delete entry')
    de.geometry("200x100")

    job_number = Label(de,text='Job number')
    job_number.grid(row=0,column=0,sticky=W)

    #------------------------------------------------------------------------------------------------

    job_number_e=Entry(de,width=20)
    job_number_e.grid(row=0,column=1)
    job_number_e.insert(0,'Enter job number')

    btn3 =Button(de,text="Enter", command=Delete_job).grid(row=1,column=0,sticky=W)
    btn4 =Button(de,text="Close Window", command=de.destroy).grid(row=1,column=1,sticky=E)
    return
def show(window_job,variable_job,x,y,width_size,type_input):
    my_label=Label(window_job,text=variable_job.get()).grid(row=x, column=y)

    update_par= Entry(window_job,width= width_size)
    update_par.grid(row=x,column=y+1,sticky=W,pady=10)
    update_par.insert(0,"Enter " + type_input+ variable_job.get())

def jobapp():
    ja=Toplevel()
    ja.iconbitmap('images/database.ico')
    ja.title('Update entry: Job application')
    ja.geometry("350x405")

    width_size = 30

    job_number = Label(ja,text='Job number')
    job_number.grid(row=0,column=0,sticky=W)

    job_number_e = Entry(ja,width= width_size)
    job_number_e.grid(row=0,column=1,sticky=W,pady=10)
    job_number_e.insert(0,"Enter job number")

    column_headers=['Date',
    'Company name',
    'Job title',
    'Location',
    'Salary',
    'Aptitude testing',
    'Automated interview',
    'Technical interview',
    'HR interview',
    'Job offer']
    type_input =[

    ]
    clicked=StringVar()
    clicked.set(column_headers[0])
    drop_jobapp = OptionMenu(ja, clicked,*column_headers).grid(row=2,column=0)

    

    #job_number = Label(ja,text=clicked.get())
    #job_number.grid(row=3,column=0,sticky=W)


    btn7=Button(ja,text='update',command= lambda:show(ja,clicked,3,0,width_size,type_input)).grid(row=2,column=1)



    btn6=Button(ja,text="Close Window", command= ja.destroy).grid(row=4,column=0,sticky=W)
    return
def aptest():
    at=Toplevel()
    at.iconbitmap('images/database.ico')
    at.title('Update entry: Aptitude testing')
    at.geometry("265x405")

    btn8 =Button(at,text="Close Window", command=at.destroy).grid(row=3,column=0)
    return
def autointer():
    ai=Toplevel()
    ai.iconbitmap('images/database.ico')
    ai.title('Update entry: Automated interview')
    ai.geometry("265x405")

    btn9 =Button(ai,text="Close Window", command=ai.destroy).grid(row=3,column=0)
    return
def Update_Entry():
    up=Toplevel()
    up.iconbitmap('images/database.ico')
    up.title('Update entry')
    up.geometry("265x405")
    
    #Update job application button
    jobapp_button = Button(up,text="Job application table",command=jobapp,padx=72.5,pady=50)
    jobapp_button.grid(row=0,column=0)

    # Update aptitude testing  button 
    ap_test_button = Button(up,text="Aptitude testing table", command =aptest,padx=70,pady=50 ) 
    ap_test_button.grid(row=1,column=0)

    # Update automated interview button
    auto_inter_button = Button(up,text="Automated interview table",command=autointer,padx=57,pady=50)
    auto_inter_button.grid(row=2,column=0)

    btn10 =Button(up,text="Close Window", command=up.destroy).grid(row=3,column=0)
    return 

# New entry (Job application) button 
Entry_button = Button(root,text="New Entry",command=Entry_start,padx=100,pady=50)
Entry_button.grid(row=0,column=0)

# Update entry (Job application) button 
Update_button = Button(root,text="Update", command =Update_Entry,padx=108.4,pady=50 ) 
Update_button.grid(row=1,column=0)

# Delete current entry (Job application) button
Delete_button = Button(root,text="Delete",command=Delete_Entry,padx=110.5,pady=50)
Delete_button.grid(row=2,column=0)



root.mainloop()
