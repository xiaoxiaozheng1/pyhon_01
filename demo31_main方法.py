# main ： __main__,每个文件都有一个名字，叫__main__


def div1(x, y):
    try:
        z = x / y
        return z
    except  Exception as e:  # 更加准确的是： except  ZeroDivisionError as e:
        print("除法不能出现被0除的现象")
        print(e)  # division by zero


print(div1(4, 4))
print(__name__)

if __name__ == '__main__':
    print(div1(3, 4))
