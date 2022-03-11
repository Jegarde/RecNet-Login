import traceback
from recnetlogin import RecNetLogin
from recnetlogin.exceptions import *

# Insert your Rec Room account credentials
USERNAME: str = ""
PASSWORD: str = ""

def main() -> None:
    rnl = RecNetLogin(username=USERNAME, password=PASSWORD)
    # rnl = RecNetLogin(username=USERNAME, password=PASSWORD, prompt_2fa=True)  <- Fixes TwoFactorAuthenticatorProcessDisabled 
    
    try:
        token = rnl.get_token(include_bearer=True)
        decoded_token = rnl.get_decoded_token()
    except Lockout:  # Account login rate limited!
        print(f"{USERNAME} is locked out!")
        return
    except InvalidAccountCredentials:  # Invalid account credentials!
        print(f"Wrong account credentials for {USERNAME}!")
        return    
    except TwoFactorAuthenticatorProcessDisabled:  # 2FA prompting disabled
        print("Two factor authentication process is disabled! To enable it, include 'prompt_2fa=True' in the instance initialization.")
        return    
    except TwoFactorAuthenticatorCancelled:  # Left 2FA prompt empty
        print("Two factor authenticator process was cancelled by leaving the prompt empty!")
        return
    except Exception:  # Uncaught exception
        traceback.print_exc()
        return
    
    print(f"{token=}\n{decoded_token=}")

if __name__ == "__main__":
    main()