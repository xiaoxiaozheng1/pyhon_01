import json


# json.dumps把python对象转换成json对象的一个过程，生成的是字符串
# import json
# data= json.dumps({"a":1,"c":2})
# print(data)#{"a":1,"c":2}
# print(type(data))#<class 'str'>

class all():
    def __init__(self):
        self.code = 1
        # self.lis = [{"role": "admin", "account": "admin", "password": "123456", "dept": "tester"},
        # {"role": "user", "account": "dev", "password": "123456", "dept": "tester"}]
        try:
            f = open("a.txt", "r")
            usli = []
            while True:
                line = f.readline().replace("\n", "")
                if not line:
                    break
                else:
                    usli.append(json.loads(line))
                    # print(usli, end="")
            self.lis = usli
        except Exception as e:
            print(e)

    def load(self):
        while self.code == 1:
            a = input("请输入用户名：")
            b = input("请输入密码：")
            if a == "" or b == "":
                print("用户名或密码为空，请重新输入：")
            i = 0
            while i < len(self.lis):
                if self.lis[i]["account"] == a and self.lis[i]["password"] == b:
                    self.code = 0
                    key_list = list(self.lis[i])  # 键名表
                    print({'code': '0', 'message': '登录成功',
                           'user_list': [key_list[0] + ":" + self.lis[i]['role'],
                                         key_list[1] + ":" + self.lis[i]['account'],
                                         key_list[2] + ":" + self.lis[i]['password'],
                                         key_list[3] + ":" + self.lis[i]['dept']]})
                    break
                else:
                    i += 1
            if self.code != 0:
                print("请检查您的用户名或密码是否正确，按Enter键重新输入，其他任意退出")
                rep = input()
                if not rep == "":
                    break
            else:
                break

    def search(self):
        i = 0
        li = []  # 保存查询到的其他用户信息
        usr = input("请输入您要查询的用户账号：")
        while i < len(self.lis):
            if usr in self.lis[i]["account"]:  # 第i个用户名包含输入的用户名
                key_list = list(self.lis[i])  # 键名表
                li.append({'user_list': [key_list[0] + ":" + self.lis[i]['role'],
                                         key_list[1] + ":" + self.lis[i]['account'],
                                         key_list[3] + ":" + self.lis[i]['dept']]})
            i += 1  # 不管当前查询到没有，看看还有没有符合模糊查询的用户
        if len(li) != 0:  # 查询到的用户数量不为空
            print(li)
        else:
            print("输入的用户名不正确，未查询到用户。")

    def add(self):
        role1 = input("请输入需要新增的用户权限名称（user,admin）：")
        acount1 = input("请输入需要新增的用户账号：")
        passwd1 = input("请输入需要新增的用户密码：")
        dept1 = input("请输入新增的用户类型(eg:tester)：")
        usrdic = {"role": role1, "account": acount1, "password": passwd1, "dept": dept1}
        usrstr = json.dumps(usrdic)
        try:
            f = open("a.txt", "a")
            f.write("\n" + usrstr)
        except Exception as e:
            print(e)

    def func(self):
        if self.code != 0:
            print("权限不足，请先登录：")
            self.load()
        n = input("请选择功能，输入add新增用户，输入sea查询用户：")
        if n == "add":
            self.add()
        elif n == "sea":
            self.search()


s = all()
s.func()
