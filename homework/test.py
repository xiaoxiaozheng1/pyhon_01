# 方法：从文件中读取数据，返回的时列表形式的数据
from datetime import datetime


def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name, 'r')
        line = f.readline()  # 读出来的是字符串
        user_data = eval(line)  # 此方法是将字符串转化成对应的形式：如列表，元祖和字典
        return user_data
    except Exception as  e:
        print(e)
    finally:
        if not f:
            f.close()  # 这里的f可能是None,就不能调用close()方法


if __name__ == "__main__":
    result = from_file_get_data('user_data.txt')
    print(type(result))
    print(result)
    print(datetime.now())


a=[1,2,3,4,5,6,7,8,9]
b=a[:]
print(b)