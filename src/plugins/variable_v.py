"""
本模块是bingyue_dic的变量第二分装层
https://github.com/bingqiu456
点个星星 行不行
"""

from . import start_dic

class variable:

    @staticmethod
    def admin(event, *args):
        ans = []
        for arg in args:
            print(arg)
            if start_dic.date_tree.search(arg):
                ans.append(arg)
            else:
                ans.append("0")
        return ans[0] if len(ans) == 1 else ans