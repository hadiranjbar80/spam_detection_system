"""
Spam Crawler
This crawler gets url(s) from caller and saves it's specified content in a file.

Data Mining:    Final Project
Date:           May 2023
Author:         Mohammad Javad Rakhshani
"""

# Python built-in modules
import requests
from lxml import html

class Crawler:
    """
    Crawler
    Gets url(s) from caller and saves it's specified content in a file.
    """

    def __init__(self) -> None:
        """
        Create a simple instance of Crawler.
        """
        pass

    def crawl_and_save(self, url: str, file_path: str, xpath: str = "") -> None:
        """
        Gets url and saves it's xpath content in a file.
        """
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
