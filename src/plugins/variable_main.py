"""
本模块是bingyue-dic
词库的主要变量 是%的变量
请勿随意更改
`https://github.com/bingqiu456`
"""

from . import api_fn



class Variable:
    
    @staticmethod
    async def event_get(event, *args):
        """
        读取event事件的消息
        """
        fn = {
            "%QQ%":"user_id",
            "%Robot%":"self_id",
            "%消息id%":"message_seq",
            "%群号%":"group_id",
        }
        api_fn_class = api_fn.variable_main_api_class
        api_fn_index = api_fn.variable_main_api
        if args[0] in fn:
            x = fn[args[0]]
            return str(event[x])
        elif args[0] in api_fn_index:
            method = getattr(api_fn_class, api_fn_index[args[0]], None)
            return await method()
        else:
            return "error"

