class Test:
    a = "a"
    b = "b"
[print(variable) for variable in Test.__dict__ if not callable(variable) and not variable.startswith("__")]