# 列表

# 格式 ： 变量名 = []

alst = []  # 定义空列表
blst = [11, 23, 'hds', 'None']

print(alst)
print(blst)

# 循环列表 ：
for x in blst:
    print("列表中的值", x)

# 列表的方法 ：
clst = ['red', 'green', 'blue']

# 向列表中添加元素 ： list.append[obj]，列表的元素
clst.append("black")
print("使用append添加元素后的列表：", clst)

# 向列表中追加一个其他列表内的元素：list.extend(seq)
clst.extend(blst)
print("追加blst后的结果：", clst)

# 列表反转 ： list.reverse()
clst.reverse()
print("翻转后的结果：", clst)

# 列表排序 ： list.sort() ，里面的元素必须是同类型的
# clst.sort()
# print("排序后的结果：", clst)

# 统计在列表中出现的次数：list.count(obj)
print("次数为：",clst.count("blue"))

# 从列表中找出某个元素的位置：list.index(obj)
print(clst.index('black'))

# 向列表中的某个位置插入元素：List.insert(index,obj)
clst.insert(1, 'hello')
print(clst)

# 移除列表中的一个元素: list.pop(index)
clst.pop(1)
print(clst)

# 移除某个元素匹配的值： List.remove(obj)
clst.remove("None")
print(clst)

# 复制列表 list.copy()
clst1 = clst.copy()
print(clst1)

# 请空列表  list.clear()
clst1.clear()
print(clst1)

# 打印1-10之间的数
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(x)

# 打印1-10之间的偶数
for x in [2, 4, 6, 8, 10]:
    print(x)
