#!/usr/bin/env python
# Python3

'''
selenium的使用
'''

from selenium import webdriver

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    brower = webdriver.Firefox(firefox_options=fireFoxOptions)

    # webdriver.FirefoxOptions
    brower.get('http://www.baidu.com')
    print(brower.page_source)
finally:
    try:
        brower.close()
    except:
        pass
