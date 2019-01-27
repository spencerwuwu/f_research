from bs4 import BeautifulSoup
from utils import *


def parse_review(url):
    html = wget_html(url)
    with open(html) as fp:
        soup = BeautifulSoup(fp)

    r_list = soup.find("div", id="cm_cr-review_list")

    for div in r_list.find_all(attrs={"data-hook": "review"}):
        date = div.find(attrs={"data-hook": "review-date"}).string
        rate = div.find(attrs={"data-hook": "review-star-rating"}).string
        if date != None and rate != None:
            print parse_date(date) + " " + parse_rate(rate)

    remove_html(html)

