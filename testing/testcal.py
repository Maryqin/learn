import pytest
import yaml

from pythoncode.claculator import Calculator


class TestCalc:

    def setup_class(self):
        print('开始计算！')
        # 实例化Calculator
        self.calc = Calculator()

    def teardowm_class(self):
        print('计算结束！')

    @pytest.mark.parametrize('a, b, expect',
                             [[1, 2, 3], [1, -1, 0], [1, 0.2, 1.2], [0.2, 0.2, 0.4], [10000, 10000, 20000]],
                             ids=['int0_case', 'int1_case', 'float0_case', 'float1_case', 'bing_case'])
    def test_add(self, a, b, expect):
        # 调用Calculator的类方法add()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect',
                             [[1, 2, -1], [1, -1, 2], [1, 0.2, 0.8], [0.4, 0.2, 0.2], [20000, 10000, 10000]],
                             ids=['int0_case', 'int1_case', 'float0_case', 'float1_case', 'bing_case'])
    def test_sub(self, a, b, expect):
        # 调用Calculator的类方法sub()
        result = self.calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open('mul.yaml')))
    def test_mul(self, a, b, expect):
        # 调用Calculator的类方法mul()
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open('div.yaml')))
    def test_div(self, a, b, expect):
        # 调用Calculator的类方法div()
        try:
            result = self.calc.div(a, b)
            assert result == expect
        except ZeroDivisionError:
            result = 0
            assert result == 0


if __name__ == '__main__':
    pytest.main(['testcal.py', '-v'])
