"""
Exceptions for the RecNetLogin clients
"""

class InvalidAccountCredentials(Exception):
    """Raised when the Rec Room account credentials are invalid."""
    def __init__(self) -> None:
        super().__init__("Unable to login to RecNet - Invalid Rec Room account credentials!")
        
class TwoFactorAuthenticatorEnabled(Exception):
    """Raised when the Rec Room account has 2FA enabled."""
    def __init__(self) -> None:
        super().__init__("Unable to login to RecNet - 2FA enabled!")