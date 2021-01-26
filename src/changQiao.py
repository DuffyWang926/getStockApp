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
def buyChangQiao(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'global.longbridge.app.android'
    settingData['appActivity'] = 'global.longbridge.android.LaunchActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("市场")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("IPO 专区")').click()
    sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("可认购")').click()
    # sleep(1)
    
    # path = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]'
    # driver.find_element_by_xpath(path).click()
    # sleep(1)
    # pwd = getPwd('dongFang')['tradePwd']
    # driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys(pwd)
    # loginPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[7]/android.view.View'
    # driver.find_element_by_xpath(loginPath).click()
    # sleep(1)
    # agreePath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.view.View[2]'
    # driver.find_element_by_xpath(agreePath).click()
    # sleep(5)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("新股申购")').click()
    # sleep(5)
    
    # driver.find_element_by_xpath('//*[contains(@text, "马上登录")]').click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    # sleep(1)
    # driver.find_element_by_id('com.lphtsccft.zlqqt2:id/main_account').click()
    # sleep(1)
    # path = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]'
    # driver.find_element_by_xpath(path).click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("打新股")').click()

    
    
    # driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    # sleep(1)
    # driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "认购中")]').click()
    # sleep(1)
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
    sleep(10)
    # driver.quit()
    

def getChangQiaoProperty(param):
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'global.longbridge.app.android'
    settingData['appActivity'] = 'global.longbridge.android.LaunchActivity'
    desired_caps = settingData
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    sleep(1)
    allId = 'global.longbridge.app.android:id/tv_summary_value'
    allNum = driver.find_element_by_id(allId).text
    availableId = 'global.longbridge.app.android:id/tv_cash_value'
    availableNum = driver.find_element_by_id(availableId).text
    param = {
        'method':0,
        'tableName':'changQiao0',
        'allNum':allNum,
        'availableNum':availableNum,
    }
    initMysql(param)
    driver.quit()
    
   