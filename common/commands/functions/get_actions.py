from common import Callbacks, Actions

def get_actions(user):
    availableActions = [action for action in Actions.__dict__ if not callable(action) and not action.startswith("__")]
    user.callback(Callbacks.AVAILABLE_ACTIONS, {"actions": availableActions})