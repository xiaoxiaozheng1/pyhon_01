# 实例变量
# 实例: 创建学生类，要求有属性：姓名和年级
# 方法有：学习的方法，打印学生的上课情况
class Students():  # 类名首字母规范是大写
    # name = "张三"  #  类变量，在这里可以等价看做Students.name = "张三"
    # grade = "5年级"  # 类变量 在这里可以等价看做Students.grade = "5年级"

    def study(self):  # 定义变量在内部不太好
        # self.name = '张三'  # 实例变量
        # self.grade = '5年级'  # 实例变量
        # score = 60  # 定义局部变量 ，只能在这个方法中使用访问
        print("这里的self是：", self)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # sex = '男'  # 定义局部变量
        print("这里的self是：", self)
        print("{}年级的学生{}正在学习".format(self.grade, self.name))

    def eat(self):
        print(self.name, "是", self.grade, "正在吃饭")


# 调用的时候有两种方法：
# s1 = Students()
# print(s1.study() )
# print(s1.eat())  # 这里颠倒study()放在eat()前面才不会报错，因为self.name和self.grade定义在了study()中

s1 = Students('张三', '5年级')
print(s1.eat())  # 这里直接调用eat()方法就不会报错
