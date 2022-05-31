# append出现None的问题 ：一定要注意！append方法只是在恰当的位置修改原来的列表！！！
# 这意味着，他不是返回一个列表，而只是修改原来的列表，所以如果用 等式 输出的话，返回是None ，也就意味着不会有返回值！！
# 也就是说，去掉返回值即可得到新的列表！
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
             {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
lst = []
print(lst)
# for x in user_list:
#     x.pop('password')
#     lst1 = lst.append(x)
#     print(lst1)  # []  None None 打印结果

for x in user_list:
    x.pop('password')
    lst.append(x)
print(lst)
# 返回结果
# []
# [{'role': 'admin', 'account': 'admin', 'dept': 'tester'}, {'role': 'user', 'account': 'dev', 'dept': 'dev'}]
