from utils import *

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def parse_review(soup):
    r_list = soup.find("div", id="cm_cr-review_list")

    for div in r_list.find_all(attrs={"data-hook": "review"}):
        date = div.find(attrs={"data-hook": "review-date"}).string
        rate = div.find(attrs={"data-hook": "review-star-rating"}).string
        if date != None and rate != None:
            cmd = "echo " + parse_date(date) + " " + parse_rate(rate)+ " >> result_amazon.txt"
            os.system(cmd)

def has_next(html):
    if "no-reviews-section" in html:
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

    while True:
        print "Parsing page " + str(count)
        soup = BeautifulSoup(html, features="lxml")
        parse_review(soup)

        count += 1
        url = base_url + str(count)
        driver.get(url)
        html = str(driver.page_source.encode('ascii', 'ignore'))
        if not has_next(html):
            print "End at " + str(count)
            break

    driver.quit()
