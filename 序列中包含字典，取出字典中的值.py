goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}, ]
# 找出美女的价格
# print(goods[3]["price"])   # 仅仅适用一眼可以看出的这种： 998
for x in goods:  # 找出美女的价格 第一层循环，获取各个元素（各个不同的字典）
    if "美女" in x.values():  # 判断"美女"在不在其中的values
        print(goods[goods.index(x)]["price"])  # 如果在 获取美女所在的索引 x 。打印对应的price下的value的值

for x in goods:
    if x.get('name') == '美女':
        print(goods[goods.index(x)]['price'])


# 获取每个元素的Key和value
for x in goods:
    # print(x.items())c 这种形式不是我们想要的 ： dict_items([('name', '电脑'), ('price', 1999)])
    for key, value in x.items():
        print(key, value, end=' ')
    print()  # 这种是我们想要的：name 电脑 price 1999

# 反思举例：已知值获取键。先找出键值，通过值反找出键
key_list = []
value_list = []
d5 = {'zhangsan': 23, 'lisi': 35}
for key, value in d5.items():
    key_list.append(key)
    value_list.append(value)
get_value = int(input("你要查询的值是："))
if get_value in value_list:
    get_value_index = value_list.index(get_value)
    print("您查询的键是：%s" % key_list[get_value_index])
else:
    print("您查询的数%s不存在" % get_value)



