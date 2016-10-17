# coding=utf-8

from mhlib import PATH
from appium import webdriver

# config driver by appium environment factors
def driver_configurator():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH('/Users/risan/Downloads/mobile-dev-v2.3.3-debug.apk')
    print desired_caps
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # return driver


driver_configurator()
