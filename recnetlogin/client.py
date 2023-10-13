import httpx
import os
import jwt
import datetime
from typing import Optional
from urllib.parse import urlparse, parse_qs
from dotenv import dotenv_values
from .exceptions import *

class RecNetLogin:
    def __init__(self, env_path: str = None):
        """RecNetLogin, used for getting your RecNet bearer token with ease.

        Args:
            env_path (str, optional): Path to an .env.secret file if you stored your cookie there. Defaults to None.

        Attrs:
            client (httpx.Client): HTTPX client used to fetch the token. Can be reused.

        Raises:
            CookieMissing: Raises when the cookie cannot be found from either a .env.secret file or your system variables.
        """

        # Prioritize local .env.secret files
        env = dotenv_values(env_path if env_path else ".env.secret")

        # Gotten from .env.secret or system variables?
        self.is_local: bool = False

        # Get identity cookie
        if "RN_COOKIE" in env:
            cookie = env["RN_COOKIE"]
            self.is_local = True
        else:
            # If no local .env.secret file, look for globals
            if "RN_COOKIE" in os.environ:
                cookie = os.getenv("RN_COOKIE")
            else:
                raise CookieMissing

        # Initialize attributes
        self.__cookie: dict = {".AspNetCore.Identity.Application": cookie}
        self.client: httpx.Client = httpx.Client(cookies=self.__cookie)

        # Fetch tokens
        self.__token: str = ""
        self.decoded_token: dict = {}

        self.get_token()
        self.get_decoded_token()

        # Update client headers
        self.client.headers = {
            "Authorization": f"Bearer {self.__token}" 
        }

    def get_decoded_token(self) -> Optional[dict]:
        """Returns a decoded bearer token

        Returns:
            Optional[dict]: A decoded token if one exists
        """
        return self.decoded_token

    def get_token(self, include_bearer: bool = False) -> str:
        """Returns and automatically renews your bearer token.

        Args:
            include_bearer (bool, optional): Whether to include the Bearer prefix to the token. Defaults to False.

        Raises:
            InvalidLocalCookie: Raises if your .env.secret cookie is invalid or has expired.
            InvalidSystemCookie: Raises if your system variable cookie is invalid or has expired.

        Returns:
            str: A bearer token.
        """

        # Check if the token has at least 15 minutes of lifetime left
        if int((datetime.datetime.now() + datetime.timedelta(minutes=15)).timestamp()) > self.decoded_token.get("exp", 0):
            # Less than 15 minutes, renew the token

            # Get with cookie
            auth_url = "https://auth.rec.net/connect/authorize?client_id=recnet&redirect_uri=https%3A%2F%2Frec.net%2Fauthenticate%2Fsilent&response_type=id_token%20token&scope=openid%20rn.api%20rn.notify%20rn.match.read%20rn.chat%20rn.accounts%20rn.auth%20rn.link%20rn.clubs%20rn.rooms&state=3b0bbf22ce1c40e7966dc6dd0f2df854&nonce=1ec7e44b909c416bbffae6b5e00ccb38&prompt=none"
            r = self.client.get(auth_url, follow_redirects=True)

            # Acquire token from url
            parsed_url = urlparse(str(r.url))

            try:
                self.__token = parse_qs(parsed_url.fragment)['access_token'][0]  # Acquire the bearer token from the URL
            except KeyError:
                # The cookie has expired or is invalid
                raise InvalidLocalCookie if self.is_local else InvalidSystemCookie

            # Decode it for later
            self.decoded_token = self.__decode_token(self.__token)

        return f"Bearer {self.__token}" if include_bearer else self.__token
    
    def close(self) -> None:
        """Closes the HTTPX client."""
        self.client.close()

    def __decode_token(self, token: str) -> dict:
        """Decodes bearer tokens

        Args:
            token (str): A bearer token

        Returns:
            dict: Decoded bearer token
        """
        
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded


if __name__ == "__main__":
    rnl = RecNetLogin()

    r = httpx.get(
        url="https://accounts.rec.net/account/me", 
        headers={
            # Always run the "get_token" method when using your token!
            # RecNetLogin will automatically renew the token if it has expired.
            "Authorization": rnl.get_token(include_bearer=True)  
        }
    )

    for key, value in r.json().items():
        print(f"{key} = {value}")

    rnl.close()
