from common import Callbacks, Actions

def get_actions(user): user.callback(Callbacks.ACTIONS, {"commands": list(Actions.keys())})