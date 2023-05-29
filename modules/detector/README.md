# Email Detector File(email_detector Class)

   An email should be provided when a sample is made;
   By that given email determines whether the email is valid or not

## Class Methods

### detect_email function
   This method gets the email from **self** and checks whether it is spam or not;
   by conparing it with stored emails in the **ram_spammer_list.txt**.
   If the email is spam, it would return Trure otherwise False.
```py   
  def detect_email(self):
     with open("database/ram_spammer_list.txt",'r',encoding='utf-8') as file:
         raw_spam_email_list= list(file.readlines())
         spam_email_list = map(lambda item: item.strip(), raw_spam_email_list)
         if self._email in spam_email_list:
             return True
         else:
             return False
```

#### Example:

```py
>>> detector = email_detector('hadi@google.com')
>>> detector.detect_email()
True
```
### detect_domain_email
   This method gets the email from **self** and specifies whether the email domain is valid or not
   First, it separates the domain from the entire email and compares that domain with the content of the **matomo_referrer_spam_list.txt** file; 
   which has common spam domains in it.
   True spam and False not spam
   
   ```py
   def detect_email_domain(self):
      email_domain=self._email.split('@')
      with open('database/matomo_referrer_spam_list.txt','r',encoding='utf-8') as file:
          raw_spam_domains=list(file.readlines())
          spam_domains=list(map(lambda item: item.strip(), raw_spam_domains))
          if email_domain[1] in spam_domains:  
              return True
          else:
              return False
   ```
   #### Example:
   
   ```py
   >>> detector = email_detector('hadi@google.com')
   >>> detector.detect_email_domain()
   True
   ```
### detect_ip_address

   This method gets an IP and compares it with the content if **spam_ips.txt** file to specify whether it is spam or not.
   
  ```py
   def detect_ip_address(self,ip_address):
     with open('database/spam_ips.txt','r',encoding='utf-8') as file:
        raw_spam_ip_list=list(file.readlines())
        spam_ip_list=list(map(lambda item: item.strip(), raw_spam_ip_list))
        if ip_address in spam_ip_list:
            return True
        else:
            return False
   ```
   #### Example:
   
   ```py
   >>> detector = email_detector('hadi@google.com')
   >>> detector.detect_ip_address('1.116.222.161')
   False
   ```
# Detector File


