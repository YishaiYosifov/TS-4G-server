from __future__ import annotations

from common.request_constants import *
from typing import TYPE_CHECKING

if TYPE_CHECKING: from common.client.command_client import CommandClient

def get_connected_users(user : CommandClient):
    user.callback(Callbacks.USERS, {"users": [user.to_dict() for user in user.users.values()]})
