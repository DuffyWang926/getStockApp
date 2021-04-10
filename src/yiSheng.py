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
def buyYiSheng(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    # settingData['appPackage'] = 'com.miui.home'
    # settingData['appActivity'] = '.launcher.Launcher'
    settingData['appPackage'] = 'com.yszq.ysapp'
    settingData['appActivity'] = '.activity.main.LaunchActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    sleep(1)
    codeListPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout'
    codeList = driver.find_elements_by_xpath(codeListPath)
    codeListLen = len(codeList)
    if codeListLen < 2:
        buyCodePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[6]/android.widget.TextView[3]'
        driver.find_element_by_xpath(buyCodePath).click()
        sleep(1)
    loginApp(driver, buyCodePath)
    
    sleep(10)
    # driver.quit()

def loginApp(driver, buyCodePath):
    namePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.EditText'
    nameText = driver.find_element_by_xpath(namePath).text
    pwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.EditText'
    driver.find_element_by_xpath(pwdPath).click()
    sleep(1)
    account = getPwd('yiSheng')['account']
    if account in nameText:
        pwd = getPwd('yiSheng')['tradePwd']
        getKeyCode(driver, pwd)
        sleep(1)
        loginPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button'
        driver.find_element_by_xpath(loginPath).click()
        sleep(1)
    else:
        pwd = getPwd('yiSheng')['logInPwd']
        getKeyCode(driver, pwd)
        sleep(1)
        loginPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button'
        driver.find_element_by_xpath(loginPath).click()
        sleep(1)
        driver.find_element_by_xpath(buyCodePath).click()
        sleep(1)
        pwd = getPwd('yiSheng')['tradePwd']
        getKeyCode(driver, pwd)
        sleep(1)
        loginPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button'
        driver.find_element_by_xpath(loginPath).click()
        sleep(1)
    driver.find_element_by_xpath(buyCodePath).click()
    sleep(1)