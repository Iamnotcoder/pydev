#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/5/28'

import requests


def load_cookies(fname):
    with open(fname) as f:
        cookies = {}
        for line in f.read().split(';'):
            key, val = line.strip().split('=', 1)
            cookies[key] = val
    return cookies