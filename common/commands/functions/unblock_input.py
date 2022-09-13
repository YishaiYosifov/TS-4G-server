from common.request_constants import *

def run(user, targetID):
    targetUser = user.users[targetID]
    if not targetUser.inputBlocked:
        user.error(Errors.USER_NOT_AFFECTED, f"Input for user {targetID} is not blocked")
        return
    targetUser.inputBlocked = False

    targetUser.action(Actions.UNBLOCK_INPUT)
    user.callback(Callbacks.UNBLOCKED_INPUT_SUCCESSFULLY)
