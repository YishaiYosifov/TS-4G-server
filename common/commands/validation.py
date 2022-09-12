from common import *

def check_id(user, userID : int) -> bool:
    if not userID in user.users:
        user.error(Errors.INVALID_USER_ID, f"Invalid User ID: {userID}")
        return False

    targetUser = user.users[userID]
    if targetUser == user:
        user.error(Errors.CANNOT_PERFORM_ON_YOURSELF, f"You cannot perform this action on yourself")
        return False
    elif targetUser.role > 0:
        user.error(Errors.USER_IS_HOST, f"You cannot perform this action on a host")
        return False
    
    return True