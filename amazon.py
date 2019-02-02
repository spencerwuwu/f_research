#!/usr/bin/python2.7
import sys
import os

from amazon_review import *


if __name__ == "__main__":
    url = sys.argv[1]
    os.system("rm -f amazon_result.txt")
    os.system("touch amazon_result.txt")
    get_reviews(url)
