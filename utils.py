#!/usr/bin/python2.7
import sys
import os

def get_path():
    return os.path.dirname(os.path.abspath(__file__)) + "/"

def parse_month(month):
    if "Jan" in month:
        return 1
    elif "Feb" in month:
        return 2
    elif "Mar" in month:
        return 3
    elif "Apr" in month:
        return 4
    elif "May" in month: return 5
    elif "Jun" in month:
        return 6
    elif "Jul" in month:
        return 7
    elif "Aug" in month:
        return 8
    elif "Sep" in month:
        return 9
    elif "Oct" in month:
        return 10
    elif "Nov" in month:
        return 11
    elif "Dec" in month:
        return 12

def parse_date(orig_date):
    month = orig_date.split(" ")[0]
    month = str(parse_month(month))
    day = orig_date.split(" ")[1].split(",")[0]
    year = orig_date.split(" ")[2]
    return year + " " + month + " " + day

def parse_rate(rate):
    return rate.split(".")[0]
