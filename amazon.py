#!/usr/bin/python2.7
import sys
import os

from amazon_review import *


if __name__ == "__main__":
    url = sys.argv[1]
    os.system("rm -f result_amazon.txt")
    os.system("touch result_amazon.txt")
    get_reviews(url)
