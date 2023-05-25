"""
Interface
Graphical uesr-interface for the app.

Data Mining:    Final Project
Date:           May 2023
Author:         Mohammed Hadi Ranjbar
"""
#-----------------------------Dependencies-----------------------
from ..parser.EmailParser import EmailParser
import tkinter as tk
from tkinter import filedialog
from ..detector.Detector import Detector

d=Detector(create_new=False)

root=tk.Tk()
root.resizable(width=False,height=False)

ip = ""
content = ""
email = ""

PAD_X=5
PAD_Y=5
MAX_LENGTH_ENTRY = 40

"""
Geterates the interface of the application
"""
def generate_interface():
    #---------------------------------------functions-------------------------------

    """
    Gets a file dynamically in the local computer
    Called in the 'get_file_content' method
    """
    def get_file():
        filename= filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        with open(filename,encoding="utf-8") as file:
            return file.read()

    """
    Gets content of a txt file and put the values into the entries
    called in the 'Open an Email' button

    """
    def get_file_conten():
        global content
        global ip
        global email
        parser =  EmailParser(get_file())

        content, ip, email = parser.parse("content"),parser.parse("ip"),parser.parse("email")
        en_subject_text.set(parser.parse("subject"))
        en_email_text.set(f"{email}({ip})")
        en_mail_text.configure(state='normal')
        en_mail_text.delete(1.0, tk.END)
        en_mail_text.insert(tk.END,content)
        en_mail_text.configure(state='disabled')

    """
    Calculates the score of the email to to check it is spam or not.
    This calculation is done by three prameters (content, email,ip)
    """
    def calculate_text():
        global content
        global email
        global ip
        email_score=d.score(content.lower(),email.lower(),ip.lower())
        if content != '':
            en_mail_text.configure(state='normal')
            label_percent.configure(text=f"Percent: {email_score *100:.2f}",fg='black')
            if email_score >0.9:
                label_icon.configure(text='❌',fg='red')
                label_title.configure(text='Spam')
            else:
                label_icon.configure(text='✔',fg='green')
                label_title.configure(text='Ham')

            en_mail_text.configure(state='disabled')
        else:
            label_percent.configure(text='Please first open a file!',fg='red')
    
    """
    User can use this method to train the system, 
    if the system detects incorrectly
    (Trains the system by the givin email.)
    Called in 'ham_button'
    """
    def report_ham():
        global content
        global email
        global ip
        if content != "" and\
             email != "":
            d.train(content,False,ip,email)
            d.save()
        else:
            label_percent.configure(text='Please first open a file!',fg='red')


    """
    User can use this method to train the system, 
    if the system detects incorrectly
    (Trains the system by the givin email.)
    Called in 'spam_button'
    """
    def report_spam():
        global content
        global email
        global ip
        if content != "" and\
             email != "":
            d.train(content,True,ip,email)
            d.save()
        else:
            label_percent.configure(text='Please first open a file!',fg='red')
    #---------------------------------------labels-------------------------------
    label_frame=tk.Frame(master=root,width="50",height="100")
    subject_label=tk.Label(master=label_frame,text='Subject: ')
    mail_label=tk.Label(master=label_frame,text='Email: ')
    text_label=tk.Label(master=label_frame,text='Text: ')

    label_frame.pack(side=["left"],fill='both')
    subject_label.pack(padx=PAD_X,pady=PAD_Y)
    mail_label.pack(padx=PAD_X,pady=PAD_Y)
    text_label.pack(padx=PAD_X,pady=PAD_Y)


    #---------------------------------------Entries-------------------------------
    en_subject_text=tk.StringVar()
    en_email_text=tk.StringVar()

    entry_frame=tk.Frame(master=root,width=500,height=500)
    en_subject=tk.Entry(master=entry_frame,textvariable=en_subject_text,state='disabled', width=MAX_LENGTH_ENTRY)
    en_email=tk.Entry(master=entry_frame,textvariable=en_email_text,state='disabled', width=MAX_LENGTH_ENTRY)

    entry_frame.pack(side='left',fill='both')
    en_subject.pack(padx=PAD_X,pady=PAD_Y,fill='both')
    en_email.pack(padx=PAD_X,pady=PAD_Y,fill='both')

    #---------------------------------Scroll-----------------------
    v=tk.Scrollbar(entry_frame, orient='vertical')
    v.pack(side='right',fill='y')

    en_mail_text=tk.Text(master=entry_frame,state='disabled',width=MAX_LENGTH_ENTRY,height=MAX_LENGTH_ENTRY/2,yscrollcommand=v.set)
    en_mail_text.pack(padx=PAD_X,pady=PAD_Y)
    v.config(command=en_mail_text.yview)

    #---------------------------------------Buttons-------------------------------
    button_frame=tk.Frame(master=root,width=500,height=500)
    open_mail_button=tk.Button(master=button_frame,text='Open an Email',command=get_file_conten)
    oprate_spam_button=tk.Button(master=button_frame,text='Detect Spam',command=calculate_text)
    

    button_frame.pack(side='top',fill='x')
    open_mail_button.pack(padx=PAD_X,pady=PAD_Y)
    oprate_spam_button.pack(padx=PAD_X,pady=PAD_Y)

    #--------------------------------------Program Output---------------------------------
    output_frame=tk.Frame(master=root,width=50,height=500)

    label_icon=tk.Label(master=output_frame,text="✔️,❌")
    label_icon.pack(padx=PAD_X,pady=PAD_Y)

    label_title=tk.Label(master=output_frame,text='Title spam',font=('bold',15))
    label_title.pack(padx=PAD_X,pady=PAD_Y)

    label_percent=tk.Label(master=output_frame,text='Percent',font=(3))
    label_percent.pack(padx=PAD_X,pady=PAD_Y)
    output_frame.pack(side='top',fill='x')

    label_error=tk.Label(master=output_frame,font=(4))
    label_error.pack(padx=PAD_X,pady=PAD_Y)
    label_error.pack(side='top',fill='x')

    ham_button=tk.Button(master=output_frame,text='✔ Report Ham',command=report_ham)
    spam_button=tk.Button(master=output_frame,text='❌ Report Spam',command=report_spam)

    spam_button.pack(padx=PAD_X,pady=PAD_Y)
    ham_button.pack(padx=PAD_X,pady=PAD_Y)

    root.mainloop()

# calculate the percentage
#print(f"{d.score('Hello Hadi, check this.') *100:.2f}%")