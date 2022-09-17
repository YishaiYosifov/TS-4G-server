from __future__ import annotations

from common.request_constants import *
from typing import TYPE_CHECKING

import common.client.screenshare_client as screenshare_client
import random

if TYPE_CHECKING: from common.client.command_client import CommandClient

def start_screenshare(user : CommandClient, targetID : int):
    screenshareID = ""
    for i in range(5): screenshareID += str(random.randint(1, 9))
    screenshareID = int(screenshareID)

    screenshare_client.ScreenshareClient(user.connection, (user.ip, user.id), targetID, screenshareID)

    targetUser = user.users[targetID]
    targetUser.action(Actions.START_SCREENSHARE, {"target_id": targetID, "screenshare_id": screenshareID})

    user.callback(Callbacks.AWAITING_SCREENSHARE_CLIENT)
    user.screenshare = screenshareID
    user.closed = True

def init_target_screenshare(user : CommandClient, targetID : int, screenshareID : int):
    try: screenshareClient = screenshare_client.ScreenshareClient.users[targetID]
    except KeyError:
        user.error(Errors.NOT_TARGET, f"User {targetID} doesn't have a screenshare request")
        return
    if screenshareClient.screenshareID != screenshareID:
        user.error(Errors.INVALID_AUTHORIZATION, f"Incorrect Screenshare ID")
        return

    screenshareClient.targetUser = user
    screenshareClient.started = True
    user.users.pop(screenshareClient.id)

    user.callback(Callbacks.SCREENSHARE_STARTED)
    user.users.pop(user.id)
    user.closed = True

def click(user : CommandClient, targetID : int, x : int, y : int):
    targetUser = user.users[targetID]
    targetUser.action(Actions.CLICK, {"x": x, "y": y})
