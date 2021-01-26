import os
from time import sleep
import unittest
from appium import webdriver
from utils.verify import isExist
from utils.verify import numFromStr
from src.getPwdData import getPwd
from setting import getSetting
from mysql.initDB import initMysql
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_xpath('//*[@text="天猫国际"]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
# financingBtn.text
# financingBtn.get_attribute('checkable')
def buyFuTu(param):
    code = param['code']
    isCash = param['isCash']
    # stockNum = param['num']
    stockNumVal = param['numVal']
    # isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'cn.futu.trader'
    settingData['appActivity'] = '.launch.activity.LaunchActivity'
    desired_caps = settingData
    # desired_caps = {
    #     'platformName':'Android',
    #     'platformVersion':'10',
    #     'deviceName':'2214c691',
    #     'appPackage':'cn.futu.trader',
    #     'noReset':True,
    #     'appActivity':'.launch.activity.LaunchActivity'
    # }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    closeId = 'cn.futu.trader:id/close_popup_ad_view'
    if isExist(driver, 4, closeId):
        driver.find_element_by_id(closeId).click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    sleep(1)
    buyPath='//*[@text="' + code + '"]/parent::*/parent::*/following-sibling::android.widget.RelativeLayout/android.widget.TextView'
    if isExist(driver,2,buyPath):
        driver.find_element_by_xpath(buyPath).click()
        sleep(4)
        print(driver.page_source)
        print(driver.contexts)
        financeTimePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[4]'
        financingPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[5]/android.view.View/android.view.View[5]/android.view.View'
        cashPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[4]/android.view.View/android.view.View[3]/android.view.View'
        # financingDisablePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[5]/android.view.View/android.view.View[4]/android.view.View'
        if isExist(driver,2,cashPath):
            if not isCash:
                if isExist(driver,2,financingPath):
                    financingBtn = driver.find_element_by_xpath(financingPath)
                    financingBtn.click()
                    sleep(1)

            else:
                cashBtn = driver.find_element_by_xpath(cashPath)
                cashFlag = cashBtn.get_attribute('checked')
                if not cashFlag:
                    cashBtn.click()
                    sleep(1)

            otherPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[21]'
            driver.find_element_by_xpath(otherPath).click()
            sleep(1)
            num = str(4 + 2*numFromStr(stockNumVal))
            if isCashAll:
                cashAllPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[25]/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View[2]'
                driver.find_element_by_xpath(cashAllPath).click()
                sleep(1)
            else:
                numPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[25]/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View['+ num + ']/android.view.View[1]/android.widget.TextView'
                driver.find_element_by_xpath(numPath).click()
                sleep(1)
            nextStepPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[31]/android.view.View[2]/android.view.View[2]/android.view.View[5]'
            driver.find_element_by_xpath(nextStepPath).click()
            sleep(2)
            agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[34]/android.view.View[3]/android.view.View/android.view.View[1]'
            driver.find_element_by_xpath(agreePath).click()
            sleep(1)
            finishPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[35]/android.view.View[2]'
            # finishBtn = driver.find_element_by_xpath(finishPath)
            driver.find_element_by_xpath(finishPath).click()
            sleep(2)
            print(driver.page_source)
            pwd = getPwd('fuTu')['tradePwd']
            print(pwd[0])
            os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')
            # os.system('adb shell ime set io.appium.settings/.UnicodeIME')
            # os.system('adb shell ime set com.iflytek.inputmethod.miui/.FlyIME')
            # os.system('adb shell ime set com.baidu.input_mi/.ImeService')
            
            pwdPatha = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[35]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View[1]'
            driver.find_element_by_xpath(pwdPatha).click()
            driver.press_keycode(144)
            # driver.find_element_by_xpath(pwdPatha).set_value(3)
            # pwdPathb = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[35]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View[2]'
            # driver.find_element_by_xpath(pwdPathb).click()
            # driver.press_keycode(10)
        elif isExist(driver,2,financeTimePath):
            financingTime = driver.find_element_by_xpath(financeTimePath)
            text = financingTime.get_attribute('text')
            print(text)


    sleep(5)
    driver.quit()

def getFuTuProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'cn.futu.trader'
    settingData['appActivity'] = '.launch.activity.LaunchActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    closeId = 'cn.futu.trader:id/close_popup_ad_view'
    if isExist(driver, 4, closeId):
        driver.find_element_by_id(closeId).click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("今日盈亏")').click()
    sleep(1)
    allPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView'
    allNum = driver.find_element_by_xpath(allPath).text
    availablePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView'
    availableNum = driver.find_element_by_xpath(availablePath).text
    param = {
        'method':0,
        'tableName':'fuTu0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()
    