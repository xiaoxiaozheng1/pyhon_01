# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = 10
b = 12
c = 14
d = 16
print("计算a + b - c * d的结果：", a + b - c * d)
# 2. 打印1~100内被3整除的所有数的和 。
a = 1
sum = 0
while a <= 100:
    a += 1
    if a % 3 == 0:
        sum += a
print("1-100被3整除所有数的和：", sum)
print("------------------------------")
sum = 0
for x in range(1, 101, 1):
    if x % 3 == 0:
        sum += x
print("1-100被3整除所有数的和：", sum)
# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1, 10, 2):
    print(x)
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for x in range(0, 100, 2):
    sum1 += x
for y in range(1, 100, 2):
    sum2 += y

# for x in range(1, 101):
#     if x % 2 == 0:
#         sum += x
#     else:
#          sum2 += x
# print(sum1 - sum2)

# for y in range(0, 100, 2):
# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1, 101):
    sum += x
print(sum)
# 6. 判断一个数n能同时被3和5整除
m = int(input("请输入一个数："))
if m % 3 == 0 and m % 5 == 0:
    print("这个数能被3和5整除")
else:
    print("这个数不能被3和5整除")
# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
a = 10
if a in range(1, 101):
    print(a)
# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x = int(input("请输入第一个数:"))
y = int(input("请输入第二个数:"))
z = int(input("请输入第三个数:"))
list = [x, y, z]
list.sort()
for n in list:
    print(n)
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。备注：需要使用input()方法
score = int(input("请输入你的成绩："))
if score >= 90:
    print("你的成绩为：A")
elif 60 < score < 89:
    print("你的成绩为:B")
else:
    print("你的成绩为：C")
# alt + shift + E 运行选中命令
# 10. 将一个列表的数据复制到另一个列表中。
list = [1, 2, 3]
list1 = list.copy()
print(list1)

# 11. 输出 9*9 乘法口诀表。
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%dx%d=%-2d" % (j, i, i * j), end="\t")
print()
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str = input("请输入一行字符串：")
a, b, c, d = 0, 0, 0, 0
for ch in str:
    if ch == ' ':
        a += 1
    elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        b += 1
    elif '0' <= ch <= '9':
        c += 1
    else:
        d += 1
print("空格有%d个，字母有%d个，数字有%d个，其它字符有%d个。" % (a, b, c, d))
# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。
# 22 = 2*10^1+2
# 222 = 2*10^2+2
# 2222 = 2*10^3+2
a = int(input("请输入一个数："))
b = int(input("请输入要加的次数："))
i = 0
sum = 0
while i < b:
    c = a * (10 ** b) + a
    sum += c
    i += 1
print(sum)
# 14. 题目：打印出如下图案（菱形）:
#         *
#        ***
#       *****
#      *******
#       *****
#        ***
#         *
# center(width,fillchar)
# 返回一个长度为width,两边用fillchar(单字符)填充的字符串，
# 即字符串str居中，两边用fillchar填充。
# 若字符串的长度大于width,则直接返回字符串str
for i in range(1, 8, 2):
    n = '*' * i
    print(n.center(10))
for i in range(5, 0, -2):
    n = '*' * i
    print(n.center(10))
