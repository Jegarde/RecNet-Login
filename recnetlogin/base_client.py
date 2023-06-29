import aiohttp
import httpx

class BaseClient():
    def __init__(
        self, 
        username: str, 
        password: str,
        prompt_2fa: bool = False,
        given_2fa: str = "",
        session: aiohttp.ClientSession or httpx.Client = None,
        **kwargs
    ) -> None:
        # RecNet credentials
        self.username, self.password = username, password
        # HTTP session
        self.session = session
        # The bearer token
        self.bearer_token = ""
        # Decoded bearer token
        self.decoded = {}
        # Whether or not to prompt for 2fa code
        self.prompt_2fa = prompt_2fa
        # 2FA token
        self.given_2fa = given_2fa