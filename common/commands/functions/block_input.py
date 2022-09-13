from common.request_constants import *

def run(user, targetID : int):
    targetUser = user.users[targetID]
    if targetUser.inputBlocked:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Input for user {targetID} already blocked")
        return
    targetUser.inputBlocked = True

    targetUser.action(Actions.BLOCK_INPUT)
    user.callback(Callbacks.BLOCKED_INPUT_SUCCESSFULLY)
