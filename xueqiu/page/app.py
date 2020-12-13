import time

from appium import webdriver

from xueqiu.page.base_page import BasePage
from xueqiu.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            # desire_caps = {}
            # desire_caps['platformName'] = 'android'
            # desire_caps['platformVersion'] = '6.0'
            # desire_caps['deviceName'] = '127.0.0.1:5555'
            # desire_caps['appPackage'] = 'com.xueqiu.android'
            # desire_caps['appActivity'] = '.view.WelcomeActivityAlias'
            # desire_caps['noReset'] = 'true'
            # desire_caps['unicodeheyBoard'] = 'true'
            # desire_caps['reseKeyBoard'] = 'true'
            # desire_caps['chromedriverExecutable'] = r'D:\Downloads\chromedriver\74.0.3729\chromedriver.exe'
            desire_caps = self.parse_yaml(r'D:\MyProject\xueqiu\data\capa.yaml', None)
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        time.sleep(5)
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
