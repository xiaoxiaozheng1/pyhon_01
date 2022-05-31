# 类的多肽
"""
1.必须是继承关系
2.子类的方法覆盖了子类的方法

继承和多肽的区别：
如果说子类直接调用的是父类的方法： 继承
如果说子类直接覆盖父类的方法： 多肽

"""


class People():

    def eat(self, people_type):
        print(people_type, '在吃饭')


class Students(People):
    def eat(self, grade):
        super().eat(grade) # 可以继承父亲的方法
        print(grade, "年级学生在吃饭")


class Teacher(People):
    def eat(self, subject, time):
        print("{}的老师在{}时间吃饭".format(subject, time))


s = Students()
s.eat('2年级')
print('==============')
t = Teacher()

t.eat('语文学科', '12:00')
