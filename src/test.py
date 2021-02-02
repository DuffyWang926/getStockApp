import os
from time import sleep
import unittest
from appium import webdriver
from utils.verify import isExist, numFromStr
from utils.openCv import getNumberLocation
from src.getPwdData import getPwd


# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_xpath('//*[@text="天猫国际"]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
# financingBtn.text
# financingBtn.get_attribute('checkable')
# driver.press_keycode(51)
# driver.press_keycode(29,64,59)
def tryTest(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    # isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    desired_caps = {
        'platformName':'Android',
        'platformVersion':'10',
        'deviceName':'2214c691',
        'appPackage':'cn.futu.trader',
        'noReset':True,
        'appActivity':'.launch.activity.LaunchActivity'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    searchPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.ImageView'
    driver.find_element_by_xpath(searchPath).click()
    sleep(1)
    a = driver.available_ime_engines
    # im = 'all.jpg'
    # im = 'next.png'
    # im = 'all.png'
    # pwd = '123'
    # test = getNumberLocation(im, pwd)
    # print('test')
    # print(test)
    #  os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')
    # os.system('adb shell ime set io.appium.settings/.UnicodeIME')
    # os.system('adb shell ime set com.iflytek.inputmethod.miui/.FlyIME')
    # os.system('adb shell ime set com.baidu.input_mi/.ImeService')
    
    # pwdPatha = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[35]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View[1]'
    # driver.find_element_by_xpath(pwdPatha).click()
    
    driver.press_keycode(51,64,59)
    
    driver.press_keycode(33)
    driver.press_keycode(34)
    driver.press_keycode(8)
    driver.press_keycode(16)
    driver.press_keycode(16)
    driver.press_keycode(8)
    driver.press_keycode(16)

    
    


    # sleep(5)
    # driver.quit()