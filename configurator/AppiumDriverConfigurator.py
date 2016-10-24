# coding=utf-8
import os

from appium import webdriver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# config driver by appium environment factors
def driver_configurator():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = 'MI NOTE LTE'
    desired_caps['app'] = PATH('/Users/risan/Downloads/mobile-dev-v2.3.3-debug.apk')
    print desired_caps
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print 'driver start done '
    # return driver
    return driver


driver = driver_configurator()

# 点击投资理财

Money_button = driver.find_element_by_id('com.fengjr.mobile:id/tvMoney')
driver.find_element_by_android_uiautomator("android.widget.TextView")

print 'button done '

Money_button.click()

print 'click done '
