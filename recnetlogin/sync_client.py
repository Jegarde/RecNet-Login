import requests
import time
from .api_info import ApiInfo
from .base_client import BaseClient
from .helpers import *

class RecNetLogin(BaseClient):
    def __init__(
        self, 
        username: str, 
        password: str,
        session: requests.Session = None
    ) -> None:
        BaseClient.__init__(self, username, password)
        # HTTP session
        self.__session = session if isinstance(session, requests.Session) else requests.Session()
       
    def __login(self) -> None:
        resp = self.__session.get(ApiInfo.URL)
        html = resp.content
        rvt = parse_rvt(html=html)
                
        body = create_body(username=self.username, password=self.password, rvt=rvt)
            
        resp = self.__session.post(ApiInfo.URL + ApiInfo.PARAMS, headers=ApiInfo.HEADERS, data=body, allow_redirects=True)
        self.bearer_token = parse_token(resp.url)
        self.decoded = decode_token(self.bearer_token)

    def __renew_token(func):
        def wrapper(self, *args, **kwargs) -> func:        
            if not self.bearer_token or not self.decoded or int(time.time()) >= self.decoded['exp']:
                self.__login()
            return func(self, *args, **kwargs)
        return wrapper

    @__renew_token
    def get_token(self, include_bearer: bool = False) -> str:
        token = self.bearer_token
        if include_bearer: token = "Bearer " + token
        return token

    @__renew_token
    def get_decoded_token(self) -> dict:
        return self.decoded