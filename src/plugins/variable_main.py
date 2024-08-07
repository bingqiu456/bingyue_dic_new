"""
本模块是bingyue-dic
词库的主要变量 是%的变量
请勿随意更改
`https://github.com/bingqiu456`
"""

from . import start_dic
import time

class api:

    @staticmethod
    async def owner_qq(*args):
        return start_dic.owner_dic
    
    @staticmethod
    async def get_times(*args):
        return str(int(time.time()))

    @staticmethod
    async def test_var(*args): # 这里类名要改成你自己设置的 
        return "测试"

class Variable:
    
    @staticmethod
    async def event_get(event, *args):
        """
        读取event事件的消息
        """
        p = {
            "%QQ%":"user_id",
            "%Robot%":"self_id",
            "%消息id%":"message_seq",
            "%群号%":"group_id",
        }
        v = {
           "%主人%":"owner_qq",
           "%time%":"get_times",
           "%test%":"test_var"
        }
        if args[0] in p:
            x = p[args[0]]
            return str(event[x])
        elif args[0] in v:
            method = getattr(api, v[args[0]], None)
            return await method()
        else:
            return "error"

