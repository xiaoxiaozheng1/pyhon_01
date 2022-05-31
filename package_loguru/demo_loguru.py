# loguru模块
"""功能
1.可以格式化日志
2.着色（不同的颜色）
3.生成到文件
4.显示不同的日志级别
5，只使用一个对象（非常方便）

"""
# 1.下载安装：pip install loguru

# 2.导包
from loguru import logger

# 3.打印一条日志：hello world
logger.info("hello world")

# 输出不同的日志级别，分别是debug,info,warning,success,error
logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

# 输出到文件 ：add()
# logger.add('a.log', level='DEBUG')
logger.add('a.log', format="{time:YYYY-MM-DD  HH:mm:ss}|{level}|{module}|{line}|{message}", level='DEBUG')
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

# 进行传入参数的格式化：
logger.info("我的名字叫{},今天星期{}", '张三', '1')
