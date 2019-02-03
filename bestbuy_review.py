from utils import *

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def parse_review(soup):
    r_list = soup.find("ul", attrs={"class": "reviews-list"})

    for div in r_list.find_all(attrs={"class": "review-item"}):
        date = div.find(attrs={"class": "submission-date"})['title']
        rate = div.find(attrs={"class": "c-review-average"}).string
        cmd = "echo " + parse_date(date) + " " + rate + " >> result_bestbuy.txt"
        os.system(cmd)

def has_next(soup):
    r_list = soup.find("div", id="main-content")
    if "page next disabled" in str(r_list):
        return False
    else:
        return True


def get_reviews(base_url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    count = 1
    url = base_url + str(count)
    driver.get(url)
    html = str(driver.page_source.encode('ascii', 'ignore'))
    soup = BeautifulSoup(html, features="lxml")
    while True:
        print "Parsing page " + str(count)
        parse_review(soup)

        count += 1
        url = base_url + str(count)
        driver.get(url)
        html = str(driver.page_source.encode('ascii', 'ignore'))
        soup = BeautifulSoup(html, features="lxml")
        if not has_next(soup):
            print "End at " + str(count)
            break

    driver.quit()
