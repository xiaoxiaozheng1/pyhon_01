def load():
    lis = [{"role": "admin", "account": "admin", "password": "123456", "dept": "tester"},
           {"role": "user", "account": "dev", "password": "123456", "dept": "tester"}]
    code = 1
    while code == 1:
        a = input("请输入用户名：")
        b = input("请输入密码：")
        if a == "" or b == "":
            print("用户名或密码为空，请重新输入：")
        i = 0
        while i < len(lis):
            if lis[i]["account"] == a and lis[i]["password"] == b:
                code = 0
                print({'code': '0', 'message': '登录成功',
                       'user_list': [lis[i]['role'], lis[i]['account'], lis[i]['password'], lis[i]['dept']]})
                break
            else:
                i += 1
        if code != 0:
            print("请检查您的用户名或密码是否正确，按Enter键重新输入，其他任意退出")
            rep = input()
            if not rep == "":
                break


load()
