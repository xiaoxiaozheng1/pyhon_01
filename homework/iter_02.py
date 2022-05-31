"""
需求-迭代2：用户查询功能:
1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
3. 若输入的用户名不正确 ，给出无查询结果的提示
4. 查询支持模糊查询。
"""

# 1.定义用户数据:[a1,a2]
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
             {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
# 2.定义返回数据
result = {'code': 0, 'message': ""}


# 3.定义登录函数
def login(username, password):  # 少写多次if，else循环，存在未预料的结果，时间也比较长。故参考这种
    # 用户名和密码为空的情况
    if username is None or username == "":
        result.update({"code": 1, "message": "用户名不能为空"})
        return result
    if password is None or password == "":
        result.update({"code": 1, "message": "密码不能为空"})
        return result

    # 登录成功的的情况
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({"message": "登录成功", "user_list": user_list})
            return result

    # 用户名和密码不匹配的情况
    result.update({"code": 1, "message": "请检查您的用户名或密码是否填写正确"})
    return result


# 用户查询功能
def get_user(username):
    if __name__ == "__main__":
        username = input("请输入用户名:")
        password = input("请输入密码:")
        # print(login("", 123456))  # 先测试一下
    print(login(username, password))
