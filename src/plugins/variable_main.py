"""
本模块是bingyue-dic
词库的主要变量 是%的变量
请勿随意更改
`https://github.com/bingqiu456`
"""


class Variable:
    
    @staticmethod
    def QQ(event, *args):
        return event.get_user_id()
        
    @staticmethod
    def bot_qq(event, *args):
        return str(event.self_id)
    
    @staticmethod
    def id(event, *args):
        return str(event.m())

    @staticmethod
    def message_id(event, *args):
        return str(event.message_id)

    @staticmethod
    def group_id(event, *args):
        return str(event.group_id)
    