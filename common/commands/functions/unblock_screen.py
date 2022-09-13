from common.request_constants import *

def run(user, targetID):
    targetUser = user.users[targetID]
    if not targetUser.screenBlocked:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Screen for user {targetID} not blocked")
        return
    targetUser.screenBlocked = False

    targetUser.action(Actions.UNBLOCK_SCREEN)
    user.callback(Callbacks.UNBLOCKED_SCREEN_SUCCESSFULLY)