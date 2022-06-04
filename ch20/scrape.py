import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        """
        Takes a website as a parameter.
        """
        self.site = site

    def scrape(self):
        """
        Requests a Response object from website and
        stores XML data.

        Creates a BeautifulSoup object to pass XML and
        parse preference as  parameters.

        Calls the findall function on BS object to look
        for and display data related to item tags, more 
        specifically titles, in the XML
        """
        r = urllib.request.urlopen(self.site)
        xml = r.read()

        parser = "html.parser"
        sp = BeautifulSoup(xml,parser)

        with open("output.txt", "w") as f:
            for item in sp.find_all("item"):
                title = item.find("title")
                if title is None:
                    continue
                else:
                    print("\n" + title.text)
                    f.write(title.text + "\n")

news = "https://news.google.com/news/rss/headlines"

Scraper(news).scrape()


