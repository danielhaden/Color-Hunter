import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

from BaseScraper import BaseScraper


class ColorHunt(BaseScraper):

    filePath = "C:/Users/hadend.UNIVERSITY/Desktop/ColorHuntPalettes.csv"
    mainURL = "https://colorhunt.co"

    def __init__(self):
        super(ColorHunt, self).__init__()

    def get_collections_urls(self):
        """ Get the URLs of all Color Hunt collections (from menu bar on left side of page)
        :return: None
        """

        # Start up Chrome browser
        self.initiate_browser()

        # Get source for Color Hunt's main page
        self.browser.get(self.mainURL)
        html = self.browser.page_source

        # parse HTML and navigate to the relevant elements
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find("body")
        tags = body.find("div", {"class": "tags"})
        urls = tags.find_all("a", {"href": True})

        # get the full URLs for Selenium and store them in object list
        for url in urls:
            self.urls.append(self.mainURL + url['href'])

    def get_all_palettes_on_page(self, url):
        """ Scrolls to bottom of page to load all palettes and scraps color
        hex codes for each palette.
        :param url: the URL of the collection/page
        :return: None
        """

        # Go to the page
        self.browser.get(url)

        # Sets how rapidly the page is scrolled in seconds
        pause_time_on_scroll = 0.2

        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")

        # Loop until we reach the bottom of the page
        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(pause_time_on_scroll)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")

            # If the new scroll height is the same, we've reached the buttom of the page
            if new_height == last_height:
                break

            # Otherwise, record the last scroll height before looping
            last_height = new_height

        # Get, parse, and scrape the page
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find("body")
        items = soup.find_all("div", {"class": "item"})

        palettes = []
        for item in items:
            palette = item.find("div", {"class": "palette"})

            c3 = palette.find("div", {"class": "place c3"})
            c2 = palette.find("div", {"class": "place c2"})
            c1 = palette.find("div", {"class": "place c1"})
            c0 = palette.find("div", {"class": "place c0"})

            colors = []
            if c3.find("span", {"data-copy": True}) is not None:
                colors.append(c3.find("span", {"data-copy": True})['data-copy'])

            if c2.find("span", {"data-copy": True}) is not None:
                colors.append(c2.find("span", {"data-copy": True})['data-copy'])

            if c1.find("span", {"data-copy": True}) is not None:
                colors.append(c1.find("span", {"data-copy": True})['data-copy'])

            if c0.find("span", {"data-copy": True}) is not None:
                colors.append(c0.find("span", {"data-copy": True})['data-copy'])

            palettes.append(colors)

        self.collections[url.rsplit('/', 1)[1]] = palettes

    def get_all_palettes(self):
        """Gets all palettes from every collection of Color Hunt"""

        self.get_collections_urls()

        for url in self.urls:
            self.get_all_palettes_on_page(url)

        self.browser.close()

    def print_stats(self):
        print("{} collections retrieved from Color Hunt.".format(len(self.collections)))

        for key, collection in self.collections.items():
            print("Color Hunt collection {}".format(key), "contains {} palettes.".format(len(collection)))

    def save_to_csv(self):
        """
        Saves results to CSV file
        :return: None
        """

        # Open the file (create if necessary)
        with open(self.filePath, 'w+', newline='') as f:

            # create the csv writer
            writer = csv.writer(f)

            for key, collection in self.collections.items():

                for palette in collection:
                    row = [key]

                    row = row + palette

                    if len(row) > 1:
                        writer.writerow(row)

            f.close()

