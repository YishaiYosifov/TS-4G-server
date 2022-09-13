from .validation import check_id
from typing import Any, Callable
from pydantic import BaseModel

class CommandArgument(BaseModel):
    name : str
    type : Any
    required : bool = True
    validation : Callable[[Any, Any], bool] = lambda connection, argument: True

class Command(BaseModel):
    role : int = 0
    arguments : list = {}

COMMANDS = {
    "login": Command(
        arguments=[
            CommandArgument(name="role", type=str),
            CommandArgument(name="password", type=str, required=False)
        ]),
    "block_input": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id)]),
    "unblock_input": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id)]),
    "block_screen": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id)]),
    "unblock_screen": Command(
        role=1,
        arguments=[CommandArgument(name="target_id", type=int, validation=check_id)]
    )
}