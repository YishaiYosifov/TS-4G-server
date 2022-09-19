from __future__ import annotations

from common.request_constants import Errors
from typing import TYPE_CHECKING

import validators

if TYPE_CHECKING: from common.client.command_client import CommandClient

def check_id(user : CommandClient, userID : int) -> bool:
    if not userID in user.users:
        user.error(Errors.INVALID_USER_ID, f"Invalid User ID: {userID}")
        return False

    targetUser = user.users[userID]
    if targetUser == user:
        user.error(Errors.CANNOT_PERFORM_ON_YOURSELF, f"You cannot perform this action on yourself")
        return False
    
    return True

def check_id_no_host(user: CommandClient, userID : int):
    if not check_id(user, userID): return False
    
    targetUser = user.users[userID]
    if targetUser.role > 0:
        user.error(Errors.USER_IS_HOST, f"You cannot perform this action on a host")
        return False

    return True

def validate_url(user : CommandClient, url : str):
    if not validators.url("https://" + url) or not isinstance(url, str):
        user.error(Errors.INVALID_URL, f"Invalid URL: {url}")
        return False
    
    return True
