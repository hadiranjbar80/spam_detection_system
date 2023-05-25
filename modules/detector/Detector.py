"""
Spam Detector
This detector contain base code for spam email detection.
This system uses the baysian spam filter techninc to achive this.

Data Mining:    Final Project
Date:           May 2023
Author:         Mohammad Javad Rakhshani
"""

# Project built-in modules
import modules.detector.email_detector as email_detector

# Python built-in modules
import re
import os
import json
from functools import reduce

class Detector:
    """
    Spam Detector
    This detector contain base code for spam email detection.
    This system uses the baysian spam filter techninc to achive this.

    Data Mining:    Final Project
    Date:           May 2023
    Author:         Mohammad Javad Rakhshani
    """
    
    # [Class variables]
    TOKENS_RE = re.compile(r"\$?\d*(?:[.,]\d+)+|\w+-\w+|\w+", re.U)
    SCORE: float = 0.4

    # [Methods]
    # [Methods] constructor
    def __init__(self, path=None, create_new=False):
        self.model = Model(path, create_new)

    # [Methods] return words of a text
    def _get_word_list(self, content: str):
        """
        Returns a list of strings which contains only alphabetic letters,
        and keep only the words with a length greater than 2.

        word -> alphabetic and len>2

        Parameters:
        content (str): content of an email.
        """
        return filter(lambda s: len(s) > 2,
                        self.TOKENS_RE.findall(content.lower()))
    

    def train(self, content: str,  is_spam: bool, email_from: str, ip_from: str):
        """
        Train the model.

        Parameters:
        content (str): email content.
        is_spam (bool): spam (True) / ham (False).
        email_from (str): email address of sender of email.
        ip_from (str): ip address of the sender of email.
        """
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

    def save(self):
        """
        Save 'self.model' based on 'self.model.file_path'.
        """
        self.model.save()

    def score(self, content: str, email_from: str, ip_from: str):
        """
        Evaluate and return the spam score of a content. 
        The higher the score, the stronger the liklihood that
        the content is a spam is.

        Parameters:
        content (str): content of an email.
        email_from (str): email address of sender of email.
        ip_from (str): ip address of the sender of email.
        """
        email_detect = email_detector.email_detector(email_from)
        spam_email = email_detect.detect_email()
        spam_ip = email_detect.detect_ip_address(ip_from)

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

    def is_spam(self, content: str):
        """
        Is the content of the email spam (True) or ham (False).
        """
        return self.score(content) > 0.9


class Model(object):
    """
    Save & Load the model in/from the file system using Python's json
    module.
    """

    DEFAULT_DATA_PATH = "database/model.json"

    def __init__(self, file_path=None, create_new=False):
        """
        Constructs a Model object by the indicated 'file_path', if the
        file does not exist, create a new file and contruct a empty model.

        Parameters:
        file_path: (optional) Path for the model file indicated, if
            path is not indicated, use the built-in model file provided by
            the author, which is located in the 'database' folder.

        create_new: (option) Boolean. If 'True', create an empty
            model. 'file_path' will be used when saving the model. If there
            is an existing model file on the path, the existing model file
            will be overwritten.
        """
        self.file_path = file_path if file_path else self.DEFAULT_DATA_PATH
        self.create_new = create_new
        if self.create_new:
            self.spam_count_total = 0
            self.ham_count_total = 0
            self.token_table = {}
        else:
            self.spam_count_total, self.ham_count_total, self.token_table = self.load(file_path)

    def load(self, file_path=None):
        """
        Load the serialized file from the specified file_path, and return
        'spam_count_total', 'ham_count_total' and 'token_table'.

        Parameters:
        file_path: (optional) Path for the model file. If the path does
            not exist, create a new one.
        """
        file_path = file_path if file_path else self.DEFAULT_DATA_PATH
        if not os.path.exists(file_path):
            with open(file_path, 'a'):
                os.utime(file_path, None)
        with open(file_path, 'rb') as f:
            try:
                return json.load(f)
            except:
                return (0, 0, {})

    def save(self):
        """
        Serialize the model using Python's json module, and save the
        serialized modle as a file which is indicated by 'self.file_path'.
        """
        with open(self.file_path, "w", encoding="utf8") as f:
            json.dump(
                (self.spam_count_total, self.ham_count_total,
                 self.token_table), f)
