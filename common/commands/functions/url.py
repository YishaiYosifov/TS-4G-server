from __future__ import annotations

from common.request_constants import *
from ..validation import validate_url
from common.util import format_url
from typing import TYPE_CHECKING

if TYPE_CHECKING: from common.client.command_client import CommandClient

def block_url(user : CommandClient, targetID : int, url : str):
    url = format_url(url)
    if not validate_url(user, url): return
    
    targetUser = user.users[targetID]
    if url in targetUser.blocked["urls"]:
        user.error(Errors.USER_ALREADY_AFFECTED, f"URL already blocked")
        return
    targetUser.blocked["urls"].append(url)

    targetUser.action(Actions.BLOCK_URL, {"url": url})
    user.callback(Callbacks.BLOCKED_URL_SUCCESSFULLY)

def unblock_url(user : CommandClient, targetID : int, url : str):
    url = format_url(url)

    targetUser = user.users[targetID]
    if not url in targetUser.blocked["urls"]:
        user.error(Errors.USER_NOT_AFFECTED, f"URL not blocked")
        return
    targetUser.blocked["urls"].remove(url)

    targetUser.action(Actions.UNBLOCK_URL, {"url": url})
    user.callback(Callbacks.UNBLOCKED_URL_SUCCESSFULLY)

def set_blocked_urls(user : CommandClient, urls : list):
    for url in urls:
        url = format_url(url)
        
        if not validate_url(user, url): continue
        elif not url in user.blocked["urls"]: user.blocked["urls"].append(url)
    
    print(user.blocked["urls"])
    
    user.callback(Callbacks.SET_BLOCKED_URLS_SUCCESSFULLY)
