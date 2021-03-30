import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist
from setting import getSetting
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyYaoCai(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    stockNum = param['num']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.brightsmart.android.etnet'
    settingData['appActivity'] = 'com.etnet.android.iq.Welcome'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    tradePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RadioGroup/android.widget.RadioButton[5]'
    driver.find_element_by_xpath(tradePath).click()
    sleep(1)
    loginYaoCai(driver)
    ipoPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RadioGroup/android.widget.RadioButton[4]'
    driver.find_element_by_xpath(ipoPath).click()
    sleep(5)
    codeListPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View'
    codeListView = driver.find_elements_by_xpath(codeListPath)
    codeLen = len(codeListView)
    for i in range(codeLen):
        index = str(i + 1)
        codePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[' + index + ']/android.view.View[1]'
        codeText = driver.find_element_by_xpath(codePath).text
        print(codeText)
        print(code in codeText)
        if code in codeText:
            buyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[' + index + ']/android.view.View[4]/android.view.View[2]/android.view.View'
            driver.find_element_by_xpath(buyPath).click()
            sleep(4)
            break
    driver.swipe(200,2100,200,1000,300)
    sleep(1)
    agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[11]/android.view.View/android.view.View/android.view.View[1]'
    driver.find_element_by_xpath(agreePath).click()
    sleep(4)
    print(driver.page_source)
    applyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.GridView[1]/android.view.View[12]/android.view.View[1]/android.widget.Button'
    
    if not isCash:
        financePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.GridView[1]/android.view.View[6]/android.view.View[2]/android.widget.RadioButton[2]'
        if isExist(driver, 2, financePath):
            driver.find_element_by_xpath(financePath).click()
            sleep(1)
            applyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.GridView/android.view.View[16]/android.view.View[1]/android.widget.Button'
            amountFlagPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.GridView[1]/android.view.View[7]/android.view.View[2]/android.widget.Spinner'

    amountFlagPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.GridView[1]/android.view.View[7]/android.view.View[2]/android.widget.Spinner'
    if not isExist(driver, 2, amountFlagPath):
        amountFlagPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.GridView[1]/android.view.View[6]/android.view.View[2]/android.widget.Spinner'

    amountInitText = driver.find_element_by_xpath(amountFlagPath).text
    print(amountInitText)
    if not isFinancingAll:
        if amountInitText != stockNum:
            driver.find_element_by_xpath(amountFlagPath).click()
            sleep(1)
    print(applyPath)
    driver.find_element_by_xpath(applyPath).click()
    sleep(2)
    confimPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.GridView[2]/android.view.View/android.view.View[1]/android.widget.Button'
    # driver.find_element_by_xpath(confimPath).click()
    print(driver.find_element_by_xpath(confimPath).text)
    sleep(10)
    # driver.quit()

def getYaoCaiProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.brightsmart.android.etnet'
    settingData['appActivity'] = 'com.etnet.android.iq.Welcome'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    tradePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RadioGroup/android.widget.RadioButton[5]'
    driver.find_element_by_xpath(tradePath).click()
    sleep(1)
    loginYaoCai(driver)
    
    allId = 'com.brightsmart.android.etnet:id/Portfolio'
    allNum = driver.find_element_by_id(allId).text
    availableId = 'com.brightsmart.android.etnet:id/AvailPurchase'
    availableNum = driver.find_element_by_id(availableId).text

    print(allNum)
    print(availableNum)
    print(driver.page_source)
    print(driver.contexts)
    # driver.switch_to.context(driver.contexts[1])
    
    
def loginYaoCai(driver):
    account = getPwd('yaoCai')['account']
    driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys(account)
    logInPwd = getPwd('yaoCai')['logInPwd']
    driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys(logInPwd)
    driver.find_element_by_id('com.brightsmart.android.etnet:id/login').click()
    sleep(10)
