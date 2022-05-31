# 问题 ：测试用例过多导致代码冗余 ，维护性不高 ，主要原因： 就是代码重复，数据不同

# 解决方案 ： 使用parameterized 实现数据参数化， 将列表中的数据在一条测试用例中循环运行，起到多条数据测试的作用 。

# 具体方法 ： expand(list) ,list : 数据列表
# 备注 ：使用了expand()，需要把它放在测试方法前，加@ ，这个叫装饰器(下去了解)

# 前置条件 ： 下载安装：pip install parameterized

# 1. 导入包
from parameterized import parameterized
import unittest

# 测试数据
from homework.iter03_add_user_finally import login

lst_data = [(0, 'admin', '123456'), (0, 'dev', '123456'), (1, 'dev', '1234567'),
            (1, 'aaa', '123456'), (1, '', '123456'), (1, 'dev', '')]  # 第三条是错误数据返回code=1


class TestLogin(unittest.TestCase):


    @parameterized.expand(lst_data)
    def test_login(self, except_value, username, password):
        actual_value = login(username, password).get('code')
        self.assertEqual(except_value, actual_value)


if __name__ == '__main__':
    unittest.main()  # 有三条测试数据
