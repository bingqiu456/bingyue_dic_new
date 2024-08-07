"""
本模块是bingyue-dic
词库核心加载模块
请勿随意更改
`https://github.com/bingqiu456`
"""

from . import load_file
from . import date_tree
from typing import List
from nonebot import get_driver

dic_json = load_file.v  # 词库的文本,每一行
key_dict = []  # 词库的索引 对应每个功能从文本的第几行到第几行
keybox = []  # 词库的指令

date_tree = date_tree.DataTree()
owner_dic = str(get_driver().config.dict().get("onwer_dic", "0"))
admin_dic = get_driver().config.dict().get("admin_dic", [])
date_tree.add_list(admin_dic)

def load_key(i: List[str]) -> None:
    """
    读取词库的指令
    并加载每个功能的第一行和结尾行
    return List[int,int]
    """
    t = False if i[0] == "\n" else True  # 利用这个维持状态 true代表找到了触发句 但还没找到终止的地方
    i_ = 0  # 初始化指针
    for p in range(len(i)):
        # 当出现换行没有东西的时候 判断一下状态
        if i[p] == "\n" and t:
            keybox.append(i[i_][:-1])
            key_dict.append([i_, p - 1])
            t = False
        elif i[p] != "\n" and not t:
            t = True
            i_ = p
        else:
            continue
    # 防止末尾出现 不换行
    if t:
        keybox.append(i[i_][:-1])
        key_dict.append([i_, len(i) - 1])


load_key(dic_json)
