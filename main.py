
# Project built-in modules
import modules.parser.EmailParser
import modules.crawler.Crawler as crawler
import modules.ui.interface as ui

# Python built-in modules
import os
import time

# Global Variables
SPAMMER_MAIL_LIST_FILE = "database/ram_spammer_list.txt"
SPAMMER_DOMAIN_LIST_FILE = "database/matomo_referrer_spam_list.txt"
SPAMMER_IP_LIST_FILE = "database/spam_ips.txt"

# Crawl the spam lists and update its knowledge
crawler_control = crawler.Crawler()

# Loading Intro
print("[LOADING]")


if not os.path.exists(SPAMMER_MAIL_LIST_FILE):
    print("Downloading the spammers' email database files...")
    # Spammers' email list
    crawler_control.crawl_and_save("http://www.ram.org/ramblings/philosophy/spam/spammers.html",
                                SPAMMER_MAIL_LIST_FILE, "/html/body/pre/text()")

if not os.path.exists(SPAMMER_DOMAIN_LIST_FILE):
    print("Downloading the spammers' domain database files...")
    # Spammers' domain list
    crawler_control.crawl_and_save("https://raw.githubusercontent.com/matomo-org/referrer-spam-list/master/spammers.txt",
                                SPAMMER_DOMAIN_LIST_FILE)

if not os.path.exists(SPAMMER_IP_LIST_FILE):
    print("Downloading the spammers' ip database files...")
    # Spammers' ip list
    crawler_control.crawl_and_save("https://raw.githubusercontent.com/LittleJake/ip-blacklist/main/all_blacklist.txt",
                                SPAMMER_IP_LIST_FILE)


print("[RUN]")
ui.generate_interface()
