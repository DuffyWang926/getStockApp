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
def buyRuiFeng(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.tsci.rfg'
    settingData['appActivity'] = 'com.konsonsmx.market.module.base.ui.FlashADActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    loginApp(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股申购")').click()
    sleep(1)
    codeListPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ExpandableListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout'
    codeList = driver.find_elements_by_xpath(codeListPath)
    codeListLen = len(codeList)
    if codeListLen < 2:
        codeChoosePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ExpandableListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[2]'
    driver.find_element_by_xpath(codeChoosePath).click()
    sleep(1)
    codeConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button'
    driver.find_element_by_xpath(codeConfirmPath).click()
    sleep(1)
    loginApp(driver,codeConfirmPath)
    agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button'
    driver.find_element_by_xpath(agreePath).click()
    sleep(2)
    agreeNextConfirm = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageView'
    driver.find_element_by_xpath(agreeNextConfirm).click()
    sleep(1)
    agreeNextPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button'
    driver.find_element_by_xpath(agreeNextPath).click()
    sleep(1)
    if not isCash:
        typePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]'
        driver.find_element_by_xpath(typePath).click()
        sleep(1)
        driver.swipe(200,2161,200,2002,300)
        sleep(1)
        typeConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button[2]'
        driver.find_element_by_xpath(typeConfirmPath).click()
        sleep(1)
    numChoosePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]'
    driver.find_element_by_xpath(numChoosePath).click()
    sleep(1)
    oneNum = int(param['oneNum'])
    num = int(param['num'])
    numLen = int(num/oneNum -1)
    print(numLen)
    for i in range(numLen):
        driver.swipe(200,2050,200,2000,300)
        sleep(1)
    numConfirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button[2]'
    driver.find_element_by_xpath(numConfirmPath).click()
    sleep(1)
    confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button'
    driver.find_element_by_xpath(confirmPath).click()
    sleep(1)
    


    sleep(10)
    # driver.quit()

def loginApp(driver,*others):
    pwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'
    if isExist(driver, 2, pwdPath):
        driver.find_element_by_xpath(pwdPath).click()
        sleep(1)
        pwd = getPwd('ruiFeng')['logInPwd']
        getKeyCode(driver, pwd)
        sleep(1)
        confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button'
        driver.find_element_by_xpath(confirmPath).click()
        sleep(2)
    if others:
        lastPath = others[0]
        if isExist(driver, 2, lastPath):
            driver.find_element_by_xpath(lastPath).click()
            sleep(1)