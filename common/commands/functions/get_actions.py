from __future__ import annotations

from common import Callbacks, Actions
from typing import TYPE_CHECKING

if TYPE_CHECKING: from common.client.command_client import CommandClient

def get_actions(user : CommandClient):
    availableActions = [action for action in Actions.__dict__ if not callable(action) and not action.startswith("__")]
    user.callback(Callbacks.AVAILABLE_ACTIONS, {"actions": availableActions})