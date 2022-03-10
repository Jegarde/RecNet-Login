import traceback
from recnetlogin import RecNetLogin
from recnetlogin.exceptions import TwoFactorAuthenticatorEnabled, InvalidAccountCredentials

# Insert your Rec Room account credentials
USERNAME: str = ""
PASSWORD: str = ""

def main() -> None:
    rnl = RecNetLogin(username=USERNAME, password=PASSWORD)
    
    try:
        token = rnl.get_token(include_bearer=True)
        decoded_token = rnl.get_decoded_token()
    except TwoFactorAuthenticatorEnabled:  # 2FA enabled!
        print("FAILED TO LOGIN!")
        print(f"{USERNAME} has two factor authenticator enabled!")
        return
    except InvalidAccountCredentials:  # Invalid account credentials!
        print("FAILED TO LOGIN!")
        print(f"Wrong account credentials for {USERNAME}!")
        return    
    except Exception:  # Uncaught exception
        traceback.print_exc()
        return
    
    print(f"{token=}\n{decoded_token=}")

if __name__ == "__main__":
    main()