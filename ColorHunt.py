from requests_html import HTMLSession


class ColorHunt:

    def get_html(self):
        session = HTMLSession()
        self.results = session.get(self.url)

    def __init__(self, url):
        self.url = url
        self.results = None

