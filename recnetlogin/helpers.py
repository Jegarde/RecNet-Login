import jwt
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from .api_info import ApiInfo
from .exceptions import TwoFactorAuthenticatorEnabled, InvalidAccountCredentials
            
def parse_token(url: str) -> tuple:
    redirect_url = str(url).replace("#", "?")  # Patch the URL
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
    return rvt

def create_body(username: str, password: str, rvt: str) -> str:
    body = ApiInfo.BODY.format(name=username, password=password, rvt=rvt)
    return body