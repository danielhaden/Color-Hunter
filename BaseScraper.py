import csv
import os
from selenium import webdriver


class BaseScraper:

    def __init__(self):
        self.urls = []
        self.collections = {}
        self.browser = None

    def initiate_browser(self):
        """ Instantiate a Chrome browser driven by Selenium
        :return: None
        """
        pathToDriver = os.getcwd() + "\chromedriver.exe"

        self.browser = webdriver.Chrome(
            executable_path=pathToDriver)

    def save_to_csv(self):
        """
        Saves results to CSV file
        :return: None
        """

        # Open the file (create if necessary)
        with open(self.filePath, 'w+', newline='') as f:

            # create the csv writer
            writer = csv.writer(f)

            for name, colors in self.collections.items():

                name = [name]

                row = name + colors

                if len(row) > 1:
                    writer.writerow(row)

            f.close()

    @staticmethod
    def rgb_to_hex(r, g, b):
        """
        Converts an RGB triplet to hexadecimal
        :param r: the 0-255 red pixel value
        :param g: the 0-255 green pixel value
        :param b: the 0-255 blue pixel value
        :return: hexidecimal value representing a 24-bit color
        """
        return '#%02x%02x%02x' % (r, g, b)