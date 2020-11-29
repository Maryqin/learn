import yaml

from app_wx.page.base_page import BasePage
from app_wx.page.main_page import WwMainpage
from appium import webdriver


with open('../datas/capa.yaml') as f:
    config = yaml.safe_load(f)
    desire_caps = config['desire_caps']
    ip = config['sever']['ip']
    port = config['sever']['port']


class App(BasePage):
    def start(self):
        if self.driver == None:
            # desire_caps = {}
            # desire_caps['platformName'] = 'android'
            # desire_caps['platformVersion'] = '6.0'
            # # genymotion模拟器
            # desire_caps['deviceName'] = '127.0.0.1:5555'
            # desire_caps['appPackage'] = 'com.tencent.wework'
            # desire_caps['appActivity'] = '.launch.LaunchSplashActivity'
            # desire_caps['noReset'] = 'true'
            # # 设置idle的时间
            # # desire_caps['settings[waitForIdleTimeout]'] = 0
            # desire_caps['unicodeheyBoard'] = 'true'
            # desire_caps['reseKeyBoard'] = 'true'
            # 指定chromedriver的地址
            desire_caps['chromedriverExecutable'] = r'D:\Downloads\chromedriver\74.0.3729\chromedriver.exe'
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', desire_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return WwMainpage(self.driver)
