# 实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Students():
    name = ""
    grade = ""

    def study(self):
        print("这里的self是:", self)
        print("{}年级的学生{}正在学习".format(self.grade, self.name))


s1 = Students()
print(s1)
s1.name = '张三'
s1.grade = '5'
print(s1.study())

s2 = Students()
print(s2)
s2.name = '李四'
s2.grade = '4'
print(s2.study())
