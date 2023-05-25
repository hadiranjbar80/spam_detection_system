
import modules.parser.EmailParser
import modules.crawler.Crawler as crawler
import modules.ui.interface as ui

# Crawl the spam lists and update its knowledge
crawler_control = crawler.Crawler()
# Spammers' email list
crawler_control.crawl_and_save("http://www.ram.org/ramblings/philosophy/spam/spammers.html",
                               "database/ram_spammer_list.txt", "/html/body/pre/text()")
# Spammers' domain list
crawler_control.crawl_and_save("https://raw.githubusercontent.com/matomo-org/referrer-spam-list/master/spammers.txt",
                               "database/matomo_referrer_spam_list.txt")
ui.generate_interface()
