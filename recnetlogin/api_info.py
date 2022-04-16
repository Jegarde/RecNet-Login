class ApiInfo():
    URL: str = "https://auth.rec.net/Account/Login"
    TWOFA_URL: str = "https://auth.rec.net/Account/LoginWith2fa"
    BODY: str = "Input.Username={name}&Input.Password={password}&Input.RememberMe=true&button=login&__RequestVerificationToken={rvt}"
    TWOFA_BODY: str = "RememberMe=True&Input.TwoFactorCode={twofa_code}&__RequestVerificationToken={rvt}&Input.RememberMachine=true"
    PARAMS: str = "?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Drecnet%26redirect_uri%3Dhttps%253A%252F%252Frec.net%252Fauthenticate%252Fdefault%26response_type%3Did_token%2520token%26scope%3Dopenid%2520rn.api%2520rn.notify%2520rn.match.read%2520rn.chat%2520rn.accounts%2520rn.auth%2520rn.link%2520rn.clubs%2520rn.rooms%26state%3Da01a9f406219471ebfa9602eb3abfa97%26nonce%3D99a86479c2f54ec5af90152184d2049c"
    TWOFA_PARAMS: str = "?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Drecnet%26redirect_uri%3Dhttps%253A%252F%252Frec.net%252Fauthenticate%252Fdefault%26response_type%3Did_token%2520token%26scope%3Dopenid%2520rn.api%2520rn.notify%2520rn.match.read%2520rn.chat%2520rn.accounts%2520rn.auth%2520rn.link%2520rn.clubs%2520rn.rooms%26state%3D0b156b90d78249cd95cc54ed965cf705%26nonce%3D3a64f6e9e3324f3ca10dd0ad57fd83f0&RememberMe=True"
    HEADERS: dict = {"Content-Type": "application/x-www-form-urlencoded", "Connection": "keep-alive"}