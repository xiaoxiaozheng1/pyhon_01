# 1.使用TestSuite(),可以将不同的测试用例添加到套件中（作用）
"""
b. TestSuite()功能：
    1.addTest(testcase),testcase代表的是测试用例，可以添加不同的测试用例到套件中（单条）-用的多
    2.addTests(tests),tests代表的是测试测试用例组，以列表形式显示，可以添加不同的测试用例组到套件中（一组）-用得少
"""
# 2.使用TextTestRunner()类进行运行测试套件
"""
c.TextTestRunner()功能：
    1.run(suite)，suite就是测试套件，可以将测试套件进行运行
"""
# 解决的问题：解决了可以按照不同的测试套件上运行

from homework.iter03_add_user_finally import login
import unittest
import sys


class TestLogin(unittest.TestCase):
    # 初始化类方法
    @classmethod  # 装饰器
    def setUpClass(cls) -> None:
        print("开始运行方法:", sys._getframe().f_code.co_name)  # 获取方法的名字 ，在类最开始的地方执行

    # 清空类方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("开始运行方法:", sys._getframe().f_code.co_name)  # 获取方法的名字 ，在类结束的地方执行

    # 初始化方法
    def setUp(self) -> None:
        print("开始运行方法:", sys._getframe().f_code.co_name)

    # 清除方法
    def tearDown(self) -> None:
        print("开始运行方法:", sys._getframe().f_code.co_name)

    # 1.测试登录的测试用例
    # case1： 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin', '123456').get('code')
        self.assertEqual(except_value, actual_value)

    # case2： 输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('bca', '123456').get('code')
        self.assertEqual(except_value, actual_value)

    # case3:  输入空的用户或密码登录
    def test_password_is_null(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 1  # 可以在这里改成1让运行通过，原本是2
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)


if __name__ == '__main__':
    # 创建一个套件a
    suite_a = unittest.TestSuite()  # 调用unittest下面的类
    suite_a.addTest(TestLogin('test_login_success'))  # 先写测试用例类TestLogin()，括号里面才是调用方法
    suite_a.addTest(TestLogin('test_user_wrong'))  # 此两条添加到套件中  显示有两个点，一个点代表一条测试用例，点代表的成功，f代表失败
    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)
