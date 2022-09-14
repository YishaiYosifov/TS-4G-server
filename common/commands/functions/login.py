from common.request_constants import *
from common import CONFIG

def login(user, role : int, pcName : str, password : str):
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

    user.callback_to_all(Callbacks.USER_LOGGED_IN, {"user": user.to_dict()}, exclude=[user.id])
