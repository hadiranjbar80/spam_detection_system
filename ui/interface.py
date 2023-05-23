"""
Interface
Graphical uesr-interface for the app.

Data Mining:    Final Project
Date:           May 2023
Author:         Mohammed Hadi Ranjbar
"""

import tkinter as tk

def generate_interface():
    root=tk.Tk()
    root.resizable(width=False,height=False)
    
    PAD_X=5
    PAD_Y=5
    MAX_LENGTH_ENTRY = 40

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
    entry_frame=tk.Frame(master=root,width=500,height=500)
    en_subject=tk.Entry(master=entry_frame,state='disabled', width=MAX_LENGTH_ENTRY)
    en_email=tk.Entry(master=entry_frame,state='disabled', width=MAX_LENGTH_ENTRY)



    entry_frame.pack(side='left',fill='both')
    en_subject.pack(padx=PAD_X,pady=PAD_Y)
    en_email.pack(padx=PAD_X,pady=PAD_Y)



    #---------------------------------Scroll-----------------------
    v=tk.Scrollbar(entry_frame, orient='vertical')
    v.pack(side='right',fill='y')

    en_mail_text=tk.Text(master=entry_frame,state='disabled',width=MAX_LENGTH_ENTRY,height=MAX_LENGTH_ENTRY/2,yscrollcommand=v.set)
    en_mail_text.pack(padx=PAD_X,pady=PAD_Y)
    v.config(command=en_mail_text.yview)
    #---------------------------------------Buttons-------------------------------
    button_frame=tk.Frame(master=root,width=500,height=500)
    open_mail_button=tk.Button(master=button_frame,text='Open an Email')
    oprate_spam_button=tk.Button(master=button_frame,text='Detect Spam')

    button_frame.pack(side='left',fill='both')
    open_mail_button.pack(padx=PAD_X,pady=PAD_Y)
    oprate_spam_button.pack(padx=PAD_X,pady=PAD_Y)

    root.mainloop()