import aiohttp
import time
from .api_info import ApiInfo
from .base_client import BaseClient
from .helpers import *

class RecNetLoginAsync(BaseClient):
    def __init__(
        self, 
        username: str, 
        password: str,
        session: aiohttp.ClientSession = None
    ) -> None:
        BaseClient.__init__(self, username, password)
        # HTTP session
        self.__session = session if isinstance(session, aiohttp.ClientSession) else aiohttp.ClientSession(headers=ApiInfo.HEADERS)
       
    async def __login(self) -> None:
        async with self.__session as session:
            async with session.get(ApiInfo.URL) as resp:
                html = await resp.text()
                rvt = parse_rvt(html=html)
                
            # Body with the account details
            body = create_body(username=self.username, password=self.password, rvt=rvt)
            
            async with session.post(ApiInfo.URL + ApiInfo.PARAMS, data=body, allow_redirects=True) as resp:
                self.bearer_token = parse_token(str(resp.real_url))
                self.decoded = decode_token(self.bearer_token)

    def __renew_token(func):
        async def wrapper(self, *args, **kwargs) -> func:        
            if not self.bearer_token or not self.decoded or int(time.time()) >= self.decoded['exp']:
                await self.__login()
            return await func(self, *args, **kwargs)
        return wrapper

    @__renew_token
    async def get_token(self, include_bearer: bool = False) -> str:
        token = self.bearer_token
        if include_bearer: token = "Bearer " + token
        return token

    @__renew_token
    async def get_decoded_token(self) -> dict:
        return self.decoded