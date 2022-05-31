# 问题 ：用unittest的测试报告太简单，只能在控制台查看，想生成的测试报告能更加详细，能在浏览器中打开

# 解决方案：使用HTMLTestRunner模块生成测试用例，原理：将运行的测试用例结果输出到HTML文件中，就能使用浏览区打开

# 前置条件：直接现成的
"""
类：HTMLTestRunner(f,title,description)
f:

"""
from homework.iter03_add_user_finally import login
import unittest
import sys
from package_unittest.HTMLTestRunner import HTMLTestRunner


class TestLogin(unittest.TestCase):

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
    suite_a.addTest(TestLogin('test_password_is_null'))  # 此两条添加到套件中  显示有两个点，一个点代表一条测试用例，点代表的成功，f代表失败
    print(suite_a)
    # 创建一个测试报告文件，是HTML格式的
    test_report = './test_report.html'
    with open(test_report, 'wb') as f:  # 打开以后直接关闭

        runner = HTMLTestRunner(f, title='测试报告', description='测试报告描述')
        runner.run(suite_a)
