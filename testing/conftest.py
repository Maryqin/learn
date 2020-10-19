import pytest

from pythoncode.claculator import Calculator


@pytest.fixture(scope='module')
def get_calc():
    print('开始计算！')
    calc = Calculator()
    yield calc
    print('计算结束！')
