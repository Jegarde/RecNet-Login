"""
Exceptions for the RecNetLogin clients
"""

EXCEPTION_SIGNATURE = "Unable to login to RecNet – "

class Lockout(Exception):
    """Raised when the Rec Room account is locked out."""
    def __init__(self) -> None:
        super().__init__(EXCEPTION_SIGNATURE + "Rec Room account locked!")

class InvalidAccountCredentials(Exception):
    """Raised when the Rec Room account credentials are invalid."""
    def __init__(self) -> None:
        super().__init__(EXCEPTION_SIGNATURE + "Invalid Rec Room account credentials!")

class TwoFactorAuthenticatorCodeWrong(Exception):
    """Raised when the Authenticator code is wrong."""
    def __init__(self) -> None:
        super().__init__(EXCEPTION_SIGNATURE + "Wrong Authenticator code!")
        
class TwoFactorAuthenticatorEnabled(Exception):
    """Raised when the Rec Room account has 2FA enabled."""
    def __init__(self) -> None:
        super().__init__(EXCEPTION_SIGNATURE + "2FA enabled!")

class TwoFactorAuthenticatorCancelled(Exception):
    """Raised when the authentication process is cancelled."""
    def __init__(self) -> None:
        super().__init__(EXCEPTION_SIGNATURE + "2FA authentication cancelled!")

class TwoFactorAuthenticatorProcessDisabled(Exception):
    """Raised when the authentication process is disabled."""
    def __init__(self) -> None:
        super().__init__(EXCEPTION_SIGNATURE + "2FA authentication process disabled!")