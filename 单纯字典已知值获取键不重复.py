key_list = []
value_list = []
mydisc = {'key1': '123', 'key2': '234', 'key3': '345'}
for key, value in mydisc.items():
    key_list.append(key)
    value_list.append(value)
get_value = input("请输入要查值：")
if get_value in value_list:
    get_value_index = value_list.index(get_value)
    print("你要查询的值对应的键为：%s" % key_list[get_value_index])
else:
    print("你要查询的值%s不存在" % get_value)




