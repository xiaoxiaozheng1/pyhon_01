# 字典

# 1.字典的定义 ： 变量名 ={key1:value,key2:value}

dct1 = {}
dct2 = {'a': 1, 'b': 2, 'c': 3}
dct3 = {1: 'a', 2: 'b', 3: 'c'}
# print(dct1)
# print(dct2)
# 已知值查找键
key_list = []
value_list = []
for key, value in dct3.items():
    key_list.append(key)
    value_list.append(value)
print(value_list)
get_value = input("请输入你要查的值：")
if get_value in value_list:
    get_value_index = value_list.index(get_value)
    print("你要查的键值为：%s" % key_list[get_value_index])
else:
    print("你要查询的键值%s不存在" % get_value)

# 遍历字典中的值
for key, value in dct2.items():
    print(key, value)

print(dct2['a'])
# 2.字典的获取 ：dict['键名']
print("获取字典dct2中键名为b的值：", dct2['b'])
print("获取字典dct3中键名为2的值：", dct3[2])
# print("获取字典dct2中键名为d的值：", dct2['d']) 键名不存在会报错

# 字典的获取：dict.get(键名)
print("获取字典dct2中键名为b的值：", dct2.get('b'))
print("获取字典dct2中键名为d的值：", dct2.get('d'))

# 3.更新字典的某个值:dict[‘键名’] = 新值
dct2['b'] = 31
dct3[1] = 32
print(dct2)
print(dct3)

# 4.更新字典里的值到另一个字典：dict.update(dict1) #把字典4更新到2
dct4 = {'e': 22, 'f': 'hello'}
dct2.update(dct4)
print("更新后的字典显示：", dct2)

# 5.判断字典中是否存在某个键名：'键名'in dict
print('e' in dct2)
print('g' in dct2)

# 6.获取字典中所有的键名：dict.keys()
print("获取字典中所有的键名：", dct2.keys())
for x in dct2.keys():
    print(x)

# 7.获取字典中所有的值：dict.values()
print("获取字典中所有的值：", dct2.values())
for x in dct2.values():
    print(x)

# 8.获取字典中所有的键值对：dict.items()
print("获取字典中所有的键值对:", dct2.items())
for x in dct2.items():
    print(x)
