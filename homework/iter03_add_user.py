""" 需求-迭代3：用户新增功能:
1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2. 需要对文件的读写进行异常捕获
3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
4. 同时进行查询时，也能查询出该用户 。
5.当用户添加成功时，在返回的结果中要创建时间
"""

# 方法：从文件中读取数据，返回的时列表形式的数据
from datetime import datetime


def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name, 'r')
        line = f.readline()  # 读出来的是字符串
        user_data = eval(line)  # 此方法是将字符串转化成对应的形式：如列表，元祖和字典
        return user_data
    except Exception as  e:
        print(e)
    finally:
        if not f:
            f.close()  # 这里的f可能是None,就不能调用close()方法


# 方法：能向文件中写入内容，用户添加的信息是在原来的基础上添加的。
def save_data(file_name, file_content):
    f = None
    try:
        f = open('user_data.txt', 'w')
        f.write(str(file_content))  # file_content是一个列表，而write保存的是字符串
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


# 1 定义用户默认数据:[a1,a2]

# user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
#              {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
# 注释掉后直接从文件获取
user_list = []
"""
值 if 表达式1  else 表达式2
"""
# 如果user_list有值直接返回if前面的user_list的值否则的话调用from_file_get_data('user_data.txt')
user_list = user_list if user_list else from_file_get_data('user_data.txt')

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
            result.update({"message": "登陆成功", "user_list": user_list})
            return result
    # 用户名和密码不匹配或输入错误的情况
    result.update({"code": 1, "message": "请检查您的用户名或密码是否填写正确。"})
    return result


# 创建一个类，包括新增用户，修改用户，删除用例，查询用户
class User():

    # 添加用户的方法
    def add_user(self, username, password='123456', **kwargs):  # **代表以字典的形式传
        user_dict = {}
        user_dict['account'] = username
        user_dict['password'] = password
        user_dict.update(**kwargs)
        # 将组装的数据添加到用户列表中
        user_list.append(user_dict)
        save_data('user_data.txt', user_list)
        result.update({"message": "用户添加成功", "add_time": datetime.now()})

    # 用户查询功能
    def get_user(self, username):  # 放在类当中前面一定要加self占位符
        # 判断用户是否登录，若登陆成功可以进行查询：若登陆失败，返回权限不足
        if result.get('code') != 0:
            result.update({"code": 11, "message": "用户未登录，无法查询出结果"})
            return result
        # 输入正确用户名进行查询，返回结果（支持模糊查询）
        result.update({"user_list": []})  # 这里是清空比如登录成功后user__list里面的数据清空（result里面的，并不是原始数据）
        lst = []  # 存放的是查询到的结果的数据
        for x in user_list:
            account = x.get('account')  # 等号是精确查找，in是模糊查找
            if username in account:  # 模糊查询
                x.pop('password')  # 去除 password对应的值
                lst.append(x)
        # 判断新列表里的数据，如果列表不为空，查询成功，返回对应的结果
        if lst:
            result.update({"message": "查询用户成功!", "user_list": lst})
            return result

        # 若输入的用户名不正确，返回无查询结果提示
        result.update({"code": 12, "message": "未查到用户,请重新输入!"})
        return result


if __name__ == '__main__':
    # 1.进行循环，以便用户做各种操作
    flag = True
    while flag:
        # 提供用户的各种选择，比如输入1代表登录，输入2代表查询操作，输入q:退出操作 # \n代表换行
        vls = input("操作请输入对应编号:"
                    "\n 1:)  进行登录 :"
                    "\n 2:)  进行查询用户，请输入用户名:"
                    "\n 3:)  添加用户，请输入用户信息:"
                    "\n q:)  退出操作:"
                    "\n 其他字符:)  未知操作，请重新输入:")
        # 当输入未知符号后，进行重新输入
        if not vls in ('1', '2', '3', 'q', 'quit'):
            print("=" * 30)
            continue

        # 进行登录操作
        if vls == "1":
            username = input("请输入用户名:")
            password = input("请输入密码:")
            login_result = login(username, password)
            print(login_result)
            print("=" * 30)
            continue
        # 进行查询用户的情况
        if vls == '2':
            name = input("请输入查询用户名：")
            user = User()
            get_result = user.get_user(name)  # 以前是个函数现在是个类的方法
            print(get_result)
            print("=" * 30)
            continue
        # 添加用户的情况
        if vls == '3':
            name = input("请输入添加的用户名:")
            user = User()
            get_result = user.get_user(name)
            print("get_result::::::::", get_result)
            if 12 == get_result.get('code'):  # 12代表没有查询到用户
                password = input("请输入用户密码:")
                role = input("请输入用户角色:")
                dept = input("请输入用户部门:")
                user.add_user(name, password, role=role, dept=dept)  # 以关键字形式传值=，用字典的话是：
            if 0 == get_result.get('code'):
                result.update({'code': 13, 'message': "用户已存在无法添加"})
                print(result)
            print(get_result)  # 打印查询结果
            print("=" * 30)

        # 是否退出
        if vls in ('q', 'quit'):
            flag = False
            print("退出成功!")
