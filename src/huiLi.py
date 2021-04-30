import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd,getKeyCode
from utils.verify import isExist
from setting import getSetting
from mysql.initDB import initMysql
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyHuiLi(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.hk.poems.poemsMobileFX'
    settingData['appActivity'] = 'PoemsMobileTabActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    accountPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.EditText[1]'
    driver.find_element_by_xpath(accountPath).clear()
    driver.find_element_by_xpath(accountPath).click()
    acount = getPwd('huiLi')['account']
    getKeyCode(driver,acount)
    sleep(1)
    pwdPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.EditText[2]'
    driver.find_element_by_xpath(pwdPath).click()
    pwd = getPwd('huiLi')['logInPwd']
    getKeyCode(driver,pwd)
    sleep(1)
    loginPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.Button[2]'
    driver.find_element_by_xpath(loginPath).click()
    sleep(5)
    confirmKeyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button'
    driver.find_element_by_xpath(confirmKeyPath).click()
    sleep(1)
    print(driver.page_source)
    keyPath = '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton'
    driver.find_element_by_xpath(keyPath).click()
    sleep(1)
    copyKeyPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    driver.find_element_by_xpath(copyKeyPath).click()
    sleep(1)
    confirmCopyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'
    driver.find_element_by_xpath(confirmCopyPath).click()
    sleep(5)
    acceptPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]'
    driver.find_element_by_xpath(acceptPath).click()
    sleep(5)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("认购新股")').click()
    # sleep(1)
    
    sleep(10)
    # driver.quit()
    
    
def getYouYuProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.ruifusoft.finance.app'
    settingData['appActivity'] = 'com.ruifusoft.ui.SplashActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    sleep(1)
    allPath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[3]'
    allNum = driver.find_element_by_xpath(allPath).text
    availablePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView[2]'
    availableNum = driver.find_element_by_xpath(availablePath).text
    param = {
        'method':0,
        'tableName':'youYu0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()
