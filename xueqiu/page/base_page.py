import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from xueqiu.page.hand_black import handle_black


class BasePage:
    black_list = [(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, by, locator):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    # 滚动查找
    def find_scroll(self, text):
        return self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                                        'instance(0));').click()

    def parse_yaml(self, path, func_name):
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if func_name is None:
                desire_caps = data['desire_caps']
                return desire_caps
            else:
                self.parse(data[func_name])

    def parse(self, steps):
        for step in steps:
            if step['action'] == 'click':
                self.find(step['by'], step['locator']).click()

            elif step['action'] == 'send_keys':
                self.find(step['by'], step['locator']).send_keys(step['text'])

    def wait(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*locator))
