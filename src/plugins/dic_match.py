"""
本模块是bingyue-dic
词库匹配逻辑
请勿随意更改
https://github.com/bingqiu456
"""


from . import start_dic
from . import load_file
from . import variable_main

async def match_sentence(event: any, word: str) -> str:
    
    if word not in start_dic.keybox:
        return ""
    
    i_ = start_dic.keybox.index(word) # 查找词库的索引
    if i_ == -1:
        return ""
    ans = "" # 初始化匹配的答案
    dic_json = load_file.v # 词库的json条
    p_start, p_end = start_dic.key_dict[i_][0]+1, start_dic.key_dict[i_][1] # 读取初始化的索引和终止索引

    while p_start <= p_end:

        now_text = dic_json[p_start][:-1].replace("'\n'","\n").replace("'\r'","\r") # 先转移一下换行

        ans+= await get_var(event, now_text)
        p_start+=1
    
    print(ans)
    return ans

async def get_var(event: any, s: str) -> str:
    """
    获取变量
    测试示例 $管理员 %QQ%$
    """
    ans = ""
    k = []
    temp = ""
    for i in range(len(s)):
        if s[i] in ["$","%"]:
            if s[i] in k and k.pop() == s[i]:
                ans+= await variable_main_event(event,temp+s[i])
                temp = ""
            else:
                k.append(s[i])
                temp += s[i]
        else:
            temp += s[i]
    ans+=temp
    return ans


async def variable_main_event(event: any, s: str) -> str:
    "变量对应名字的扩展"
    v_ = {
        "%QQ%":"QQ",
        "%Robot%":"bot_qq",
        "%消息id%":"message_id",
        "%群号%":"group_id"
    }
    p = variable_main.Variable
    k = p.__dict__.get(v_[s]).__func__(event)
    return k