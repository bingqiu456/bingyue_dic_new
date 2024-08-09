from . import start_dic
import time

class variable_main_api_class:

    @staticmethod
    async def owner_qq(*args):
        return start_dic.owner_dic
    
    @staticmethod
    async def get_times(*args):
        return str(int(time.time()))

    @staticmethod
    async def test_var(*args): # 这里类名要改成你自己设置的 
        return "测试"
    
class variable_ver_api_class:

    @staticmethod
    async def admin(*args):
        ans = []
       
        for arg in args:
            if start_dic.date_tree.search(arg):
                ans.append(str(arg))
            
        if not ans:
            return "0"
        elif len(ans) == 1:
            return ans[0]
        else:
            return str(ans)
    
    @staticmethod
    async def get_message_type(event,*args):
        a = list(event.get_message())
        i = 0
        target = args[0]
        for i_ in a:
            if i_.type == target:
                if i == int(args[1]):
                    return i_.data["qq"]
                i+=1
            else:
                continue
        return ""

    @staticmethod
    async def guess_size(*args):
        i_ = int(args[0])
        for i in args:
            i_ = max(i_, int(i))
        return str(i_)
    
variable_main_api = {
        "%主人%":"owner_qq",
        "%time%":"get_times",
        "%test%":"test_var"
    }

variable_ver_api = {
        "$管理员$":["admin",False],
        "$获取消息$":["get_message_type",True],
        "$猜大小$":["guess_size", False]
    }