from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, element):
        return self.driver.find_element(by, element)

    def find_click(self, by, element):
        self.driver.find_element(by, element).click()

    def find_send_keys(self, by, element, text):
        self.driver.find_element(by, element).send_keys(text)

    # 滚动查找
    def find_scroll(self, text):
        return self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                                        'instance(0));').click()

    def find_toast_text(self):
        return self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text

    # 显示等待查到元素
    def wait(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*locator))

    # 显示等待查找不到元素
    def wait_not(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until_not(lambda x: x.find_element(*locator))

    def wait_source(self, timeout, text):
        WebDriverWait(self.driver, timeout).until(lambda x: f"{text}" in x.page_source)
