from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import time

executable_path = "/Users/XieWantong/Code/Driver/geckodriver"
url = "file:///Users/XieWantong/Code/WebStormCode/js-visualdegree/index.html"


def create_firefox_session():
    # create a new Firefox session
    driver = webdriver.Firefox(executable_path=executable_path)
    driver.implicitly_wait(60)
    driver.maximize_window()
    # navigate to the application home page
    driver.get(url)
    return driver


_driver = create_firefox_session()
action = ActionChains(_driver)
next_button = _driver.find_element(By.ID, 'next')
num = 0 # 点击次数

try:
    # 您的 Selenium 代码在这里
    while True:  # 找到“下一步”按钮元素并点击
        action.move_to_element(next_button).click().perform()
        # time.sleep(1)
        confirm = _driver.switch_to.alert
        confirm.accept()

        # num += 1
        # if num % 100 ==0:
        #   time.sleep(15) 
        #   confirm = _driver.switch_to.alert
        #   confirm.accept()

except UnexpectedAlertPresentException:
    alert = _driver.switch_to.alert
    alert.dismiss()
