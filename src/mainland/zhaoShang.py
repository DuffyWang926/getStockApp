import os
from time import sleep
import unittest
from appium import webdriver
from utils.verify import isExist, numFromStr
from src.getPwdData import getPwd
from setting import getSetting

# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_xpath('//*[@text="天猫国际"]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
# financingBtn.text
# financingBtn.get_attribute('checkable')
def operateZhaoShang(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.cmschina.stock'
    settingData['appActivity'] = '.InitActivity'
    desired_caps = settingData

    
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    logPath = 'new UiSelector().text("登录查看")'
    if isExist(driver, 1,logPath):
        driver.find_element_by_android_uiautomator(logPath).click()
        sleep(3)
        print(driver.page_source)
        print(driver.contexts)
        pwdPatha = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText'
        driver.find_element_by_xpath(pwdPatha).send_keys(1)
    # searchPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.ImageView'
    # driver.find_element_by_xpath(searchPath).click()
    # sleep(1)
    # a = driver.available_ime_engines
    # print(a)
    #  os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')
    # os.system('adb shell ime set io.appium.settings/.UnicodeIME')
    # os.system('adb shell ime set com.iflytek.inputmethod.miui/.FlyIME')
    # os.system('adb shell ime set com.baidu.input_mi/.ImeService')
    
    # pwdPatha = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[35]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View[1]'
    # driver.find_element_by_xpath(pwdPatha).click()
    # driver.press_keycode(144)
    # driver.press_keycode(29)

    
    


    # sleep(5)
    # driver.quit()