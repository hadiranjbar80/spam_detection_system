"""
Interface
Email detector for the project. 
This section checks whether the givin email is in the list of spam email or not.

Data Mining:    Final Project
Date:           May 2023
Author:         Mohammed Hadi Ranjbar
"""

class email_detector:
    def __init__(self,email) -> None:
        self._email=email

    def detect_email(self):
        with open("../../database/ram_spammer_list.txt",'r',encoding='utf-8') as file:
            raw_spam_email_list= list(file.readlines())
            spam_email_list = map(lambda item: item.strip(), raw_spam_email_list)
            if self._email in spam_email_list:
                return True
            else:
                return False
            
    def detect_email_domain(self):
        email_domain=self._email.split('@')
        with open('../../database/matomo_referrer_spam_list.txt','r',encoding='utf-8') as file:
            raw_spam_domains=list(file.readlines())
            spam_domains=list(map(lambda item: item.strip(), raw_spam_domains))
            if email_domain[1] in spam_domains:  
                return True
            else:
                return False
