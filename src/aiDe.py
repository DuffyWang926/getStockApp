import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist
from setting import getSetting
from mysql.initDB import initMysql
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyAiDe(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'io.newtype.eddid.app'
    settingData['appActivity'] = 'com.eddid.home.ui.activity.LauncherActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(6)
    tipId = 'io.newtype.eddid.app:id/tv_notice_dialog_no_reminder'
    if isExist(driver, 4, tipId):
        driver.find_element_by_id(tipId).click()
        sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    sleep(5)
    contentPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View'
    contentView = driver.find_elements_by_xpath(contentPath)
    contentLen = len(contentView) -2
    for i in range(contentLen):
        index = str(i + 2)
        titlePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[' + index +']/android.view.View[1]'
        itemTitle = driver.find_element_by_xpath(titlePath).text
        if code in itemTitle:
            buyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[' + index +']/android.view.View[2]'
            driver.find_element_by_xpath(buyPath).click()
            sleep(2)
    confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.widget.Button'
    confirmBtn = driver.find_element_by_xpath(confirmPath).text
    print(confirmBtn)
    
    sleep(5)
    driver.quit()

def getAiDeProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'io.newtype.eddid.app'
    settingData['appActivity'] = 'com.eddid.home.ui.activity.LauncherActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(6)