import time

from selenium import webdriver

from bs4 import BeautifulSoup

from ColorHunt import ColorHunt


if __name__ == '__main__':

    option = webdriver.ChromeOptions().add_argument(" - incognito")

    browser = webdriver.Chrome(executable_path='C:/Users/hadend.UNIVERSITY/PycharmProjects\ColorPaletteWebScraper/chromedriver.exe',
                               chrome_options=option)

    browser.get("https://colorhunt.co/retro")

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    html = browser.page_source


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

    print(palettes)
