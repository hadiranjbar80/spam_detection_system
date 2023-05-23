"""
Email Parser
Parses the email and its attributes and return it as a dictionary or str.

Data Mining:    Final Project
Date:           May 2023
Author:         Mohammad Javad Rakhshani
"""

class EmailParser:
    """
    Email Parser
    Parses the email and its attributes and return it as a dictionary or str.
    """

    __file_content: str = ""

    def __init__(self, filename: str) -> None:
        """
        Creat an instance of EmailParser.

        Parameters:
        filename (string): filename to read email content.
        """

        self.read_file(filename)
    
    def read_file(self, filename: str) -> str:
        """
        Reads a file content.

        Parameters:
        filename (string): filename to read email content.

        File should contain these three parts:
        'from': from whom the e-mail came from;
        'subject': email-subject;
        'content': body or content of the mail.
        """
        with open(filename, "r", encoding="UTF-8") as file:
            self.__file_content = file.read()
        
        return self.__file_content
    
    def parse(self, key: str) -> str:
        """
        Parses a file content and finds 'key' in it.

        Parameters:
        key (string): key to get its values from.
        """

        assert self.__file_content != ""

        buffer: str = self.__file_content

        # [index of the key] + [legth of itself] + [1 to ignore ':']
        start_idx: int = buffer.find(key) + len(key)+1 

        # [start from where key found (start_idx)] and find ';'
        end_idx: int = buffer[start_idx:].find(";") + start_idx

        value: str = buffer[start_idx:end_idx]
        return value
    
    def parse_all(self, keys: list) -> dict:
        """
        Parses a file content and find 'keys' in it.

        Parameters:
        keys (list): keys to get its values from.
        """
        buffer: dict = dict()

        for key in keys:
            buffer[key] = self.parse(key)

        return buffer

    def print_email(self):
        """
        Prints what was inside file.
        """
        print(self.__file_content)