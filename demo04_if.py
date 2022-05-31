# 条件语句
"""""
格式：
    if 条件语句：
        执行代码块
"""""

a = 5
if a > 5:
    print("a是大于5的数")
else:
    print("a是小于5的数")

"""""
多条件判断格式:
if 条件语句1：
    执行代码块1
elif 条件语句2：
    执行代码块2
elif 条件语句3：
    执行代码块3
else:
    执行代码块4
"""""
score = 75
if score > 90:
    print("A")
elif score > 80:
    print('B')
elif score > 60:
    print('C')
else:
    print('D')

if 70 < score < 90:
    print('良')

if 0:
    print("hello world")

if "abcd":
    print("hello world")
if "":
    print("hello world")

a_str = "hello"
b_str = "helloworld"
print(a_str in b_str)
