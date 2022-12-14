class Errors:
    CANNOT_PERFORM_ON_YOURSELF = "cannot_perform_on_yourself"
    USER_IS_HOST = "user_is_host"

    USER_ALREADY_AFFECTED = "user_already_affected"
    USER_NOT_AFFECTED = "user_not_affected"

    INSUFFICIENT_ROLE = "insufficient_role"
    MISSING_ARGUMENT = "missing_argument"
    WRONG_DATA_TYPE = "wrong_data_type"

    NOT_TARGET = "not_target"
    
    INVALID_REQUEST_TYPE = "invalid_request_type"
    INVALID_PASSWORD = "invalid_password"
    INVALID_USER_ID = "invalid_user_id"
    INVALID_TYPE = "invalid_type"
    INVALID_ROLE = "invalid_role"
    INVALID_URL = "invalid_url"

    INVALID_AUTHORIZATION = "invalid_authorization"

class Callbacks:
    UNBLOCKED_SCREEN_SUCCESSFULLY = "unblocked_screen"
    BLOCKED_SCREEN_SUCCESSFULLY = "blocked_screen"

    UNBLOCKED_INPUT_SUCCESSFULLY = "unblocked_input"
    BLOCKED_INPUT_SUCCESSFULLY = "blocked_input"

    SET_BLOCKED_URLS_SUCCESSFULLY = "set_blocked_urls"
    UNBLOCKED_URL_SUCCESSFULLY = "unblocked_url"
    BLOCKED_URL_SUCCESSFULLY = "blocked_url"
    
    LOGGED_IN_SUCCESSFULLY = "logged_in"
    USER_DISCONNECTED = "user_disconnected"
    USER_LOGGED_IN = "user_logged_in"

    AWAITING_SCREENSHARE_CLIENT = "awaiting_screenshare_client"
    SCREENSHARE_STARTED = "screenshare_started"

    AVAILABLE_ACTIONS = "actions"
    USERS = "users"

class Actions:
    UNBLOCK_INPUT = "unblock_input"
    BLOCK_INPUT = "block_input"

    UNBLOCK_SCREEN = "unblock_screen"
    BLOCK_SCREEN = "block_screen"

    UNBLOCK_URL = "unblock_url"
    BLOCK_URL = "block_url"

    START_SCREENSHARE = "start_screenshare"

    CLICK = "click"
