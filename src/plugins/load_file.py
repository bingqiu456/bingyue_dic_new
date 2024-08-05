"""
本模块是`bingyue-dic`
加载文件模块
请勿随意更改
https://github.com/bingqiu456
"""

from nonebot.log import logger
import os

if not os.path.isdir("./data"):
    os.mkdir("data")
    logger.warning("检测到data文件夹不存在，已创建")

logger.success("词库系统启动中....")
logger.success("开始加载词库.....")

try:
    with open("./data/dic.txt", "r+", encoding="utf_8") as f:
        v = f.readlines()
        f.close()
except FileNotFoundError:
    with open("./data/dic.txt", "w+", encoding="utf_8") as f:
        f.write("测试\n测试")
        f.close()
        v = ["测试", "\n测试"]
    logger.warning("检测到词库不存在，已为你创建一个")
