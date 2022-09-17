from typing import Any, Callable
from pydantic import BaseModel
from .validation import *

class CommandArgument(BaseModel):
    name : str
    type : Any
    required : bool = True
    validation : Callable[[Any, Any], bool] = lambda connection, argument: True

class Command(BaseModel):
    role : int = None
    arguments : list = {}

COMMANDS = {
    "login": Command(
        arguments=[
            CommandArgument(name="role", type=int),
            CommandArgument(name="pc_name", type=str, required=False),
            CommandArgument(name="password", type=str, required=False)]),

    "block_input": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id_no_host)]),
    "unblock_input": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id_no_host)]),

    "block_screen": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id_no_host)]),
    "unblock_screen": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id_no_host)]),

    "start_screenshare": Command(
        role=2,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id_no_host)]),
    "init_target_screenshare": Command(
        arguments=[
            CommandArgument(name="target_id", type=int, validation=check_id),
            CommandArgument(name="screenshare_id", type=int)]),
    
    "click": Command(
        role=1,
        arguments=[
            CommandArgument(name="target_id", type=int, validation=check_id_no_host),
            CommandArgument(name="x", type=int),
            CommandArgument(name="y", type=int)]),

    "get_connected_users": Command(role=1),
    "get_actions": Command()
}
