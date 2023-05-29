# Interface File

This file generates an UI for the app

## Functions

### get_file function
   This functions opens a **txt file** from a local directory and return the entire content of the file.
   
        def get_file():
        """
        Gets a file dynamically in the local computer
        Called in the 'get_file_content' method
        """
        filename= filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        with open(filename,encoding="utf-8") as file:
            return file.read()

### get_file_content function
    
   This function uses the **EmailParser** class and saprates each individual part of that file into related textbox.
     
     def get_file_conten():
        """
        Gets content of a txt file and put the values into the entries
        called in the 'Open an Email' button
        """
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

### calculate_text function

   This function uses another function in itself called **score** which is in the **Detector** Class;
   this function (score) takes three parameters and retrun a score for the givin email.

     def get_file_conten():
        """
        Gets content of a txt file and put the values into the entries
        called in the 'Open an Email' button
        """
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

### report_ham and report_spam functioms

   If the system does not recognize correctly whether the given email is spam or not, 
   the user can train the system by clicking on the desired button and calling the realted function.
   The trained data is stored in **model.json** file in the database folder 
    
    def report_ham():
        """
        User can use this method to train the system, 
        if the system detects incorrectly
        (Trains the system by the givin email.)
        Called in 'ham_button'
        """
        global content
        global email
        global ip
        if content != "" and\
             email != "":
            d.train(content,False,ip,email)
            d.save()
        else:
            label_percent.configure(text='Please first open a file!',fg='red')


    def report_spam():
        """
        User can use this method to train the system, 
        if the system detects incorrectly
        (Trains the system by the givin email.)
        Called in 'spam_button'
        """
        d.train(content, True,ip,email)
        d.save()
