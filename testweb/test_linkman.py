import shelve

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data():
    with open('./data.yaml') as f:
        datas = yaml.safe_load(f)
        filexlsx = datas['datas']['filexlsx']
        filertf = datas['datas']['filertf']
        fileaxlsx = datas['datas']['fileaxlsx']
        filexls = datas['datas']['filexls']
        return [filexlsx, filertf, fileaxlsx, filexls]


# 把cookies存到shelve数据库中
def test_shelve():
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850128898183'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'GTjmodJ3a7J2H4lI2wf5dySBzrd_XNYCzPL5s3ZztS926sKsK9GtjbF1-tLZ_qeffvcn0fb5l7I0uVzQFY1sNXsmIYugN9dqMV0fSthx2RLagqPPFjgws3PFdy1dUTe6eu1U_dsc4FvUEYcdPLZqhPJVUYP24P7X5KaqmjnQN0Y5Yg1Z7tiwLVgT-1H29Oyhue2s_ObOET8hwuDYzHj0SiCV5JsM0K9rdJdRE09UqxZcbGFCfwsyDUWWdzwZcSQlZzx-mDXmko-5J_aG7n8eNA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603532787'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635068787, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603455386,1603464287,1603504532,1603532787'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '9850689404'}, {'domain': '.work.weixin.qq.com', 'expiry': 2234249562, 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True, 'value': '39645983301237135'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850128898183'}, {'domain': 'work.weixin.qq.com', 'expiry': 1603536067.479345, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': '5m366v3'}, {'domain': '.qq.com', 'expiry': 1603619240, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.667671313.1603454103'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '-28XWpbCt0qfIvvBOHbZTtl2QLYJNGzv-QTHBPhkXc8UJrzSSwVzCJlgCQuB3JOH'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634990098.232068, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324963171111'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '6989190144'}, {'domain': '.work.weixin.qq.com', 'expiry': 1606124842.752319, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1909468'}, {'domain': '.qq.com', 'expiry': 2147483647.083794, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'NNQsakvnNM'}, {'domain': '.qq.com', 'expiry': 1666604840, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.610113701.1603454103'}, {'domain': '.qq.com', 'expiry': 2147483647.08383, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '1c4a344c6de9a75ddfd7d40e1da79b0ec9dcfff441bc75cb8dfa88665abacc3d'}, {'domain': '.work.weixin.qq.com', 'expiry': 2234249562, 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True, 'value': 'direct'}]
    # 打开shelve数据库
    db = shelve.open('cookies')
    # 把数据存储到db
    db['cookies'] = cookies
    # 关闭数据库
    db.close()


class TestLinkman:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('filepath,filename', get_data())
    def test_lead(self, filepath, filename):
        # 打开shelve数据库
        db = shelve.open('cookies')
        # 取出cookies
        cookies = db['cookies']
        # 关闭数据库
        db.close()
        print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 把cookie注入到页面
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 刷新当前页面
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        upload = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask')
        upload.send_keys(filepath)
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert filename == filename
