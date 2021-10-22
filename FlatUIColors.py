import re
import time

from bs4 import BeautifulSoup

from BaseScraper import BaseScraper


class FlatUIColors(BaseScraper):

    filePath = "C:/Users/hadend.UNIVERSITY/Desktop/flatUIPalettes.csv"
    mainURL = "https://flatuicolors.com/"

    def __init__(self):
        super(FlatUIColors, self).__init__()

    def get_all_palettes(self):
        """ Scrolls to bottom of page to load all palettes and scraps color
        hex codes for each palette.
        :param url: the URL of the collection/page
        :return: None
        """

        self.initiate_browser()

        # Go to the page
        self.browser.get(self.mainURL)

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

        palettes = soup.find_all("div", {"class": "small-palette"})

        for palette in palettes:


            name = palette.find("a", {"class": "smallpalette-container",
                                      "href": True})

            if name is not None:
                name = name['href'].rsplit("/", 1)[1]


            colors = palette.find_all("div", {"class": "color",
                                              "style": True})

            paletteColors = []
            for color in colors:
                s = color['style']
                rgb = s[s.find("(")+1:s.find(")")]
                r, g, b = rgb.split(",")
                paletteColors.append(self.rgb_to_hex(int(r), int(g), int(b)))

            self.collections[name] = paletteColors

        print(self.collections)
        self.browser.close()



