import jwt
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, quote
from .api_info import ApiInfo
from .exceptions import *

def parse_token(url: str) -> tuple:
    redirect_url = str(url).replace("#", "?")  # Patch the URL
    if 'Lockout' in redirect_url: raise Lockout
    if 'LoginWith2fa' in redirect_url: raise TwoFactorAuthenticatorEnabled  # 2FA enabled! 
    if 'access_token' not in redirect_url: raise InvalidAccountCredentials  # Login unsuccessful!
    parsed_url = urlparse(redirect_url)
    bearer_token = parse_qs(parsed_url.query)['access_token'][0]  # Acquire the bearer token from the URL
    return bearer_token

def decode_token(token: str) -> dict:
    decoded = jwt.decode(token, options={"verify_signature": False})  # Decode the bearer token
    return decoded
            
def parse_rvt(html: str) -> str:
    soup = BeautifulSoup(html, features="html.parser")
    rvt = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')  # Acquire the Request Verification Token
    return quote(rvt)

def create_body(username: str, password: str, rvt: str) -> str:
    body = ApiInfo.BODY.format(name=quote(username), password=quote(password), rvt=rvt)
    return body

def create_twofa_body(twofa_code: str, rvt: str) -> str:
    body = ApiInfo.TWOFA_BODY.format(twofa_code=twofa_code, rvt=rvt)
    return body

def prompt_2fa() -> str:
    twofa_code = ""
    while True:
        twofa_code = input(debug_text("Authenticator code: "))
        if not twofa_code: raise TwoFactorAuthenticatorCancelled
        if len(twofa_code) >= 6 and len(twofa_code) <= 7:
            return twofa_code
        print(debug_text("The Authenticator code must be at least 6 and at max 7 characters long."))

def debug_text(text: str) -> str:
    signature = "RecNetLogin – "
    return signature + text