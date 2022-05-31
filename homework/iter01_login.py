## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,
# {'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示

# 1 定义用户默认数据:[a1,a2]

user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
             {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
# for user_info in user_list:
#     print(user_info)  循环出来时是字典
# 2.定义默认返回结果
result = {"code": 0, "message": ""}


# 3.定义登录功能
def login(username, password):
    # 用户名或密码为空的情况
    if username is None or username == "":
        result.update({"code": 1, "message": "用户名不能为空"})
        return result
    if password is None or username == "":
        result.update({"code": 1, "message": "密码不能为空"})
        return result

    # 登录成功的情况
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({"message": "登陆成功", "user_list": user_list})  # 返回所有用户信息
            return result
    # 用户名和密码不匹配或输入错误的情况
    result.update({"code": 1, "message": "请检查您的用户名或密码是否填写正确。"})
    return result


# 用户查询功能
def get_user(username):
    # 判断用户是否登录，若登陆成功可以进行查询；若登陆失败，返回权限不足
    if not result.get('code'):
        result.update({"code": 11, "message": "用户未登录"})
        return result
    # 输入


if __name__ == '__main__':
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # print(login(None, "123456")) 测试
    print(login(username, password))
