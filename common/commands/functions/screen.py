from __future__ import annotations

from common.request_constants import *
from typing import TYPE_CHECKING

if TYPE_CHECKING: from common.client.command_client import CommandClient

def block_screen(user : CommandClient, targetID : int):
    targetUser = user.users[targetID]
    if targetUser.blocked["screen"]:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Screen for user {targetID} already blocked")
        return
    targetUser.blocked["screen"] = True

    targetUser.action(Actions.BLOCK_SCREEN)
    user.callback(Callbacks.BLOCKED_SCREEN_SUCCESSFULLY)

def unblock_screen(user, targetID : int):
    targetUser = user.users[targetID]
    if not targetUser.blocked["screen"]:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Screen for user {targetID} not blocked")
        return
    targetUser.blocked["screen"] = False

    targetUser.action(Actions.UNBLOCK_SCREEN)
    user.callback(Callbacks.UNBLOCKED_SCREEN_SUCCESSFULLY)
