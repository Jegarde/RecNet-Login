import aiohttp
import time
import traceback
from .api_info import ApiInfo
from .base_client import BaseClient
from .helpers import *

class RecNetLoginAsync(BaseClient):
    def __init__(
        self, 
        **kwargs
    ) -> None:
        BaseClient.__init__(self, **kwargs)
        # HTTP session
        self.__session = self.session if isinstance(self.session, aiohttp.ClientSession) else aiohttp.ClientSession(headers=ApiInfo.HEADERS)
       
    async def __login(self) -> None:
        async with self.__session as session:
            async with session.get(ApiInfo.URL) as resp:
                html = await resp.text()
                rvt = parse_rvt(html=html)
                
            # Body with the account details
            body = create_body(username=self.username, password=self.password, rvt=rvt)
            
            async with session.post(ApiInfo.URL + ApiInfo.PARAMS, data=body, allow_redirects=True) as resp:
                try:
                    self.bearer_token = parse_token(resp.url)
                    self.decoded = decode_token(self.bearer_token)
                except TwoFactorAuthenticatorEnabled:
                    if not self.prompt_2fa: raise TwoFactorAuthenticatorProcessDisabled
                    await self.__login_2fa()

    async def __login_2fa(self) -> None:
        twofa_code = prompt_2fa()

        async with self.__session as session:
            async with session.get(ApiInfo.TWOFA_URL) as resp:
                html = await resp.text()
                rvt = parse_rvt(html=html)
                
            body = create_twofa_body(twofa_code=twofa_code, rvt=rvt)

            async with session.post(ApiInfo.TWOFA_URL + ApiInfo.TWOFA_PARAMS, data=body, allow_redirects=True) as resp:
                try:
                    self.bearer_token = parse_token(resp.real_url)
                    self.decoded = decode_token(self.bearer_token)   
                except TwoFactorAuthenticatorEnabled:
                    print(debug_text("Authenticator code is wrong!"))
                    return await self.__login_2fa() 
                except Exception:  # Uncaught exception
                    traceback.print_exc()
                    return

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