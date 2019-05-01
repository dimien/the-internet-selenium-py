# -*- coding: utf-8 -*-

import os

def path():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if  "nt" in dir_path:
        CHROMEDRIVER = dir_path + '/chromedriver'
        return CHROMEDRIVER
    else:
        CHROMEDRIVER = "/usr/bin/chromedriver"
        return CHROMEDRIVER

HEIGHT = 768
WEIGHT = 1366


