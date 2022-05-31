# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = int(input("请输入一个整数:"))
b = int(input("请输入一个整数:"))
c = int(input("请输入一个整数:"))
d = int(input("请输入一个整数:"))
print(a + b - c * d)
# ------------------------
a = input("请输入一个整数:")
b = input("请输入一个整数:")
c = input("请输入一个整数:")
d = input("请输入一个整数:")
print(int(a) + int(b) - int(c) * int(d))
# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(3, 101, 3):
    sum += x
print(sum)
# ------------------------
sum = 0
for x in range(1, 101):
    if x % 3 == 0:
        sum += x
print(sum)
# ------------------------
x = 1
sum = 0
while x <= 100:
    if x % 3 == 0:
        sum += x
    x += 1
print(sum)
# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1, 11, 2):
    print(x)
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1 - sum2)
# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1, 101):
    sum += x
print(sum)
# 6. 判断一个数n能同时被3和5整除
# n = int(input("请输入一个整数："))
n = input("请输入一个整数：")
n = int(n)
if n % 3 == 0 and n % 5 == 0:
    print("这个数能被3和5整除")
else:
    print("这个数不能被3和5整除")
# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
n = int(input("请输入一个整数："))
if 1 <= n <= 100:
    print("在1-100")
else:
    print("不1-100")
# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
list = []
x = int(input("请输入一个整数："))
y = int(input("请输入一个整数："))
z = int(input("请输入一个整数："))
list.append(x)
list.append(y)
list.append(z)
list.sort()
for x in list:
    print(x)
# --------------------------
x = int(input("请输入一个整数："))
y = int(input("请输入一个整数："))
z = int(input("请输入一个整数："))
list = [x, y, z]
list.sort()
for n in list:
    print(n)
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。备注：需要使用input()方法
score = int(input("请输入你的成绩"))
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
# 10. 将一个列表的数据复制到另一个列表中。
alst = [1, 255, 4664, 132]
blst = ["12", "3ca", "asd"]
alst.extend(blst)
print(alst)
# 11. 输出 9*9 乘法口诀表。
for x in range(1, 10):
    for y in range(1, x + 1):
        print(y, ' x ', x, '=', x * y, end=' ')
    print()
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str = input("请输入字符串")
alpha = 0
digit = 0
space = 0
other = 0
for x in str:
    if x.isalpha():
        alpha += 1
    elif x.isdigit():
        digit += 1
    elif x.isspace():
        space += 1
    else:
        other += 1
print("字母为：", alpha)
print("数字为：", digit)
print("空格为：", space)
print("其他为：", other)
# print("字母为{},空格为{}，数字为{}，其他{})".format(alpha, digit, space, other))
# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。
# 14. 题目：打印出如下图案（菱形）:
#         *
#        ***
#       *****
#      *******
#       *****
#        ***
#         *
"""
上面的循环：
n=1 3+1+3  空格+*+空格
n=2 2+3+2
n=3 1+5+1
n=4 0+7+0
space = " " * （x-n） 
star = "*" * (2n-1)
下面的循环：
n=1 1 + 5 
n=2 2 + 3  
n=3 3 + 1
space = n * " "
star = (5- (n-1)*2) * "*"
"""
num = 5  # 总数
x = num - 1  # 循环轮次
for n in range(1, num):
    space = " " * (x - n)
    star = "*" * (2 * (n - 1) + 1)
    print(space + star)
    # print(space + star +space)

# for n in range(1, 5):
#     space = " " * (4 - n)
#     star = "*" * (2 * n - 1)
#     print(space + star)  同样适用
for n in range(1, 4):
    space = n * " "
    star = (5 - (n - 1) * 2) * "*"
    print(space + star)
#
# for n in range(1, 4):
#     space = " " * n
#     star = "*" * (7 - 2 * n)
#     print(space + star)  同样适用
