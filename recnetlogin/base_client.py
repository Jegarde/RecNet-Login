import aiohttp
import requests

class BaseClient():
    def __init__(
        self, 
        username: str, 
        password: str,
        prompt_2fa: bool = False,
        session: aiohttp.ClientSession | requests.Session = None,
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