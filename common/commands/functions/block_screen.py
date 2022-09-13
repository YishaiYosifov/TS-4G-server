from common.request_constants import *

def run(user, targetID):
    targetUser = user.users[targetID]
    if targetUser.screenBlocked:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Screen for user {targetID} already blocked")
        return
    targetUser.screenBlocked = True

    targetUser.action(Actions.BLOCK_SCREEN)
    user.callback(Callbacks.BLOCKED_SCREEN_SUCCESSFULLY)