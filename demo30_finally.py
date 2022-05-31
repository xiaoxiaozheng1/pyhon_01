# 错误和异常


# 使用try ...except ...finally语句
"""
语法格式：
try:
    正常代码块
except Exception as e:
    处理异常代码块
finally:
    必须执行的代码块
"""
try:
    f = open('a.txt', 'r')

    lines = f.readlines()
    print(2 / 0)  # 如果这里出错后面的不会执行。
    for x in lines:
        print(x)

    # f.close()

except Exception as e:
    print(e)

finally:
    print("是否运行该代码区域")
    f.close()
