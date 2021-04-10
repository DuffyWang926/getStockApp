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
def buyYiTaoJin(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.gfhkstore.android'
    settingData['appActivity'] = 'com.gf.gfglobal.HomeActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    initApp(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股申购")').click()
    sleep(1)
    codeListPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'
    codeList = driver.find_elements_by_xpath(codeListPath)
    codeListLen = len(codeList)
    if codeListLen < 2:
        buyCodePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
        driver.find_element_by_xpath(buyCodePath).click()
        sleep(1)
    loginApp(driver)
    
    sleep(10)
    # driver.quit()
def initApp(driver):
    closePath = '//android.widget.Button[@content-desc="closeImage"]'
    if isExist(driver, 2, closePath):
        driver.find_element_by_xpath(closePath).click()
        sleep(1)

def loginApp(driver):
    pwdPath = '//android.widget.Button[@content-desc="login-trade-input-pwd"]'
    driver.find_element_by_xpath(pwdPath).click()
    sleep(1)
    pwd = getPwd('yiTaoJin')['tradePwd']
    getKeyCode(driver, pwd)
    sleep(1)