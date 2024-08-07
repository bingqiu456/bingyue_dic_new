"""
本模块是bingyue-dic
词库匹配逻辑
请勿随意更改
https://github.com/bingqiu456
"""

from . import start_dic
from . import load_file
from . import variable_main
from . import variable_v
from typing import List



async def match_sentence(event: any, word: str, bot: any) -> str:
    if word not in start_dic.keybox:
        return ""

    i_ = start_dic.keybox.index(word)  # 查找词库的索引
    if i_ == -1:
        return ""
    ans = ""  # 初始化匹配的答案
    dic_json = load_file.v  # 词库的json条
    p_start, p_end = start_dic.key_dict[i_][0] + 1, start_dic.key_dict[i_][1]  # 读取初始化的索引和终止索引
    global bot_cache
    bot_cache = bot

    while p_start <= p_end:

        if len(dic_json)-1 == p_start:
            now_text = dic_json[p_start]
        else:
            now_text = dic_json[p_start][:-1]

        ans += await get_var(event.model_dump(), now_text)
        p_start += 1

    return ans.replace("\\n", "\n").replace("\\r", "\r")  # 换行转译


async def get_var(event: any, s: str) -> str:
    """
    变量匹配
    利用了栈的性质去匹配
    最后返回是处理好的字符

    https://github.com/bingqiu456
    """
    stack = []
    p = {
        "%": "variable_main_event",
        "$": "variable_u_event"
    }
    t_ = False
    for i in range(0, len(s)):
        temp = s[i]
        if temp == "$":
            t_ = True
        while s[i] in p and s[i] in stack:
            temp += stack.pop()
        temp = temp[::-1].split(maxsplit=1) + ["?"] # 给临时数组一个占位符 解决%变量只有一个长度
        if len(temp[0]) != 1:
            m = await variable.__dict__.get(p[temp[0][0]]).__func__(event, temp[0], temp[1], t_)
            if p[temp[0][0]] == "$":
                t_ = False 
            if m:
                stack.append(m)
        else:
            stack.append(s[i])

    if not stack:
        return ""
    return "".join(stack)

    # """
    # 获取变量
    # 测试示例 $管理员 %QQ%$
    # """
    # ans = ""
    # k = []
    # temp = ""
    # m = {
    #     "$": "variable_u_event",
    #     "%": "variable_main_event"
    # }
    # for i in range(len(s)):
    #     print(ans, k, temp) # debug
    #     if s[i] in ["$", "%"]:
    #         if s[i] in k and k.pop() == s[i]:
    #             try:
    #                 temp = await variable.__dict__.get(m[s[i]]).__func__(event, temp + s[i])
    #             except IndexError:
    #                 pass
    #             temp = ""
    #             continue
    #         else:
    #             k.append(s[i])
    #
    #     temp += s[i]
    # print(ans,k,temp)
    # if k:
    #     if k.pop() == temp[0]:
    #         print(temp + temp[0])
    #         ans += await variable.__dict__.get(m[temp[0]]).__func__(event, temp + temp[0])
    #         temp = ""
    #
    # ans += temp
    # return ans


class variable:

    @staticmethod
    async def variable_main_event(event: any, s: str, *args) -> str:
        """
        %变量对应的环境扩展
        """
        k = await variable_main.Variable.__dict__.get("event_get").__func__(event, s)
        if args[1]:
            return k[::-1]
        return k

    @staticmethod
    async def variable_u_event(event: any, s: str, temp: List[str], *args) -> str:
        """
        $变量
        """
        k = await variable_v.variable.__dict__.get("core").__func__(event,s+"$" , temp[:-1])
        return k
