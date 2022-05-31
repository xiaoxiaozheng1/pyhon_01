from loguru import logger

from homework.iter03_add_user_finally import login

# 1.测试登录的测试用例
# case1：输入正确的用户名和正确的密码进行登录
# case2: 输入错误的用户名或密码登录
# case3: 输入空的用户或密码登录

# 2. 进行测试  - 使用断言 ： assert 值1 操作符 值2
# 测试方法 ： 预期效果 和 实际效果 进行比较

# 以上用例 登陆成功的预期结果是 code =0 ，
login_result = login('admin', '123456')
logger.debug("登录返回数据；{}".format(login_result))

assert 0 == login_result.get('code')  # 断言通过就不会有输出
assert 1 == login_result.get('code')  # 这条断言不通过有输出 AssertionError

# 存在的问题：
"""
1.无法查看运行的用例数，比如成功了几条，失败了几条
2.如果失败了，是因为什么导致？最好给出失败的错误日志
3.无法组织用例,不能控制哪些用例执行，哪些不执行
"""
