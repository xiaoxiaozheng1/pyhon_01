# 读取文件：

# 1)打开文件 : open(filename,mode) #filename代表的是文件名， mode : 读写模式
f = open('a.txt', 'r')

# 2)读取所有的行 : readlines() 这个内容是放在列表当中的
for x in f.readlines():
    print(x)

# 3)关闭文件  ： close()
f.close()

# f = open('a.txt', 'r')
# for x in f.readlines():
#     print(x)
# f.close()
