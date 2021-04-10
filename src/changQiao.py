import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd, getKeyCode
from utils.verify import isExist
from setting import getSetting
from mysql.initDB import initMysql
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyChangQiao(param):
    code = param['code']
    codeName = param['codeName']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'global.longbridge.app.android'
    settingData['appActivity'] = 'global.longbridge.android.LaunchActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("市场")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("IPO 专区")').click()
    sleep(1)
    print(driver.page_source)
    codeListPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]/android.widget.ListView'
    codeList = driver.find_elements_by_xpath(codeListPath)
    codeListLen = len(codeList)
    if codeListLen < 2:
        codeNameTextPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]/android.widget.ListView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.TextView' 
        codeNameText = driver.find_element_by_xpath(codeNameTextPath).text
        print(codeNameText)
        if codeName in codeNameText:
            codeBuyPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]/android.widget.ListView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'
            driver.find_element_by_xpath(codeBuyPath).click()
            sleep(1)
    pwd = getPwd('changQiao')['tradePwd']
    getKeyCode(driver, pwd)
    sleep(1)
    numChoosePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]'
    driver.find_element_by_xpath(numChoosePath).click()
    sleep(1)
    if isFinancingAll:
        choosePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]/android.widget.Button[2]'
    else:
        choosePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]/android.widget.Button[1]'
    driver.find_element_by_xpath(choosePath).click()
    sleep(1)  
    confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[5]/android.view.View[3]/android.widget.Button' 
    driver.find_element_by_xpath(confirmPath).click()
    sleep(1)
    driver.quit()
    

def getChangQiaoProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'global.longbridge.app.android'
    settingData['appActivity'] = 'global.longbridge.android.LaunchActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    sleep(1)
    allId = 'global.longbridge.app.android:id/tv_summary_value'
    allNum = driver.find_element_by_id(allId).text
    availableId = 'global.longbridge.app.android:id/tv_cash_value'
    availableNum = driver.find_element_by_id(availableId).text
    param = {
        'method':0,
        'tableName':'changQiao0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()
    
   