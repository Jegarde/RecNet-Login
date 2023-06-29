class CookieMissing(Exception):
    """Raised when RecNet cookie is missing from environmental variables"""
    def __init__(self) -> None:
        super().__init__("Missing RN_COOKIE environmental variable! Try restarting your computer or make a .env.secret file.")

class InvalidLocalCookie(Exception):
    """Raised when RecNet cookie is not valid for getting the token from a .env.secret file"""
    def __init__(self) -> None:
        super().__init__("RN_COOKIE is not valid or has expired! Check your .env.secret file and its path.")

class InvalidSystemCookie(Exception):
    """Raised when RecNet cookie is not valid for getting the token from system environment variables"""
    def __init__(self) -> None:
        super().__init__("RN_COOKIE environmental variable is not valid or has expired! Check your environment variables and try restarting your computer.")