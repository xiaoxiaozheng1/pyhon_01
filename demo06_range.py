# range函数
"""""
range(start,end,step)
start:开始索引，默认从0开始可以省略
end：代表结束，必选项
step：步长。默认为1，可以省略
"""""
# 需求1: 打印1-10的数
for x in range(11):  # range(0,11,1)
    print(x)

# 需求2：开始位置1，循环到10
for x in range(1, 11):  # range(1,11,1)
    print(x)

# 需求3：开始位置1，循环到10,步长为2
for x in range(1, 11, 2):
    print(x)

print(range(10))
print("=" * 30)
# break 语句断开循环
# 需求： 循环1-10，当遇到7退出循环
for x in range(1,11):
    print(x)
    if x == 7:
        break
# continue 语句进行跳过本次循环
# 需求：  循环1-10，当遇到7跳过此次循环
print("=" * 30)
for x in range(1,11):
    if x == 7:
        continue
    print(x)