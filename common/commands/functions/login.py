from common.request_constants import *
from common import CONFIG

def run(user, role : int, pcName, password : str):
    if not role in CONFIG["roles"]:
        user.error(Errors.INVALID_ROLE, f"Unknwon Role: {role}")
        return

    rolePassword = CONFIG["roles"][role]
    if rolePassword and password != rolePassword:
        user.error(Errors.INVALID_PASSWORD, "Invalid Password")
        return
    
    user.pcName = pcName
    user.role = int(role)
    user.callback(Callbacks.LOGGED_IN_SUCCESSFULLY)