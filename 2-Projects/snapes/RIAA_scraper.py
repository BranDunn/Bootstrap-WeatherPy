from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #list url to visit
    url = 'https://www.google.com'
    # riaa_url = 'https://www.riaa.com/gold-platinum/?tab_active=awards_by_album#search_section'

    #visit url
    browser.visit(url)

    # riaa_html = browser.html 
    # soup = BeautifulSoup(riaa_html, 'html.parser')

    # #click 10 times to load more results
    # for x in range(1, 10):
    #     browser.click_link_by_id('loadmore')

    

scrape()