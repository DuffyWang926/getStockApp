import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd, getKeyCode
from utils.verify import isExist
from utils.readImg import readNum
from setting import getSetting
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyGuoDu(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']

    # getkey(param)
    
    # settingIndex = param['setIndex']
    # settingData = getSetting(settingIndex)
    # settingData['appPackage'] = 'com.tsci.gds'
    # settingData['appActivity'] = 'com.konsonsmx.market.module.base.ui.FlashADActivity'
    # desired_caps = settingData
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # driver.close_app();            
    # sleep(3)
    # driver.launch_app(); 
    # sleep(6)
    # tradePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RadioGroup/android.widget.RadioButton[5]'
    
    # accountPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText'
    # accountPathNext = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText'
    # pwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'
    # pwdPathNext = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'
    # if not isExist(driver, 2, accountPath):
    #     accountPath = accountPathNext
    #     pwdPath = pwdPathNext
    #     if not isExist(driver, 2, accountPath):
    #         driver.find_element_by_xpath(tradePath).click()
    #         sleep(1)

    # driver.find_element_by_xpath(accountPath).clear()
    # driver.find_element_by_xpath(accountPath).click()
    # acount = getPwd('guoDu')['account']
    # getKeyCode(driver,acount)
    # sleep(1)
    # driver.find_element_by_xpath(pwdPath).click()
    # pwd = getPwd('guoDu')['logInPwd']
    # getKeyCode(driver,pwd)
    # sleep(1)
    # confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button'
    # driver.find_element_by_xpath(confirmPath).click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("可认购")').click()
    # sleep(1)
    
    
    sleep(10)
    # driver.quit()
def getkey(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.guodu.token'
    settingData['appActivity'] = 'md58eeaaf6ecd101572fa448c5104fa33aa.BrokerListActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(6)
    pwd = getPwd('guoDu')['tradePwd']
    getKeyCode(driver,pwd)
    sleep(3)
    print(driver.page_source)
    driver.get_screenshot_as_file('./guodu.png')
    # screenshotBase64 = driver.get_screenshot_as_base64()
    # print(screenshotBase64)
    # keyLeftPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]'
    # keyLeftId = 'com.guodu.token:id/token_left_textview'
    # # keyLeft = driver.find_element_by_xpath(keyLeftPath).text
    # keyLeft = driver.find_element_by_id(keyLeftId).text
    # print(keyLeft)
    # keyRightPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]'
    # keyRightId = 'com.guodu.token:id/token_right_textview'
    # # keyRight = driver.find_element_by_xpath(keyRightPath).text
    # keyRight = driver.find_element_by_xpath(keyRightId).text
    # print(keyRight)
    # key = keyLeft + keyRight
    # print(key)
    # timePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.TextView'
    # timeId = 'com.guodu.token:id/sec_textview'
    # time = driver.find_element_by_xpath(timeId).text
    # # time = driver.find_element_by_xpath(timePath).text
    # print(time)

    
    keyListPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView'
    keyList = driver.find_elements_by_xpath(keyListPath)
    print(len(keyList))
    for i in keyList:
        text = i.text
        print(text)
