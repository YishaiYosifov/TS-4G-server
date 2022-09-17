from __future__ import annotations

from common.request_constants import *
from typing import TYPE_CHECKING
from common.util import CONFIG

if TYPE_CHECKING: from common.client.command_client import CommandClient

def login(user : CommandClient, role : int, pcName : str, password : str):
    configRole = str(role)
    if not configRole in CONFIG["roles"]:
        user.error(Errors.INVALID_ROLE, f"Unknwon Role: {role}")
        return

    rolePassword = CONFIG["roles"][configRole]
    if rolePassword and password != rolePassword:
        user.error(Errors.INVALID_PASSWORD, "Invalid Password")
        return

    user.pcName = pcName
    user.role = role
    user.callback(Callbacks.LOGGED_IN_SUCCESSFULLY)

    if not role == 2: user.callback_to_all(Callbacks.USER_LOGGED_IN, {"user": user.to_dict()}, exclude=[user.id])
