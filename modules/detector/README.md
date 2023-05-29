# Email Detector File(email_detector Class)

    An email should be provided when a sample is made
    By that givin email determine whether the email is valid or not

## Class Methods

### detect_email function
      This function gets the email from 'self' and checks whether it is spam or not;
      by conparing it with stored emails in the 'ram_spammer_list.txt'.
      If the email is spam, it would return Trure otherwise False.
### detect_domain_email
      This function gets the email from 'self' and specifies the domain for that email is valid or not.
      First, it separates the domain from the entire email and compares that domain with the content of the "matomo_referrer_spam_list.txt" file; which has common         spam domains in it.
      True spam and False not spam
### detect_ip_address
      This function gets an IP and compare it with the content if 'spam_ips.txt' file to specify whether it is spam or not.
# Detector File


