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
    # stockNumVal = param['numVal']
    stockNum = param['num']
    isCashAll = param['isCashAll']
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
    if isExist(driver, 4, 'com.tigerbrokers.stock:id/btn_cancel') :
        driver.find_element_by_id('com.tigerbrokers.stock:id/btn_cancel').click()
        sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("IPO")').click()
    sleep(3)
    print(driver.page_source)
    hkStockPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]'
    driver.find_element_by_xpath(hkStockPath).click()
    sleep(1)
    contentPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[9]/android.view.View'
    contentView = driver.find_elements_by_xpath(contentPath)
    contentLen = len(contentView)
    for i in range(contentLen):
        if contentLen > 0:
            index = '[' + str(i+1) + ']'
        else:
            index = ''
        titlePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[9]/android.view.View'+ index +'/android.view.View[1]/android.widget.TextView[2]'
        titlePathNext = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[9]/android.view.View'+ index +'/android.view.View[1]'
        if isExist(driver, 2, titlePath):
            itemTitle = driver.find_element_by_xpath(titlePath).text
        else:
            itemTitle = driver.find_element_by_xpath(titlePathNext).text
        if code in itemTitle:
            buyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[9]/android.view.View'+ index +'/android.view.View[9]/android.widget.Button[2]'
            driver.find_element_by_xpath(buyPath).click()
            sleep(2)
    immediatePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[20]/android.widget.Button'
    driver.find_element_by_xpath(immediatePath).click()
    sleep(2)
    if isCash:
        typePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]'
        driver.find_element_by_xpath(typePath).click()
        sleep(1)
        typeValPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]'
        typeVal = driver.find_element_by_xpath(typeValPath).text
        typeIndex = -1
        if '现金' in typeVal:
            typeIndex = str(1)
        else:
            typeIndex = str(2)
        typeChoosePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[' + typeIndex +']/android.view.View[1]/android.view.View'
        driver.find_element_by_xpath(typeChoosePath).click()
        sleep(1)
        typeConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[2]/android.widget.Button'
        driver.find_element_by_xpath(typeConfirmPath).click()
        sleep(1)
        amountChoosePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[10]'
        driver.find_element_by_xpath(amountChoosePath).click()
        sleep(1)
        
        
        amountFlag = True
        while amountFlag:
            amountViewPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[3]/android.view.View'
            amountView = driver.find_elements_by_xpath(amountViewPath)
            amountViewLen = len(amountView) -3
            for i in range(amountViewLen):
                amountIndex = str(i + 1)
                amountPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[3]/android.view.View['+ amountIndex +']/android.view.View[1]'
                amountText = driver.find_element_by_xpath(amountPath).text
                if isCashAll:
                    if '最大' in amountText:
                        amountFlag = False
                        
                else:
                    if stockNum in amountText:
                        amountFlag = False
                if not amountFlag:
                    amountCheckPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[3]/android.view.View['+ amountIndex +']/android.view.View[3]/android.view.View/android.view.View/android.view.View' 
                    driver.find_element_by_xpath(amountCheckPath).click()
                    sleep(1)
                    break
            if amountFlag:
               driver.swipe(200,1760,200,1600,300)
        amountConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.widget.Button'
        driver.find_element_by_xpath(amountConfirmPath).click()
        sleep(1)
        driver.swipe(200,1760,200,1000,300)
        confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Button'        
        driver.find_element_by_xpath(confirmPath).click()
        sleep(1)
        agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[11]/android.widget.CheckBox'
        driver.find_element_by_xpath(agreePath).click()
        sleep(1)
        submitPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.widget.Button[2]'
        # driver.find_element_by_xpath(submitPath).click()
        test = driver.find_element_by_xpath(submitPath).text
        sleep(1)
    else:
        financePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[9]/android.view.View'
        driver.find_element_by_xpath(financePath).click()
        sleep(2)
        fifteenPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View'
        driver.find_element_by_xpath(fifteenPath).click()
        sleep(1)
        financeTypeConfirm = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[2]/android.widget.Button'
        driver.find_element_by_xpath(financeTypeConfirm).click()
        sleep(1)
        amountChoose = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[13]/android.view.View'
        driver.find_element_by_xpath(amountChoose).click()
        sleep(1)
        amountFlag = True
        while(amountFlag):
            amountViewPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[3]/android.view.View'
            amountView = driver.find_elements_by_xpath(amountViewPath)
            amountLen = len(amountView) - 3
            print(amountLen)
            for i in range(amountLen):
                index = str(i+1)
                amountPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[3]/android.view.View[' + index +']/android.view.View[1]'
                amountText = driver.find_element_by_xpath(amountPath).text
                print(amountText)
                if '最大' in amountText:
                    amountFlag = False
                    amountCheckPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[3]/android.view.View[' + index +']/android.view.View[3]/android.view.View/android.view.View/android.view.View'
                    driver.find_element_by_xpath(amountCheckPath).click()
                    sleep(1)
            if amountFlag:
                driver.swipe(200,1760,200,1600,300)
        amountConfirm = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.widget.Button'
        driver.find_element_by_xpath(amountConfirm).click()
        sleep(1)
        driver.swipe(200,1760,200,1000,300)
        confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Button'        
        driver.find_element_by_xpath(confirmPath).click()
        sleep(1)
        agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[12]/android.widget.CheckBox'
        driver.find_element_by_xpath(agreePath).click()
        sleep(1)
        submitPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.widget.Button[2]'
        driver.find_element_by_xpath(submitPath).click()
        sleep(1)
    stockPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.widget.Button[2]'
    driver.find_element_by_xpath(stockPath).click()
    sleep(10)
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