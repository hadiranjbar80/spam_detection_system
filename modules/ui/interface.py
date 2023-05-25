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

root=tk.Tk()
root.resizable(width=False,height=False)

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
        parser =  EmailParser(get_file())
        en_subject_text.set(parser.parse("subject"))
        en_email_text.set(parser.parse("from"))
        en_mail_text.configure(state='normal')
        en_mail_text.delete(1.0, tk.END)
        en_mail_text.insert(tk.END,parser.parse("content"))
        en_mail_text.configure(state='disabled')
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
    open_mail_button=tk.Button(master=button_frame,text='Open an Email',command=get_file_conten)
    oprate_spam_button=tk.Button(master=button_frame,text='Detect Spam')

    button_frame.pack(side='top',fill='x')
    open_mail_button.pack(padx=PAD_X,pady=PAD_Y)
    oprate_spam_button.pack(padx=PAD_X,pady=PAD_Y)

    #--------------------------------------Program Output---------------------------------

    output_frame=tk.Frame(master=root,width=50,height=500)

    label_icon=tk.Label(master=output_frame,text="✔️,❌")
    label_icon.pack(padx=PAD_X,pady=PAD_Y)

    label_title=tk.Label(master=output_frame,text='Title spam',font=('bold',15))
    label_title.pack(padx=PAD_X,pady=PAD_Y)

    label_percent=tk.Label(master=output_frame,text='Percent',font=(6))
    label_percent.pack(padx=PAD_X,pady=PAD_Y)
    output_frame.pack(side='top',fill='x')


    root.mainloop()

# calculate the percentage
#print(f"{d.score('Hello Hadi, check this.') *100:.2f}%")