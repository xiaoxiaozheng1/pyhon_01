# 序列的通用操作
# 1 .索引 -列表，序列，字符串
lst = ['red', 'hello', 2, 3.5]
print(lst[1])  # 列表里的第二值  0,1,2,3
print(lst[-3])  # -4,-3，-2，-1

tp = ('red', 'hello', 2, 3.5)
print(tp[1])  # 索引都是[]
print(tp[-1])

my_str = "redhello2"  # 索引都是[]
print(my_str[1])
print(my_str[-1])

# 2.序列的切片： seq[start:end:step]，start代表开始的位置，默认是从0开始
# end代表的是结束位置，step代表的是步长，默认为1
lst5 = ['red', 'green', 'blue', 'black', 'gold', 'orange']
print(lst5[1:5:1])  # 获取第2-5个元素
print(lst5[1:6:2])  # 获取偶数的值

print(lst5[::2])  # 省略了start和end
print(lst5[0:6:2])

print(lst5[2:])  # 省略了end和step
print(lst5[2:6:1])
print(lst5[2::])

print(lst5[1::2])  # 省略的是end

print(lst5[:3:])  # 省略的是start和step

print(lst5[::])

lst1 = ('a', 'bb', 'ccc', 'dddd', 'eeeee', 'fffff')
print(lst1[2:4:1])
print(lst1[0:5:2])

str1 = "qweqrrytetgbshg12346"
print(str1[2:len(str1):1])

# 列表中有10个元素，取出其中的奇数个数的元素
print(lst[0::2])

# 3.序列的想加和相乘：+ ，*
alst = [1, 2]
blst = [3, 4]
clst = alst + blst
print(clst)
astr = 'hello'
bstr = 'python'
print(astr + bstr)

dlst = alst * 2
print(dlst)

elst = [None] * 3
print(elst)

print("======================")
print("=" * 60)

# 检查元素 ： in
lst6 = ['red', 'green', 'blue', 'black', 'gold', 'orange']
print('gold' in lst6)
print('gold1' in lst6)

# 序列中的方法：list()
# klst = []
print("=" * 20)  # =分隔符
klst = list()  # 空列表
print(klst)
cstr = "abc"  # 把字符串变成列表
mlst = list(cstr)
print(mlst)

nlst = [1, 2, 3]  # 列表转字符串有些问题
dstr = str(nlst)
print("dstr:", dstr)
print(type(dstr))
estr = str('23')
print(type(estr))

lst7 = ['red', 'green', 'blue', 'black', 'gold', 'orange']
for x in lst7:
    print(x, end=' ')
print()

# 循环序列中的索引和值
for index, vls in enumerate(lst7):
    print(index, '====', vls)
