# Interface File

This file generates an UI for the app

## Functions

### get_file method
   This method opens a dialog and with that gets a **txt file** from a local directory and returns the entire content of the file.
   
```python        
def get_file():
    filename= filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    with open(filename,encoding="utf-8") as file:
        return file.read()
```

#### Example:
```py
>>> file = interface.get_file("text.txt")
>>> print(file)
"content of the file is here."
```

### get_file_content method
    
   This method uses the **EmailParser** class and separates each individual part of that file into related textbox.
   
```py
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
```

#### Example:
```py
>>> get_file_content()
"The values will fit into text boxes."
```
### calculate_text method

   This method uses another method in itself called **score** which is in the **Detector** Class;
   this method (score) takes three parameters and retrusn a score for the given email.
```py
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
          winsound.MessageBeep(winsound.SND_NOWAIT)
      else:
          label_icon.configure(text='✔',fg='green')
          label_title.configure(text='Ham')
          winsound.MessageBeep(winsound.SND_NOSTOP)

      en_mail_text.configure(state='disabled')
  else:
      label_percent.configure(text='Please first open a file!',fg='red')
```

#### Example:
```py
>>> calculate_text()
"Calculates the score of email and show it into label_percent."
```
### report_ham and report_spam method

   If the system does not recognize correctly whether the given email is spam or not, 
   the user can train the system by clicking on the desired button and calling the realted function.
   The trained data is stored in **model.json** file in the database folder 
 ```py   
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


 def report_spam():
     """
     User can use this method to train the system, 
     if the system detects incorrectly
     (Trains the system by the givin email.)
     Called in 'spam_button'
     """
     d.train(content, True,ip,email)
     d.save()
  ```
  
  #### Example:
  ```py
  >>> report_ham()
  >>> report_spam()
  "Called in buttons."
  ```
