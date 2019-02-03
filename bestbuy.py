#!/usr/bin/python2.7
import sys
import os

from bestbuy_review import *

if __name__ == "__main__":
    url = sys.argv[1]
    os.system("rm -f result_bestbuy.txt")
    os.system("touch result_bestbuy.txt")
    get_reviews(url)
