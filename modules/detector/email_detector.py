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
        """
        This method detects whether an email is spam or not.
        True if it is spam otherwise it returns False
        """ 
        with open("database/ram_spammer_list.txt",'r',encoding='utf-8') as file:
            raw_spam_email_list= list(file.readlines())
            spam_email_list = map(lambda item: item.strip(), raw_spam_email_list)
            if self._email in spam_email_list:
                return True
            else:
                return False
 
    def detect_email_domain(self):
        """
        This method detects whether an email's domain is spam or not.
        True if it is spam otherwise it returns False
        """  
        email_domain=self._email.split('@')
        with open('database/matomo_referrer_spam_list.txt','r',encoding='utf-8') as file:
            raw_spam_domains=list(file.readlines())
            spam_domains=list(map(lambda item: item.strip(), raw_spam_domains))
            if email_domain[1] in spam_domains:  
                return True
            else:
                return False

    def detect_ip_address(self,ip_address):
        """
        This method detects whether an  IP address is spam or not.
        True if it is spam otherwise it returns False
        """ 
        with open('database/spam_ips.txt','r',encoding='utf-8') as file:
            raw_spam_ip_list=list(file.readlines())
            spam_ip_list=list(map(lambda item: item.strip(), raw_spam_ip_list))
            if ip_address in spam_ip_list:
                return True
            else:
                return False
            