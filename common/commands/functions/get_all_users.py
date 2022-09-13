from common.request_constants import *

def run(user):
    user.callback(Callbacks.USERS, {"users": [user.to_dict() for user in user.users.values()]})