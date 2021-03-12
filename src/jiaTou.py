import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist
from setting import getSetting
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyJiaTou(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    stockNum = param['num']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.kaisa.kaisafinstock'
    settingData['appActivity'] = '.MainActivity'
    desired_caps = settingData
    # desired_caps = {
    #     'platformName':'Android',
    #     'platformVersion':'10',
    #     'deviceName':'2214c691',
    #     'appPackage':'com.kaisa.kaisafinstock',
    #     'noReset':True,
    #     'appActivity':'.MainActivity',
    # }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    sleep(1)
    stockPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup'
    stockView = driver.find_elements_by_xpath(stockPath)
    stockLen = len(stockView)
    if stockLen > 2:
        for i in range(stockLen):
            stockIndex = str(i)
            codePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup[' + stockIndex +']/android.widget.LinearLayout[1]/android.widget.TextView[2]'
            codeText = driver.find_element_by_xpath(codePath).text
            if code in codeText:
                buyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup[' + stockIndex +']/android.widget.TextView'
                driver.find_element_by_xpath(buyPath).click()
                sleep(1)
    else:
        buyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView'
        driver.find_element_by_xpath(buyPath).click()
        sleep(1)
    if not isCash:
        financingId = 'com.kaisa.kaisafinstock:id/rz_subcript_cl'
        driver.find_element_by_id(financingId).click()
        sleep(1)

    
    amountFlag = True
    sum = 0
    lastText = ''

    while(amountFlag):
        amountPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup'
        amountView = driver.find_elements_by_xpath(amountPath)
        amountLen = len(amountView)
        index = str(sum+1)
        amountPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[' + index +']/android.view.ViewGroup/android.widget.TextView[1]'
        if sum == 0:
            amountView[1].click()
        else:
            amountView[sum].click()
        sleep(2)
        amountText = driver.find_element_by_xpath(amountPath).text
        if isFinancingAll:
            if lastText == amountText:
                amountFlag = False

        elif stockNum in amountText:
            driver.find_element_by_xpath(amountPath).click()
            sleep(1)
            amountFlag = False
            break
        sum = 2
        lastText = amountText
    buyNextId = 'com.kaisa.kaisafinstock:id/subcription_next_tv'
    driver.find_element_by_id(buyNextId).click()
    sleep(1)
    confirmId = 'com.kaisa.kaisafinstock:id/confirm_subcript_tv'
    driver.find_element_by_id(confirmId).click()
    sleep(1)
    driver.quit()
    
def getJiaTouProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.kaisa.kaisafinstock'
    settingData['appActivity'] = '.MainActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("账户")').click()
    sleep(2)