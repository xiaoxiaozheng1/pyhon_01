# 字符串方法演示
# 1.连接字符串：join(seq)
astr = "+"
bstr = astr.join("world")
print(bstr)

# 2.分割字符串 ： split(str="")，其中str代表分隔符
cstr = "helloworldpythonjavaphp"
dstr = cstr.split("o")
print(dstr)

# 3.查找字符串 ：find(substr)，如果找到了返回的是最小索引，没有找到返回-1
estr = "helloword"
print(estr.find("l"))
print(estr.find("x"))
print(estr.index("l"))
# print(estr.index(p)) 不存在会报错

# 4.查找以xxx结尾的字符串 ：endswith('xxx')
fstr = "测试报告.doc"
if fstr.endswith('.doc'):
    print("它是一个word文档")

# 5.替换字符串 : replace(old_value,new_value)
gstr = "hello world"
hstr = gstr.replace("hello", "python")
print(hstr)
print(len(hstr))  # 字符串长度
print(gstr.count("l"))  # count统计次数
