# Interface File

This file generates an UI for the app

## Functions

### get_file function

  This functions opens a **txt file** from a local directory and return the entire content of the file.

### get_file_content function

  This function uses the **EmailParser** class and saprates each individual part of that file into related textbox.

### calculate_text function

  This function uses another function in itself called 'score' which is in the Detector Class;
  this function (score) takes three parameters and retrun a score for the givin email.

### report_ham and report_spam functioms

  If the system does not recognize correctly whether the given email is spam or not, 
  the user can train the system by clicking on the desired button and calling the realted function.
