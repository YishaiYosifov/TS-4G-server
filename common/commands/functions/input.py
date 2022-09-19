from __future__ import annotations

from common.request_constants import *
from typing import TYPE_CHECKING

if TYPE_CHECKING: from common.client.command_client import CommandClient

def unblock_input(user : CommandClient, targetID : int):
    targetUser = user.users[targetID]
    if not targetUser.blocked["input"]:
        user.error(Errors.USER_NOT_AFFECTED, f"Input for user {targetID} is not blocked")
        return
    targetUser.blocked["input"] = False

    targetUser.action(Actions.UNBLOCK_INPUT)
    user.callback(Callbacks.UNBLOCKED_INPUT_SUCCESSFULLY)

def block_input(user : CommandClient, targetID : int):
    targetUser = user.users[targetID]
    if targetUser.blocked["input"]:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Input for user {targetID} already blocked")
        return
    targetUser.blocked["input"] = True

    targetUser.action(Actions.BLOCK_INPUT)
    user.callback(Callbacks.BLOCKED_INPUT_SUCCESSFULLY)
