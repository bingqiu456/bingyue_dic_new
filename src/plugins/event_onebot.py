"""
本层是bingyue_dic的发消息交互
目前只支持群聊 消息
未来的消息未来支持
https://github.com/bingqiu456
"""

from nonebot import on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from . import dic_match
from nonebot import get_driver


async def judge_group(event: GroupMessageEvent):
    return event.group_id in config_group


a = on_message(priority=10, rule=judge_group)
config_group = get_driver().config.dict().get("start_group", [])


@a.handle()
async def _(event: GroupMessageEvent):
    await a.finish(await dic_match.match_sentence(event, event.get_plaintext()))
