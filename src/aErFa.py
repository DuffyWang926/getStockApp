import os
from time import sleep
import unittest
from appium import webdriver
from utils.verify import isExist
from setting import getSetting
from mysql.initDB import initMysql
from src.getPwdData import getPwd, getKeyCode
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyAErFa(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    stockNum = param['num']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.hkbeiniu.securities'
    settingData['appActivity'] = '.home.activity.UPHKLauncherActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    initApp(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("可认购")').click()
    sleep(2)
    codeListPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'
    codeList = driver.find_elements_by_xpath(codeListPath)
    if len(codeList) < 2:
        codePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[2]'
        codeText = driver.find_element_by_xpath(codePath).text
        print(codeText)
        if code in codeText:
            buyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView'
            driver.find_element_by_xpath(buyPath).click()
            sleep(1)
    if not isCash:
        typePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
        driver.find_element_by_xpath(typePath).click()
        sleep(1)
        financePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView'
        driver.find_element_by_xpath(financePath).click()
        sleep(1)
        financeRatioPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
        driver.find_element_by_xpath(financeRatioPath).click()
        sleep(1)
        
        financeRatioFlag = True
        while financeRatioFlag:
            financeRatioListPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView'
            financeRatioList = driver.find_elements_by_xpath(financeRatioListPath)
            financeRatioListLen = len(financeRatioList)
            for i in range(financeRatioListLen):
                ratioText = financeRatioList[i].text
                if '90' in ratioText:
                    financeRatioFlag = False
                    ratioEndPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.TextView'
                    driver.find_element_by_xpath(ratioEndPath).click()
                    sleep(1)
            
            if financeRatioFlag:
                driver.swipe(400,1500,400,1000,300)
    numPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
    numText = driver.find_element_by_xpath(numPath).text
    if stockNum not in numText:
        driver.find_element_by_xpath(numPath).click()
        sleep(1)
        numFlag = True
        while numFlag:
            numListPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView'
            numList = driver.find_elements_by_xpath(numListPath)
            numLen = len(numList)
            for i in range(numLen):
                numText = numList[i].text
                if stockNum in numText:
                    numFlag = False
                    index = str(i+1)
                    numConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[ ' + index + ']/android.widget.TextView'
                    driver.find_element_by_xpath(numConfirmPath).click()
                    sleep(1)
            
            if numFlag:
                driver.swipe(400,660,400,550,300)
    confimPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.Button'
    driver.find_element_by_xpath(confimPath).click()
    sleep(1)
    pwd = getPwd('youYu')['tradePwd']
    print(pwd)
    getKeyCode(driver, pwd)
    sleep(1)
    driver.quit()

def getAErFaProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.hkbeiniu.securities'
    settingData['appActivity'] = '.home.activity.UPHKLauncherActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    allPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView'
    allNum = driver.find_element_by_xpath(allPath).text
    availablePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView'
    availableNum = driver.find_element_by_xpath(availablePath).text
    param = {
        'method':0,
        'tableName':'aErFa0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()

def initApp(driver):
    changePwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]'
    if isExist(driver,2,changePwdPath):
        driver.find_element_by_xpath(changePwdPath).click()