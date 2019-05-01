# -*- coding: utf-8 -*-

import os
import platform

def path():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    os_name = platform.system()
    if  os_name == "Windows":
        CHROMEDRIVER = dir_path + '/chromedriver'
        return CHROMEDRIVER
    else:
        CHROMEDRIVER = "/usr/bin/chromedriver"
        return CHROMEDRIVER


HEIGHT = 768
WEIGHT = 1366


