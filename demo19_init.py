# 实例: 创建学生类，要求有属性：姓名和年级
# 方法有：学习的方法，打印学生的上课情况
class Students():  # 类名首字母规范是大写
    name = ""
    grade = ""

    # 申明构造方法： __init__()
    def __init__(self):
        print("此方法执行了")

    def study(self):
        print("这里的self是：", self)
        print("{}年级的学生{}正在学习".format(self.grade, self.name))


s1 = Students()
print(s1)
s1.name = "张三"
s1.grade = '5'
print(s1.study())  # 即使这里注释掉构造方法也会执行


# 以上的需求使用构造方法去实现
class Students1():  # 类名首字母规范是大写

    # 申明构造方法： __init__()
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print("此方法执行了")

    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade, self.name))


s2 = Students1('王五',6)
s2.study()

# 需求 ： 实现连接数据库
"""
1.定义连续数据库的类
2.必须和数据库建立连接，使用构造方法是最合适的
3.进行各种方法的调用
"""
