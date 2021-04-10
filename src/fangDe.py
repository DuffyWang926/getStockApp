import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd, getKeyCode
from utils.verify import isExist
from setting import getSetting
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyFangDe(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    stockNum = param['num']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.fdzq.app'
    settingData['appActivity'] = '.activity.MainActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(6)
    initApp(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("IPO")').click()
    sleep(1)
    codeListPath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout'
    codeList = driver.find_elements_by_xpath(codeListPath)
    codeListLen = len(codeList)
    if codeListLen < 2:
        buyCodePath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[3]'
        buyCodeText = driver.find_element_by_xpath(buyCodePath).text
        if '申购' not in buyCodeText:
            buyCodePath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[4]'
        driver.find_element_by_xpath(buyCodePath).click()
        sleep(1)
    loginApp(driver, buyCodePath)
    if isCash:
        cashPath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView'
        driver.find_element_by_xpath(cashPath).click()
        sleep(1)
    numChoosePath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.TextView'
    driver.find_element_by_xpath(numChoosePath).click()
    sleep(1)
    
    numFlag = True
    while numFlag:
        numListPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView[1]'
        numList = driver.find_elements_by_xpath(numListPath)
        numListLen = len(numList)
        for i in range(numListLen):
            numText = numList[i].text
            if not isFinancingAll:
                if stockNum in numText:
                    numFlag = False
                    numList[i].click()
                    sleep(1)
        if numFlag:
            driver.swipe(200,2058,200,1902,300)
    
    numConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView[2]'
    driver.find_element_by_xpath(numConfirmPath).click()
    sleep(1)
    buyConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button'
    driver.find_element_by_xpath(buyConfirmPath).click()
    sleep(1)
    endPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView'
    driver.find_element_by_xpath(endPath).click()
    sleep(1)
    driver.quit()

def initApp(driver):
    closePath = '(//android.widget.ImageView[@content-desc="方德港美股"])[2]'
    if isExist(driver, 2, closePath):
        driver.find_element_by_xpath(closePath).click()
        sleep(1)
    
def loginApp(driver, buyCodePath):
    typePath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'
    if isExist(driver, 2, typePath):
        driver.find_element_by_xpath(typePath).click()
        sleep(1)
        pwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.EditText'
        driver.find_element_by_xpath(pwdPath).click()
        sleep(1)
        pwd = getPwd('fangDe')['logInPwd']
        getKeyCode(driver, pwd)
        sleep(1)
        loginPath = '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button'
        driver.find_element_by_xpath(loginPath).click()
        sleep(1)
        agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'
        driver.find_element_by_xpath(agreePath).click()
        sleep(1)
        driver.find_element_by_xpath(buyCodePath).click()
        sleep(1)
    tradePwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText'
    if isExist(driver, 2, tradePwdPath):
        driver.find_element_by_xpath(tradePwdPath).click()
        sleep(1)
        pwd = getPwd('fangDe')['tradePwd']
        getKeyCode(driver, pwd)
        sleep(1)
        loginPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button'
        driver.find_element_by_xpath(loginPath).click()
        sleep(1)