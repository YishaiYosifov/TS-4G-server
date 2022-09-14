from common.request_constants import *

def unblock_input(user, targetID):
    targetUser = user.users[targetID]
    if not targetUser.inputBlocked:
        user.error(Errors.USER_NOT_AFFECTED, f"Input for user {targetID} is not blocked")
        return
    targetUser.inputBlocked = False

    targetUser.action(Actions.UNBLOCK_INPUT)
    user.callback(Callbacks.UNBLOCKED_INPUT_SUCCESSFULLY)

def block_input(user, targetID):
    targetUser = user.users[targetID]
    if targetUser.inputBlocked:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Input for user {targetID} already blocked")
        return
    targetUser.inputBlocked = True

    targetUser.action(Actions.BLOCK_INPUT)
    user.callback(Callbacks.BLOCKED_INPUT_SUCCESSFULLY)

