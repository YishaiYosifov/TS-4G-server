class Errors:
    CANNOT_PERFORM_ON_YOURSELF = "cannot_perform_on_yourself"
    USER_ALREADY_AFFECTED = "user_already_affected"
    INVALID_REQUEST_TYPE = "invalid_request_type"
    INSUFFICIENT_ROLE = "insufficient_role"
    USER_NOT_AFFECTED = "user_not_affected"
    MISSING_ARGUMENT = "missing_argument"
    INVALID_PASSWORD = "invalid_password"
    INVALID_USER_ID = "invalid_user_id"
    WRONG_DATA_TYPE = "wrong_data_type"
    USER_IS_HOST = "user_is_host"
    INVALID_TYPE = "invalid_type"
    INVALID_ROLE = "invalid_role"

class Callbacks:
    BLOCKED_SCREEN_SUCCESSFULLY = "blocked_screen"
    UNBLOCKED_SCREEN_SUCCESSFULLY = "unblocked_screen"
    UNBLOCKED_INPUT_SUCCESSFULLY = "unblocked_input"
    BLOCKED_INPUT_SUCCESSFULLY = "blocked_input"
    LOGGED_IN_SUCCESSFULLY = "logged_in"

class Actions:
    UNBLOCK_SCREEN = "unblock_screen"
    UNBLOCK_INPUT = "unblock_input"
    BLOCK_SCREEN = "block_screen"
    BLOCK_INPUT = "block_input"