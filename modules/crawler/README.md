# Crawler Class
This is a crawler class model that gets url(s) from caller and saves it's specified content in a file.
Used to download following database content from the web:
1. spam_ips.txt from [LittleJake/ip-blacklist](https://raw.githubusercontent.com/LittleJake/ip-blacklist/main/all_blacklist.txt)
2. matomo_referrer_spam_list.txt from [matomo-org/referrer-spam-list](https://raw.githubusercontent.com/matomo-org/referrer-spam-list/master/spammers.txt)
3. ram_spammer_list.txt from [ramblings/philosophy/spam](http://www.ram.org/ramblings/philosophy/spam/spammers.html)

## Class Methods

### crawl_and_save method
Gets *url* and saves it's *xpath content* in a *file_path* that is specified.
```py   
    def crawl_and_save(self, url: str, file_path: str, xpath: str = "") -> None:
        assert requests != None

        file = open(file_path, "w", encoding="UTF-8")
        assert file != None

        page = requests.get(url)
        assert page.status_code == 200

        if xpath == "":
            content = page.content
        else:
            # Get pages Document Tree
            tree = html.fromstring(page.content)
            content = tree.xpath(xpath)[0]

        # Byte convertion to string content
        if type(content) == bytes:    
            content: str = content.decode(encoding="UTF-8")

        # Content prepration
        content_buffer: str = str(content)
        content_buffer = content_buffer.strip()
        content_buffer = content_buffer.replace("\n\n", "\n")

        # Write to file
        file.write(content_buffer)
        file.close()
```

### Module requirements
```py
import requests
from lxml import html
```
