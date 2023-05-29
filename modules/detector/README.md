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
# Detector.py File (Spam Detector class)
This detector contain base code for spam email detection and its data models. 
This system uses the baysian spam filter technique to achive this.

## Class Variables
### SCORE
The initial score for the case to check, the defualt value is set to `0.4` and the datatype is `float`.
```py
 SCORE: float = 0.4
 ```
 ### TOKENS_RE
 Regex to filter every character in an email content: `\$?\d*(?:[.,]\d+)+|\w+-\w+|\w+`

## Class Methods
Constructor of the Detector initials the the Model Class to create/open a data model for spam email detection.

### get_word_list method (private)
Returns a list of strings which contains only alphabetic letters, and keep only the words with a length greater than 2.

```py
def _get_word_list(self, content: str):
    return filter(lambda s: len(s) > 2,
                  self.TOKENS_RE.findall(content.lower()))
```

### train method
Method to train the model and pass the sample parameter to machine to learn from it.
#### Parameters:
*content (str):*  email content.<br>
*is_spam (bool):* spam (True) / ham (False).<br>
*email_from (str):* email address of sender of email.<br>
*ip_from (str):* ip address of the sender of email.<br>
```py
def train(self, content: str,  is_spam: bool, email_from: str, ip_from: str):
        token_table = self.model.token_table
        if is_spam:
            self.model.spam_count_total += 1
            with open("database/ram_spammer_list.txt",\
                        "a") as spam_list:
                if not email_detector.email_detector(email_from).detect_email():
                    if spam_list.writable:
                        spam_list.write("\n" + email_from)
            with open("database/spam_ips.txt",\
                        "a") as spam_list:
                if not email_detector.email_detector(email_from).detect_ip_address(ip_from):
                    if spam_list.writable:
                        spam_list.write("\n" + ip_from)
                        
        else:
            self.model.ham_count_total += 1

        for word in self._get_word_list(content.lower()):
            if word in token_table:
                token = token_table[word]
                if is_spam:
                    token[1] += 1
                else:
                    token[0] += 1
            else:
                token_table[word] = [0, 1] if is_spam else [1, 0]
 ```
 
 ### save method
 Save _'self.model'_ based on _'self.model.file_path'_.
 
### score method
Evaluate and return the spam score of a content. The higher the score, the stronger the liklihood that the content is a spam is.

#### Parameters:
*content (str):*  email content.<br>
*email_from (str):* email address of sender of email.<br>
*ip_from (str):* ip address of the sender of email.<br>

 ```py
 def score(self, content: str, email_from: str, ip_from: str):
        email_detect = email_detector.email_detector(email_from)
        spam_email = email_detect.detect_email()
        spam_ip = email_detect.detect_ip_address(ip_from)

 ```
 At the beginning of the methods there is a test to email address and ip that if they existed in the blacklist or not.
 
 ```py
        token_table = self.model.token_table
        hashes = self._get_word_list(content.lower())
        scores: list = []
        for h in hashes:
            if h in token_table:
                ham_count, spam_count = token_table[h]
                if spam_count > 0 and ham_count == 0:
                    score = 0.99
                elif spam_email and spam_ip:
                    score = 0.99
                elif spam_count == 0 and ham_count > 0 and (spam_email or spam_ip):
                    score = 0.80
                elif spam_count == 0 and ham_count > 0:
                    score = 0.2
                elif self.model.spam_count_total > 0 and self.model.ham_count_total > 0:

                    # Prob of spam or ham
                    ham_prob = float(ham_count) / float(
                        self.model.ham_count_total)
                    spam_prob = float(spam_count) / float(
                        self.model.spam_count_total)
                    
                    # Score
                    score = spam_prob / (ham_prob + spam_prob)

                    if score < 0.01:
                        score = 0.01
                else:
                    score = self.SCORE
            else:
                score = self.SCORE
            scores.append(score)
        
        if (len(scores) == 0):
            return 0
    
        if (len(scores) > 20):
                scores.sort()
                scores = scores[:10] + scores[-10:]

        product = reduce(lambda x, y: x * y, scores)
        alt_product = reduce(lambda x, y: x * y, map(lambda r: 1.0 - r,
                                                    scores))
        return product / (product + alt_product)
 ```
 Then the score(probability) of the email to be spam is check based-on its hashes. If there is not enough information about the hash, scoring is trying to score it based-on the ip/email blacklist.
 
 
 ### is_spam method
 Is the content of the email spam (True) or ham (False).
 
```py
def is_spam(self, content: str):
    return self.score(content) > 0.9
```


# Detector.py File (Model class)
Save & Load the model in/from the file system using Python's json module.

## Class Variables
### DEFAULT_DATA_PATH
The location of the data model to be save. The default is `"database/model.json"`. 
```py
DEFAULT_DATA_PATH = "database/model.json"
 ```
## Class Methods
### load method
Load the serialized file from the specified file_path, and return _'spam_count_total'_, _'ham_count_total'_ and _'token_table'_.

```py
def load(self, file_path=None):
    file_path = file_path if file_path else self.DEFAULT_DATA_PATH
    if not os.path.exists(file_path):
        with open(file_path, 'a'):
            os.utime(file_path, None)
        with open(file_path, 'rb') as f:
            try:
                return json.load(f)
            except:
                return (0, 0, {})
```

### save method        
Serialize the model using Python's json module, and save the serialized modle as a file which is indicated by 'self.file_path'.

```py
def save(self):
    with open(self.file_path, "w", encoding="utf8") as f:
        json.dump(
            (self.spam_count_total, self.ham_count_total,
            self.token_table), f)
```
