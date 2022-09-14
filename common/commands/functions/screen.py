from common.request_constants import *

def block_screen(user, targetID):
    targetUser = user.users[targetID]
    if targetUser.screenBlocked:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Screen for user {targetID} already blocked")
        return
    targetUser.screenBlocked = True

    targetUser.action(Actions.BLOCK_SCREEN)
    user.callback(Callbacks.BLOCKED_SCREEN_SUCCESSFULLY)

def unblock_screen(user, targetID):
    targetUser = user.users[targetID]
    if not targetUser.screenBlocked:
        user.error(Errors.USER_ALREADY_AFFECTED, f"Screen for user {targetID} not blocked")
        return
    targetUser.screenBlocked = False

    targetUser.action(Actions.UNBLOCK_SCREEN)
    user.callback(Callbacks.UNBLOCKED_SCREEN_SUCCESSFULLY)
