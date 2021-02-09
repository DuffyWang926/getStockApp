import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist
from setting import getSetting
from mysql.initDB import initMysql
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyYingLi(param):
    code = param['code']
    isCash = param['isCash']
    stockNum = param['num']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.yxzq.stock'
    settingData['appActivity'] = '.enter.LauncherActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    loginYingLi(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    sleep(1)
    stockViewPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'
    stockView = driver.find_elements_by_xpath(stockViewPath)
    stockLen = len(stockView)
    if stockLen > 1:
        for i in range(stockLen):
            sleep(1)
    else:
        codeTextPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView'
        codeText = driver.find_element_by_xpath(codeTextPath).text
        if code in codeText:
            driver.find_element_by_xpath(codeTextPath).click()
            sleep(3)
    confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.Button'
    driver.find_element_by_xpath(confirmPath).click()
    sleep(2)
    amountChoosePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[1]'
    driver.find_element_by_xpath(amountChoosePath).click()
    sleep(1)
    
    amountFlag = True
    while amountFlag:
        amountViewPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.ListView/android.view.View'
        amountView = driver.find_elements_by_xpath(amountViewPath)
        amountLen = len(amountView)
        amountCheckIndex = 0
        for i in range(amountLen):
            text = amountView[i].text
            if isCashAll:
                if '不足' in text:
                    amountCheckIndex = i -1
                    if amountCheckIndex < 1:
                        amountCheckIndex = 0
                    amountFlag = False
                    break
            else:
                if stockNum in text:
                    amountCheckIndex = i
                    amountFlag = False
                    break
        amountView[amountCheckIndex].click()
    amountConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]'
    driver.find_element_by_xpath(amountConfirmPath).click()
    sleep(1)
    agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]/android.widget.TextView'
    driver.find_element_by_xpath(agreePath).click()
    sleep(1)
    immediatePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]'
    # driver.find_element_by_xpath(immediatePath).click()
    endText = driver.find_element_by_xpath(immediatePath).text
    sleep(1)
    sleep(10)
    driver.quit()

def getYingLiProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.yxzq.stock'
    settingData['appActivity'] = '.enter.LauncherActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    loginYingLi(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(2)
    allId = 'com.yxzq.stock:id/tv_total_asset'
    allNum = driver.find_element_by_id(allId).text
    availablePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.view.ViewGroup[2]/android.widget.TextView[2]'
    availableNum = driver.find_element_by_xpath(availablePath).text
    param = {
        'method':0,
        'tableName':'yingLi0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()
    

def loginYingLi(driver):
    cancelId = 'com.yxzq.stock:id/iv_close'
    cancelIdNext = 'com.yxzq.stock:id/ic_close'
    if isExist(driver, 4, cancelId):
        driver.find_element_by_id(cancelId).click()
        sleep(1)
    if isExist(driver, 4, cancelIdNext):
        driver.find_element_by_id(cancelIdNext).click()
        sleep(1)

    