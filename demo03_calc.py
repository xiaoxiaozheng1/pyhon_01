# 赋值运算符

# a+=b,a-=b,a%=b
a = 3
b = 5
a += b
print(a)

a %= b
print(a)

# 逻辑运算符
# 1. a and b ==> 两个条件均满足为真，其余为假
print(a > 3 and b < 10)
print(a > 2 and b < 10)

# 2. a and b ==> 两个条件满足一个即为真
print(a > 3 and b < 10)
print(a > 2 and b < 10)

# 3. not a ==> 条件为真，加上not变假，反之为真
print(not a > 2)
print(not a < 2)

print("=================")

c = 12000
d = 12000
print(c == d)
print(c is d)
