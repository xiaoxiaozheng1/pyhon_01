# 变量
# 实例: 创建学生类，要求有属性：姓名和年级
# 方法有：学习的方法，打印学生的上课情况
class Students():  # 类名首字母规范是大写
    name = "张三"  # 在这里可以等价看做Students.name = "张三"
    grade = "5年级"  # 在这里可以等价看做Students.grade = "5年级"

    def study(self):
        print("这里的self是：", self)
        print("{}年级的学生{}正在学习".format(self.grade, self.name))


# 调用的时候有两种方法：

# 1.使用类名去调用
print(Students.name)
print(Students.grade)

# 2.使用实例化对象去调用
print('=' * 20)

s1 = Students()
print(s1.name)
print(s1.grade)

