import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd, getKeyCode
from utils.verify import isExist, numFromStr
from setting import getSetting
from mysql.initDB import initMysql
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyFuYuan(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.sunline.android.sunline'
    settingData['appActivity'] = '.DefaultAlias'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    if isExist(driver, 4, 'com.sunline.android.sunline:id/cancel'):
        driver.find_element_by_id('com.sunline.android.sunline:id/cancel').click()
        sleep(1)
    tipPath = 'new UiSelector().text("我知道了")'
    if isExist(driver, 1, tipPath):
        driver.find_element_by_android_uiautomator(tipPath).click()
        sleep(1)

    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("可认购")').click()
    sleep(1)
    # contentPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.ViewSwitcher/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout'
    # contentView = driver.find_element_by_xpath(contentPath)
    titlePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.ViewSwitcher/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[2]'
    title = driver.find_element_by_xpath(titlePath).text
    if code in title:
        buyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.ViewSwitcher/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.Button'
        driver.find_element_by_xpath(buyPath).click()
        sleep(1)
    pwd = getPwd('fuYuan')['tradePwd']
    print(pwd)
    for i in pwd:
        if i.isdigit():
            code = getKeyCode(i)
            driver.press_keycode(78)
            # driver.press_keycode(code)
            print(code)
        elif i.islower():
            code = getKeyCode(i.upper())
            # driver.press_keycode(code)
            print(code)
        elif i.isupper():
            code = getKeyCode(i)
            driver.press_keycode(60)
            # driver.press_keycode(code)
            print(code)
        

    sleep(20)
    driver.quit()



def getfuYuanProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.sunline.android.sunline'
    settingData['appActivity'] = '.DefaultAlias'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    if isExist(driver, 4, 'com.sunline.android.sunline:id/cancel'):
        driver.find_element_by_id('com.sunline.android.sunline:id/cancel').click()
        sleep(1)

    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(2)
    allPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    allNum = driver.find_element_by_xpath(allPath).text
    availablePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[2]'
    availableNum = numFromStr(driver.find_element_by_xpath(availablePath).text)
    param = {
        'method':0,
        'tableName':'fuYuan0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()
    



