from common.request_constants import *

def get_all_users(user): user.callback(Callbacks.USERS, {"users": [user.to_dict() for user in user.users.values()]})
