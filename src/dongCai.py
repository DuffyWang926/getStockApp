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
def buyDongCai(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.eastmoney.android.lead'
    settingData['appActivity'] = 'com.eastmoney.android.berlin.activity.MainActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    loginDongCai(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    sleep(2)
    driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "认购中")]').click()
    sleep(1)
    # if isExist(driver,'com.tigerbrokers.stock:id/btn_cancel') :
    #     driver.find_element_by_id('com.tigerbrokers.stock:id/btn_cancel').click()
    #     sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("IPO")').click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("港股")').click()
    # sleep(1)

    # buyPath='//android.widget.TextView[contains(@text,"(' + code + '.HK)")]/parent::*/following-sibling::android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    # driver.find_element_by_xpath(buyPath).click()
    # sleep(1)
    # if not isCash:
    #     driver.find_element_by_id('com.juniorchina.jcstock:id/iv_margin').click()

    # numPath = 'new UiSelector().textContains("%d")'%(stockNum)
    # driver.find_element_by_android_uiautomator(numPath).click()
    # sleep(1)
    driver.quit()

def getDongCaiProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.eastmoney.android.lead'
    settingData['appActivity'] = 'com.eastmoney.android.berlin.activity.MainActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    loginDongCai(driver)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(2)
    allId = 'com.eastmoney.android.lead:id/value_all_asset'
    allNum = driver.find_element_by_id(allId).text
    availablePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[2]/android.view.ViewGroup[2]/android.widget.TextView[2]'
    availableNum = driver.find_element_by_xpath(availablePath).text
    param = {
        'method':0,
        'tableName':'dongCai0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()

    print(allNum)
    print(availableNum)

def loginDongCai(driver):
    if isExist(driver,4,'com.eastmoney.android.lead:id/riv_card') :
        driver.find_element_by_id('com.eastmoney.android.lead:id/riv_card').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("关闭")').click()
        sleep(1)
    