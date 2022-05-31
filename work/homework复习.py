## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,
# {'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示

# 方法一：用函数来写
def login1():
    list = [{'role': 'zhangsan', 'account': 'user1', 'password': '123456', 'department': 'test'},
            {'role': 'lisi', 'account': 'user2', 'password': '123456', 'department': 'develop'}]

    i = 0
    while (i < len(list)):
        id = input("请输入您的用户名:")
        pw = input("请输入您的密码:")
        if id == list[i]['role'] and pw == list[i]['password']:
            print({'code': '0', 'message': '登录成功',
                   'user_list': [list[i]['role'], list[i]['account'], list[i]['password'], list[i]['department']]})
        elif id == "" or pw == "":
            print("用户名或密码为空")
        else:
            print("请检查您的用户名或密码是否正确")
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

# def login():
#
#     user_list=[{'role':'admin','account':'admin','password':'admin','dept':'teacher'},
#                 {'role':'user','account':'user','password':'123456','dept':'student'}]
#     user_name=input('请输入您的用户名：')
#     user_password=input('请输入您的密码：')
#
#     if user_name == '' or user_password == '':
#         dict = {'code': 1, 'message': '用户名或密码不能为空,请重新输入'}
#         print(dict)
#         login()
#
#     else:
#
#         for i in range(0,1):
#
#             if user_name == user_list[i]['account'] and user_password == user_list[i]['password'] :
#                 dict1 = {'code': 0, 'message': '登录成功', 'list': user_list[i]}
#                 print(dict1)
#                 break
#
#             elif user_name == user_list[i+1]['account'] and user_password == user_list[i+1]['password']:
#                 dict2 = {'code': 0, 'message': '登录成功', 'list': user_list[i+1]}
#                 print(dict2)
#                 break
#
#             else:
#                 dict3 = {'code': 1, 'message': '登录失败，请确认您的用户名和密码是否正确,请重新输入'}
#                 print(dict3)
#                 login()
#
#
# login()
