import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist
from setting import getSetting
import math
from mysql.initDB import initMysql
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyTiger(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.tigerbrokers.stock'
    settingData['appActivity'] = '.ui.StartupActivity'
    desired_caps = settingData
    # desired_caps = {
    #     'platformName':'Android',
    #     'platformVersion':'10',
    #     'deviceName':'2214c691',
    #     'appPackage':'com.tigerbrokers.stock',
    #     'noReset':True,
    #     'appActivity':'.ui.StartupActivity',
    # }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    loginTiger(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(2)
    if isExist(driver, 4, 'com.tigerbrokers.stock:id/btn_cancel') :
        driver.find_element_by_id('com.tigerbrokers.stock:id/btn_cancel').click()
        sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("IPO")').click()
    sleep(3)
    hkStockPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]'
    driver.find_element_by_xpath(hkStockPath).click()
    # driver.find_element_by_android_uiautomator('new UiSelector().text("港股")').click()
    sleep(1)

    # buyPath='//android.widget.TextView[contains(@text,"(' + code + '.HK)")]/parent::*/following-sibling::android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    # driver.find_element_by_xpath(buyPath).click()
    # sleep(1)
    # if not isCash:
    #     driver.find_element_by_id('com.juniorchina.jcstock:id/iv_margin').click()

    # numPath = 'new UiSelector().textContains("%d")'%(stockNum)
    # driver.find_element_by_android_uiautomator(numPath).click()
    # sleep(1)
    driver.quit()


    

def getTigerProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.tigerbrokers.stock'
    settingData['appActivity'] = '.ui.StartupActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    loginTiger(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(2)
    if isExist(driver, 4, 'com.tigerbrokers.stock:id/btn_cancel') :
        driver.find_element_by_id('com.tigerbrokers.stock:id/btn_cancel').click()
        sleep(1)

    allId = 'com.tigerbrokers.stock:id/text_asset_total'
    allNum = str(float( '%.2f' % (float(driver.find_element_by_id(allId).text.replace(',','')) * 7.7)))
    availableId = 'com.tigerbrokers.stock:id/text_assets_value_left'
    availableNum = driver.find_element_by_id(availableId).text
    param = {
        'method':0,
        'tableName':'tiger0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()

def loginTiger(driver):
    if isExist(driver, 4, 'com.tigerbrokers.stock:id/btn_cancel') :
        driver.find_element_by_id('com.tigerbrokers.stock:id/btn_cancel').click()
        sleep(1)