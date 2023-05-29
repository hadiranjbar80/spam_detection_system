# Email Parser Class
Parses the email and its attributes and return it as a dictionary or str.

## Class variables
### file_content (private)
Content of the file_path specified for the class to read its content.

## Class Methods
### read_file method
This method reads a file content by specifying its `'filename'` parameters.
```py
def read_file(self, filename: str) -> str:
    with open(filename, "r", encoding="UTF-8") as file:
        self.__file_content = file.read()
        
    return self.__file_content
 ```

#### Example
```py
>>> parser = EmailParser("email.txt")
>>> parser.read_file("email.txt")
"""from:javad@jav.bin;
ip:5.119.189.223;
subject:🌍 Hello World!;
content:Where is the work? It's all by heart! 💙;"""
 ```

### parse method
Parses a file content and finds `'key'` in it.
```py
def parse(self, key: str) -> str:
    assert self.__file_content != ""
    buffer: str = self.__file_content
    
    # [index of the key] + [legth of itself] + [1 to ignore ':']
    start_idx: int = buffer.find(key) + len(key)+1 

    # [start from where key found (start_idx)] and find ';'
    end_idx: int = buffer[start_idx:].find(";") + start_idx

    value: str = buffer[start_idx:end_idx]
    return value
 ```
 
 #### Example
```py
>>> parser.parse("content")
"Where is the work? It's all by heart! 💙"
>>> parser.parse("subject")
"🌍 Hello World!"
 ```
 
 ### parse_all method
 Parses a file content and find `'keys'` in it.
 
 ```py
def parse_all(self, keys: list) -> dict:
    buffer: dict = dict()
    
    for key in keys:
        buffer[key] = self.parse(key)

    return buffer
 ```
 
  #### Example
  ```py
>>> parser.parse_all("from", "ip", "content")
{"from": "javad@jav.bin","ip": "5.119.189.223", "content": "Where is the work? It's all by heart! 💙"}
 ```
 
 ### print_email method
 Prints what was inside file.
