from appium import webdriver

# WebDriverWait 等待一个控件是否出现，比如跳过
from selenium.webdriver.support.ui import WebDriverWait
import time

cap = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)


# 获取窗口的大小
def get_size():
    # 获取宽度
    x = driver.get_window_size()['width']
    # 获取高度
    y = driver.get_window_size()['height']
    return(x, y)


# 点击同意
# 先看看是否有没有这个控件，如果有则点击
try:
    if WebDriverWait(driver, 3).until((lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']"))):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']").click()
except:
    pass


# 点击跳过
# 先看看是否有没有这个控件，如果有则点击
try:
    if WebDriverWait(driver, 3).until((lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']"))):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except:
    pass


# 点击密码登录
try:
    if WebDriverWait(driver, 3).until((lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_code_touname']"))):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_code_touname']").click()
except:
    pass

# 输入用户名和密码
try:
    if WebDriverWait(driver, 3).until((lambda x: x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']"))):
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys("13232732408")
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys("130796abc")
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except:
    pass

# 看看有没有让你确认专业与院校，有就点，没有就跳过
try:
    if WebDriverWait(driver, 40).until((lambda x: x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/kaoyan_home_schtip_close']"))):
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/kaoyan_home_schtip_close']").click()
except:
    pass


# 点击研讯
if WebDriverWait(driver, 5).until((lambda x: x.find_element_by_xpath("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"))):
    driver.find_element_by_xpath("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()

    # 滑动操作
    # 想要划动手机屏幕，得要获取到屏幕的大小，所以定义一个get_size()方法
    l = get_size()

    # 在屏幕中间划动，取一半
    x1 = int(l[0]*0.5)
    # 从哪开始划动，从下面开始划动,  一般是取0.75
    y1 = int(l[1]*0.75)
    # 到哪停止
    y2 = int(l[1]*0.25)

    # 用这个方法swipe()划动, 什么时候开始x1, y1，什么时候结束x1, y2
    while True:
        driver.swipe(x1, y1, x1, y2)
        time.sleep(0.5)


