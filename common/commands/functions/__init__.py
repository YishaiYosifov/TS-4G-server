from .get_all_users import run as get_all_users

from .unblock_screen import run as unblock_screen
from .block_screen import run as block_screen

from .unblock_input import run as unblock_input
from .block_input import run as block_input

from .login import run as login

import os

commandFunctions = {}
for file in os.listdir("common/commands/functions"):
    if not file.endswith(".py") or file == "__init__.py" or os.path.isdir(f"common/actions/{file}"): continue

    file = file.removesuffix(".py")
    commandFunctions[file] = locals()[file]
