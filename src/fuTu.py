import os
from time import sleep
import unittest
from appium import webdriver
from utils.verify import numFromStr, isNumber, isExist
from setting import getSetting
from mysql.initDB import initMysql
from src.getPwdData import getPwd, getKeyCode
import time
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
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
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
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    sleep(1)
    buyPath='//*[@text="' + code + '"]/parent::*/parent::*/following-sibling::android.widget.RelativeLayout/android.widget.TextView'
    if isExist(driver,2,buyPath):
        driver.find_element_by_xpath(buyPath).click()
        sleep(4)
        print(driver.page_source)
        financeTimePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[4]'
        financingPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[5]/android.view.View/android.view.View[5]/android.view.View'
        cashPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[4]/android.view.View/android.view.View[3]/android.view.View'
        cashNextPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[27]/android.view.View[4]/android.view.View/android.view.View[3]/android.view.View'
        financingNextPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[27]/android.view.View[5]/android.view.View/android.view.View[5]/android.view.View'
        tipPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]'
        nextFlag = False
        if isExist(driver,2,cashNextPath):
            cashPath = cashNextPath
            financingPath = financingNextPath
            nextFlag = True
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

            if nextFlag:
                otherPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[22]'
            else:
                otherPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[21]'
            driver.find_element_by_xpath(otherPath).click()
            sleep(1)
            num = str(4 + 2*numFromStr(stockNumVal))
            if isCashAll:
                if nextFlag:
                    cashAllPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View[2]'
                else:
                    cashAllPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[25]/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View[2]'
                driver.find_element_by_xpath(cashAllPath).click()
                sleep(1)
            elif isFinancingAll:
                if nextFlag:
                    finacingAllPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View[3]'
                else:
                    finacingAllPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[25]/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View[3]'
                driver.find_element_by_xpath(finacingAllPath).click()
                sleep(1)

            else:
                if nextFlag:
                    numPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[26]/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View['+ num + ']/android.view.View[1]/android.widget.TextView'
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
            for i in pwd:
                index = i
                if i == '0':
                    index = 11
                pwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[35]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.widget.ListView/android.view.View[' + index + ']'
                driver.find_element_by_xpath(pwdPath).click()
                sleep(1)
            
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

def tradeFuTu(param):
    driver = initFuTu(param)
    searchPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.ImageView'
    if not isExist( driver, 2, searchPath):
        searchPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.ImageView'
    driver.find_element_by_xpath(searchPath).click()
    sleep(1)
    code = param['code']
    getKeyCode(driver,code)
    sleep(4)
    recordFlag = True
    while recordFlag:
        stockPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup'
        driver.find_element_by_xpath(stockPath).click()
        sleep(1)
        recordFlag = recordPrice(driver,param)
    sleep(10)

def initFuTu(param):
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
    return driver

def recordPrice(driver,param):
    pricePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
    maxPricePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView[2]'
    maxText = driver.find_element_by_xpath(maxPricePath).text
    if isNumber(maxText):
        nowPrice =  float(driver.find_element_by_xpath(pricePath).text[0:5])
        maxPrice = float(driver.find_element_by_xpath(maxPricePath).text)
        minPricePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.TextView[2]'
        minPrice = float(driver.find_element_by_xpath(minPricePath).text)
        todayPercentagePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]'
        todayPercentage = float(driver.find_element_by_xpath(todayPercentagePath).text[0:4])
        priceInit = param['priceInit']
        percentage = round((nowPrice - priceInit)/priceInit,2)
        tradeUp = param['tradeUp']
        tradeSum = param['tradeSum']
        tableName = 'code' + param['code']
        ticks = time.time()
        recordTime = int(ticks)
        print(recordTime)
        print(nowPrice)
        print(maxPrice)
        print(minPrice)

        param = {
            'method':0,
            'tableName':tableName,
            'nowPrice':nowPrice,
            'maxPrice':maxPrice,
            'minPrice':minPrice,
            'percentage':todayPercentage,
            'recordTime':recordTime,
        }
        initMysql(param)
        # if percentage > tradeUp:
        if False:
            tradeParam = {
                'nowPrice':nowPrice,
                'tradeSum':tradeSum
            }
            tradePrice(driver,tradeParam)
            return False
        else:
            backPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton'
            driver.find_element_by_xpath(backPath).click()
            sleep(1)
            return True

def tradePrice(driver,tradeParam):
    print(tradeParam)
    nowPrice = tradeParam['nowPrice']
    tradeSum = tradeParam['tradeSum']
    tradePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView'
    driver.find_element_by_xpath(tradePath).click()
    sleep(1)
    priceEditPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.EditText'
    driver.find_element_by_xpath(priceEditPath).clear()
    driver.find_element_by_xpath(priceEditPath).send_keys(str(nowPrice))
    sleep(1)
    numPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText'
    driver.find_element_by_xpath(numPath).clear()
    driver.find_element_by_xpath(numPath).send_keys(str(tradeSum))
    confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button'
    driver.find_element_by_xpath(confirmPath).click()
    sleep(1)
    # pwd = getPwd('fuTu','tradePwd')
    # getKeyCode(driver,pwd)
    # sleep(1)