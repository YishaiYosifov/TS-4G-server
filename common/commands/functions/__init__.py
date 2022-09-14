from common.commands import COMMANDS

from .get_all_users import *
from .get_actions import *
from .screen import *
from .input import *
from .login import *

commandFunctions = {}
for command in COMMANDS.keys(): commandFunctions[command] = locals()[command]