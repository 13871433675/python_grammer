# 内建模块测试
import calendar
import time
from datetime import datetime

if __name__ == '__main__':
    # datetimeTest 获取当前日期和时间
    print(datetime.now())
    # 获取指定日期和时间
    dt = datetime(2019, 6, 5, 12, 00)
    print(dt)
    # 日期转换为时间戳
    print(datetime.timestamp(dt))
    # 时间戳转换为日期 本地时间
    print(datetime.fromtimestamp(datetime.timestamp(dt)))
    # UTC时间
    print(datetime.utcfromtimestamp(datetime.timestamp(dt)))

    # 日期转换为字符串
    print("日期转为字符串"+datetime.now().strftime('%Y,%m,%d'))
    # 日期计算


    # 获取当前时间
    print(time.asctime(time.localtime(time.time())))
    # python中时间日期格式化符号：
    # % y
    # 两位数的年份表示（00 - 99）
    # % Y
    # 四位数的年份表示（000 - 9999）
    # % m
    # 月份（01 - 12）
    # % d
    # 月内中的一天（0 - 31）
    # % H
    # 24
    # 小时制小时数（0 - 23）
    # % I
    # 12
    # 小时制小时数（01 - 12）
    # % M
    # 分钟数（00 = 59）
    # % S
    # 秒（00 - 59）
    # % a
    # 本地简化星期名称
    # % A
    # 本地完整星期名称
    # % b
    # 本地简化的月份名称
    # % B
    # 本地完整的月份名称
    # % c
    # 本地相应的日期表示和时间表示
    # % j
    # 年内的一天（001 - 366）
    # % p
    # 本地A.M.或P.M.的等价符
    # % U
    # 一年中的星期数（00 - 53）星期天为星期的开始
    # % w
    # 星期（0 - 6），星期天为星期的开始
    # % W
    # 一年中的星期数（00 - 53）星期一为星期的开始
    # % x
    # 本地相应的日期表示
    # % X
    # 本地相应的时间表示
    # % Z
    # 当前时区的名称
    # % % % 号本身

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 获取某月的日历
    cal = calendar.month(2019, 6)
