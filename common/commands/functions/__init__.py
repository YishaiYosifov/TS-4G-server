from common.commands import COMMANDS

from .get_connected_users import *
from .screenshare import *
from .get_actions import *
from .screen import *
from .input import *
from .login import *
from .url import *

commandFunctions = {}
for command in COMMANDS.keys(): commandFunctions[command] = locals()[command]