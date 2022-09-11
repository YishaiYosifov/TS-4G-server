REQUEST_TYPES = {
    "login": {"role": int, "_password": str}
}

class Errors:
    INVALID_REQUEST_TYPE = "invalid_request_type"
    MISSING_ARGUMENT = "missing_argument"
    WRONG_DATA_TYPE = "wrong_data_type"
    INVALID_TYPE = "invalid_type"