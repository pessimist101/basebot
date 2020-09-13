import os
from datetime import datetime

def get_env(key, required=False, or_else=None):
    value = os.environ.get(key)
    if required and or_else:
        print(f"get_env(): for {key}, or_else parameter was ignored because this variable is required")
    if value is not None:
        return value
    else:
        if required:
            raise RuntimeError(f"Required environment variable {key} is missing.")
        else:
            return or_else

PREFIX = get_env("PREFIX", required=True)
TOKEN = get_env("TOKEN", required=True)
LOG_CHANNEL = int(get_env("LOG_CHANNEL", or_else="694838802660851712"))