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
        self.browser = webdriver.Chrome(
            executable_path='C:/Users/hadend.UNIVERSITY/PycharmProjects\ColorPaletteWebScraper/chromedriver.exe')