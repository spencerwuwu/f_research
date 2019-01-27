from bs4 import BeautifulSoup
from utils import *


def parse_review(url):
    html = wget_html(url)
    with open(html) as fp:
        soup = BeautifulSoup(fp)

    r_list = soup.find("ul", attrs={"class": "reviews-list"})

    for div in r_list.find_all(attrs={"class": "review-item"}):
        date = div.find(attrs={"class": "submission-date"})['title']
        rate = div.find(attrs={"class": "c-review-average"}).string
        if date != None and rate != None:
        print parse_date(date) + " " + rate

    remove_html(html)

def has_next(url):
    html = wget_html(url)
    with open(html) as fp:
        soup = BeautifulSoup(fp)

    r_list = soup.find("ul", attrs={"class": "reviews-list"})


def get_reviews(base_url):
    count = 1
    while True:
        url = base_url + str(count)
        parse_review(url)

        count += 1
        url = base_url + str(count)
        if not has_next(url):
            break
