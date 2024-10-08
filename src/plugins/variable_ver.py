"""
本模块是bingyue_dic的变量第二分装层
https://github.com/bingqiu456
点个星星 行不行
"""

from . import api_fn
from . import dic_match


    
class variable:

    @staticmethod
    async def core(event, *args):
        fn = {
            "$禁$":["set_group_ban", "group_id", "user_id", "duration", False],
            "$全体禁言$":["set_group_whole_ban", "group_id", "enable", True],
            "$改群名$":["set_group_name", "group_id", "group_name", False],
            "$改群名片$":["set_group_card", "group_id", "user_id", "card", False],
            "$群打卡$":["send_group_sign", "group_id", False],
            "$踢$":["set_group_kick", "group_id", "user_id", False]
        }
        n_ = {
            0:False,
            1:True,
            "0":False,
            "1":True
        }
        api_fn_class = api_fn.variable_ver_api_class
        api_fn_index = api_fn.variable_ver_api
        if args[0] in fn:
            x = fn[args[0]] # 获取对应的api调用参数
            m = {} # 构建发送api请求的数据
            n = args[1].split() # 获取需要发送的数据
            for i in range(1,len(x)-1):
                if n[i-1] in n_ and x[-1]: # 如果p字典对应的api参数开了true 代表要转译bool值
                    n[i-1] = n_[i-1] # 替换掉
                m[x[i]] = n[i-1] # 补充调用api的参数
            await dic_match.bot_cache.call_api(x[0], **m) # 调用api
            return
        elif args[0] in api_fn_index:
            api_message = api_fn_index[args[0]] # 获取到数据 0对应的是类名 1对应是你是否需要提供消息事件
            method = getattr(api_fn_class, api_message[0]) # 从api class里获取类名信息
            q = args[1].split()
            if api_message[1]:
                return await method(event,*q) # 附上参数 直接访问
            else:
                return await method(*q)
        else:
            return "error"
