from loguru import logger

logger.info("hello world")
logger.debug("这是debug日志")
logger.warning("这是warning日志")
logger.success("这是success日志")
logger.error("这是error日志")

# logger.add('a.log', level='DEBUG')
logger.add('a.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {line} | {message} )|", level='DEBUG')
logger.info("hello world")
logger.debug("这是debug日志")
logger.warning("这是warning日志")
logger.success("这是success日志")
logger.error("这是error日志")
logger.critical("这是critical日志")

logger.info("我的名字叫{}爱学{}", "小争", "测试")
logger.info("我的名字叫{}爱学{}".format("小争", "测试"))
