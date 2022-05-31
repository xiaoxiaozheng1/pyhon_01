# 类的继承
"""
1.必须具有父子关系，有父类和子类
2.在子类当中可以直接调用父类中的方法（功能）和属性(数据)
"""


class People():
    age = 0

    __age1 = 0

    def eat(self, people_type):
        print(people_type, '在吃饭')


class Students(People):
    pass  # 空实现，声明了方法和类以后，里面什么东西都没有


class Teacher(People):
    pass


s = Students()
s.eat('学生')

Students.age = '20'  # 可以用s.age ='20'，重新赋值，如果上面父类改为__age，则访问不了父类这个值
print(Students.age)

t = Teacher()
Teacher.age = '40'
print(Teacher.age)
t.eat('老师')
