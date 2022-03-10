class BaseClient():
    def __init__(
        self, 
        username: str, 
        password: str
    ) -> None:
        # RecNet credentials
        self.username, self.password = username, password
        # HTTP session
        self.session = None
        # The bearer token
        self.bearer_token = ""
        # Decoded bearer token
        self.decoded = {}