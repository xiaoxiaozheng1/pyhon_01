class Students:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, course): print("学生对象{},目前{}年级,正在学习{}".format(self, self.grade, course))


a = Students('张三', '5')
a.study("英语")
b = Students('李四', 5)
b.study("数学")
print(a)
print(b)



