import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist
from utils.verify import numFromStr
from setting import getSetting
from mysql.initDB import initMysql

# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
# following-sibling:: preceding-sibling::
def buyHuaShengTong(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.huasheng.stock'
    settingData['appActivity'] = 'com.hstong.app.launch.ui.Loading'
    desired_caps = settingData

    # desired_caps = {
    #     'platformName':'Android',
    #     'platformVersion':'10',
    #     'deviceName':'2214c691',
    #     'appPackage':'com.huasheng.stock',
    #     'noReset':True,
    #     'appActivity':'com.hstong.app.launch.ui.Loading',
    # }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(6)
    if isExist(driver, 4, 'com.huasheng.stock:id/button_cancel'):
        driver.find_element_by_id('com.huasheng.stock:id/button_cancel').click()
    if isExist(driver, 4, 'com.huasheng.stock:id/btn_close'):
        driver.find_element_by_id('com.huasheng.stock:id/btn_close').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    if isExist(driver, 3, 'android.widget.EditText') :
        pwd = getPwd('huaShengTong')['tradePwd']
        driver.find_element_by_class_name('android.widget.EditText').send_keys(pwd)
        driver.find_element_by_id('com.huasheng.stock:id/btn_login').click()
        sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("可认购")').click()
    sleep(1)
    codeExitPath = '//android.widget.TextView[contains(@text, "' + code + '")]'
    codePath = '//android.widget.TextView[contains(@text, "' + code + '")]/parent::*/parent::*/parent::*/following-sibling::android.widget.LinearLayout[4]/android.widget.TextView'
    if isExist(driver, 2, codeExitPath):
       codeBtn = driver.find_element_by_xpath(codePath)
       codeBtn.click()
       sleep(8)
    print(driver.page_source)
    
    if not isCash:
        
        financingPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.ListView[1]/android.view.View[2]'
        driver.find_element_by_xpath(financingPath).click()
        sleep(1)

    choosePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]'
    driver.find_element_by_xpath(choosePath).click()
    sleep(1)
    maxExistPath = '//android.view.View[contains(@text, "存入资金")]'
    if isCashAll or isFinancingAll:
        while not isExist(driver, 2, maxExistPath):
            driver.swipe(200,1600,200,1300,300)
        maxPath = '//android.view.View[contains(@text, "存入资金")]/parent::*/parent::*/preceding-sibling::android.view.View[1]/android.view.View'
        driver.find_element_by_xpath(maxPath).click()
        sleep(1)
    else:
        num = str(numFromStr(stockNumVal))
        numPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.ListView[2]/android.view.View[' + num +']/android.view.View[1]'
        driver.find_element_by_xpath(numPath).click()
        sleep(1)
    finishPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]'
    driver.find_element_by_xpath(finishPath).click()
    sleep(2)
    agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]'
    agreeBox = driver.find_element_by_xpath(agreePath)
    agreeBox.click()
    confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]'
    driver.find_element_by_xpath(confirmPath).click()
    sleep(1)
    endPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[3]'
    # endPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[4]'
    driver.find_element_by_xpath(endPath).click()
    sleep(5)
    driver.quit()

def getHuaShengTongProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.huasheng.stock'
    settingData['appActivity'] = 'com.hstong.app.launch.ui.Loading'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(6)
    if isExist(driver, 4, 'com.huasheng.stock:id/button_cancel'):
        driver.find_element_by_id('com.huasheng.stock:id/button_cancel').click()
    if isExist(driver, 4, 'com.huasheng.stock:id/btn_close'):
        driver.find_element_by_id('com.huasheng.stock:id/btn_close').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    if isExist(driver, 3, 'android.widget.EditText') :
        pwd = getPwd('huaShengTong')['tradePwd']
        driver.find_element_by_class_name('android.widget.EditText').send_keys(pwd)
        driver.find_element_by_id('com.huasheng.stock:id/btn_login').click()
        sleep(5)
    allPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[2]'
    allNum = driver.find_element_by_xpath(allPath).text
    availablePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[2]'
    availableNum = driver.find_element_by_xpath(availablePath).text
    param = {
        'method':0,
        'tableName':'huaShengTong0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()
    
