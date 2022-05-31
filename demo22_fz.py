# 封装：不希望某部分数据功能被外界去使用或访问，可以使用_或__把变量或方法给设置私有

class Students():
    name = "张三"
    __score = "76"

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


print(Students.name)
# print(Students.__score) 无法显示
s = Students()
# s.__score  不会显示
s.set_score(99)
s.get_score()
print(s.get_score())
# print(Students.__score) 无法访问
