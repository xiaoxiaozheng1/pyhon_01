## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,
# {'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示

# 方法一：用函数来写
def login1():
    list = [{'role': 'zhangsan', 'accont': 'user1', 'password': '123456', 'department': 'test'},
            {'role': 'lisi', 'accont': 'user2', 'password': '123456', 'department': 'develop'}]

    id = input("请输入用户名:")
    pw = input("请输入密码:")
    i = 0
    while i < len(list):

        if id == list[i]['role'] and pw == list[i]['password']:
            print({'code': '0', 'message': '登录成功', 'user_list': list[i]})
        elif id == "" or pw == "":
            print("用户名或密码为空，请重新输入：")
        else:
            print("请检查您的用户名或密码是否填写正确：")
        i += 1


login1()


#
# # 方法二：用方法来写
# class User():
#     def __init__(self, ro, ac, pw, dp):
#         self.ro = ro
#         self.ac = ac
#         self.pw = pw
#         self.dp = dp
#
#     def login(self, ro, pw):
#         if self.ro == ro and self.pw == pw:
#             print({'code': '0', 'message': '登录成功', 'user_list': [self.ro, self.ac, self.pw, self.dp]})
#         elif ro == '' or pw == '':
#             print("用户名或密码为空，请重新输入：")
#         else:
#             print("请检查您的用户名或密码是否填写正确：")
#
#
# user1 = User(ro="zhangsan", ac="user1", pw="123456", dp="test")
# user2 = User(ro="lisi", ac="user2", pw="123456", dp="develop")
# user1.login(ro=input("请输入用户名："), pw=input("请输入密码:"))
# user2.login(ro=input("请输入用户名："), pw=input("请输入密码:"))

# 方法2：用方法来写：
class User():
    def __init__(self, ro, ac, pw, dp):
        self.ro = ro
        self.ac = ac
        self.pw = pw
        self.dp = dp

    def login(self, ro, pw):
        if self.ro == ro and self.pw == pw:
            print({'code': '0', 'message': '登录成功', 'user_list': [self.ro, self.ac, self.pw, self.dp]})
        elif ro == '' or pw == '':
            print("用户名或密码为空，请重新输入：")
        else:
            print("请检查您的用户名或密码是否填写正确：")


user1 = User(ro="zhangsan", ac="user1", pw="123456", dp="test")
user2 = User(ro="lisi", ac="user1", pw="123456", dp="test")
user1.login(ro=input('请输入您的用户名：'), pw=input("请输入您的密码："))
user2.login(ro=input('请输入您的用户名：'), pw=input("请输入您的密码："))

## 需求-迭代2：用户查询功能:
# 1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
# 2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
# 3. 若输入的用户名不正确 ，给出无查询结果的提示
# 4. 查询支持模糊查询。
#
#
#
# ## 需求-迭代3：用户新增功能:
# 1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
# 2. 需要对文件的读写进行异常捕获
# 3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
# 4. 同时进行查询时，也能查询出该用户 。