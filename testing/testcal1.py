import allure
import pytest
import yaml


# 获取数据
def get_dates():
    with open('./datas.yaml') as f:
        dates = yaml.safe_load(f)
    add_date = dates['dates']['add_dates']
    sub_date = dates['dates']['sub_dates']
    mul_date = dates['dates']['mul_dates']
    div_date = dates['dates']['div_dates']
    return [add_date, sub_date, mul_date, div_date]


@allure.feature('测试计算器')
class TestCalc:

    @allure.story('加法：测试用例')
    @allure.title('加法')
    @pytest.mark.parametrize('a, b, expect', get_dates()[0],
                             ids=['int0_case', 'int1_case', 'float0_case', 'float1_case', 'bing_case'])
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, a, b, expect):
        # 调用Calculator的类方法add()
        result = get_calc.add(a, b)
        assert result == expect

    @allure.story('减法：测试用例')
    @allure.title('减法')
    @pytest.mark.parametrize('a, b, expect',
                             get_dates()[1],
                             ids=['int0_case', 'int1_case', 'float0_case', 'float1_case', 'bing_case'])
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, a, b, expect):
        # 调用Calculator的类方法sub()
        result = get_calc.sub(a, b)
        assert round(result, 2) == expect

    @allure.story('乘法：测试用例')
    @allure.title('乘法')
    @pytest.mark.parametrize('a, b, expect', get_dates()[2])
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, a, b, expect):
        # 调用Calculator的类方法mul()
        result = get_calc.mul(a, b)
        assert round(result, 2) == expect

    @allure.step('除法：测试用例')
    @allure.title('除法')
    @pytest.mark.parametrize('a, b, expect', get_dates()[3])
    @pytest.mark.run(order=-1)
    def test_div(self, get_calc, a, b, expect):
        # 调用Calculator的类方法div()
        try:
            result = get_calc.div(a, b)
            assert result == expect
        except ZeroDivisionError:
            result = 0
            assert result == 0


if __name__ == '__main__':
    pytest.main(['testcal.py', '-v'])
