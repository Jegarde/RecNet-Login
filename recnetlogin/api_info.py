class ApiInfo():
    URL: str = "https://auth.rec.net/Account/Login"
    PARAMS: str = "?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Drecnet%26redirect_uri%3Dhttps%253A%252F%252Frec.net%252Fauthenticate%252Fdefault%26response_type%3Did_token%2520token%26scope%3Dopenid%2520rn.api%2520rn.notify%2520rn.match.read%2520rn.chat%2520rn.accounts%2520rn.auth%2520rn.link%2520rn.clubs%2520rn.rooms%26state%3Da01a9f406219471ebfa9602eb3abfa97%26nonce%3D99a86479c2f54ec5af90152184d2049c"
    BODY: str = "Input.Username={name}&Input.Password={password}&Input.RememberMe=true&button=login&__RequestVerificationToken={rvt}"
    HEADERS: dict = {"Content-Type": "application/x-www-form-urlencoded"}