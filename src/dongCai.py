import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd, getKeyCode
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
    stockNum = param['num']
    # stockNumVal = param['numVal']
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
    codeText = 'new UiSelector().text("' + code +'")'
    codeParentView = driver.find_element_by_android_uiautomator(codeText).parent
    codeParentView.find_element_by_android_uiautomator('new UiSelector().text("认购")').click()
    sleep(1)
    pwd = getPwd('dongCai')['tradePwd']
    print(pwd)
    getKeyCode(driver, pwd)
    sleep(3)
    if isCash:
        cashText = 'new UiSelector().text("现金")'
        driver.find_element_by_android_uiautomator(cashText).click()
    amountChooseUi = 'new UiSelector().text("请选择认购股数")'
    driver.find_element_by_android_uiautomator(amountChooseUi).click()
    sleep(1)
    
    amountFlag = True
    amountCheckIndex = ''
    while amountFlag:
        amountViewPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        amountView = driver.find_elements_by_xpath(amountViewPath)
        amountLen = len(amountView) - 1
        print(amountLen)
        for i in range(amountLen):
            index = str(i + 1)
            print(index)
            if isCashAll:
                amountOutText = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['+ index +']/android.view.ViewGroup/android.widget.TextView[2]'
                if isExist(driver, 2, amountOutText):
                    amountFlag = False
                    amountCheckIndex = str(i)
                    break
            elif isCash:
                amountTextPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['+ index +']/android.view.ViewGroup/android.widget.TextView'
                amountText = driver.find_element_by_xpath(amountTextPath).text
                if stockNum in amountText:
                    amountFlag = False
                    amountCheckIndex = str(i+1)
                    break
            elif isFinancingAll:
                testUi = 'new UiSelector().textContains("不足")'
                if isExist(amountView[i], 1, testUi):
                    test = amountView[i].find_element_by_android_uiautomator('new UiSelector().textContains("不足")').text
                    print(test)
                    amountFlag = False
                    amountCheckIndex = str(i)
                    break
            else:
                amountTextPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['+ index +']/android.view.ViewGroup/android.widget.TextView'
                amountText = driver.find_element_by_xpath(amountTextPath).text
                if stockNum in amountText:
                    amountFlag = False
                    amountCheckIndex = str(i+1)
                    break
                
        if amountFlag:
            driver.swipe(200,1760,200,1610,300)
            sleep(1)
    amountCheckPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[' + amountCheckIndex +']/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
    print(amountCheckPath)
    driver.find_element_by_xpath(amountCheckPath).click()
    sleep(1)
    agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]'
    driver.find_element_by_xpath(agreePath).click()
    sleep(1)
    confirmPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
    driver.find_element_by_xpath(confirmPath).click()
    sleep(1)
    submitUi = 'new UiSelector().textContains("确认认购")'
    driver.find_element_by_android_uiautomator(submitUi).click()
    sleep(1)
    pwd = getPwd('dongCai')['tradePwd']
    print(pwd)
    getKeyCode(driver, pwd)
    sleep(1)
    endUi = 'new UiSelector().text("确认")'
    if isExist(driver,1,endUi):
        driver.find_element_by_android_uiautomator(endUi).click()
    sleep(3)
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
    