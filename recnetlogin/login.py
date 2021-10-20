import requests
import jwt


class login_to_recnet():
    def __init__(self, username, password):
        self.self = self

        # Account credentials
        self.username = username  # RR @ username
        self.password = password  # RR password

        self.success = False  # If login is successful

        # Access token / Bearer token
        self.access_token = None  # The bearer token if successful
        self.decoded_access_token = None  # Decoded bearer token if successful
        self.access_expiration = 0  # Unix timestamp for bearer expiration

        # Id token
        self.id_token = None  # Id token if successful
        self.decoded_id_token = None  # Decoded id token if successful
        self.id_expiration = 0  # Unix timestamp for id expiration

        self.data = {}  # Data from account/me if successful

        self.login()  # Login

    def login(self):
        """Login to RecNet"""
        # REQUEST SESSION
        session = requests.Session()

        # GET REQUEST VERIFICATION TOKEN
        r = session.get("https://auth.rec.net/Account/Login")
        login_html = str(r.content)  # Save the HTML from the login page
        # Gather the request verification token from the HTML
        request_verification_token = \
            login_html.split("<input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"")[1].split(
                "\" /><input name=\"Input.RememberMe\"")[0]

        # DO LOGIN REQUEST TO /Account/Login
        url = 'https://auth.rec.net/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Drecnet' \
              '%26redirect_uri%3Dhttps%253A%252F%252Frec.net%252Fauthenticate%252Fdefault%26response_type%3Did_token' \
              '%2520token%26scope%3Dopenid%2520rn.api%2520rn.notify%2520rn.match.read%2520rn.chat%2520rn.accounts%2520rn' \
              '.auth%2520rn.link%2520rn.clubs%2520rn.rooms%26state%3D047dc984ca704c81a7c4492a1c8d9c57%26nonce' \
              '%3Ddd01b66944934130a2cbe4613a3b0236 '
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = f"Input.Username={self.username}&Input.Password={self.password}&Input.RememberMe=true&button=login" \
               f"&__RequestVerificationToken={request_verification_token}&Input.RememberMe=false "

        r = session.post(url, headers=headers, data=body, allow_redirects=True)
        url = r.url

        # GATHER AUTHORIZATION TOKEN
        try:
            # Get the token from the url
            access_token = url.split("access_token=")[1].split("&token_type=")[0]  # Access token
            id_token = url.split("id_token=")[1].split("&access_token=")[0]  # Id token
        except IndexError:
            # Invalid url, faulty login credentials
            self.success = False
            raise InvalidCredentials("Rec Room username or password incorrect!")

        # TEST TOKEN
        bearer_token = "Bearer " + access_token
        r = session.get("https://accounts.rec.net/account/me", headers={"Authorization": bearer_token})
        if not r.ok:
            # Invalid token!
            self.success = False
            raise TokenTestingError("Login was successful, but bearer token didn't pass testing.")
        acc_data = r.json()

        # Decode tokens
        decoded_access = jwt.decode(access_token, options={"verify_signature": False})
        access_expire_unix = decoded_access['exp']
        decoded_id = jwt.decode(id_token, options={"verify_signature": False})
        id_expire_unix = decoded_id['exp']

        # SUCCESSFULLY ACQUIRED TOKEN, RETURN
        self.success = True  # Login successful!
        self.access_token = bearer_token  # Bearer token
        self.id_token = id_token  # Id token
        self.decoded_access_token = decoded_access  # Decoded bearer token
        self.decoded_id_token = decoded_id  # Decoded id token
        self.access_expiration = access_expire_unix  # Unix timestamp for bearer expiration
        self.id_expiration = id_expire_unix  # Unix timestamp for id expiration
        self.data = acc_data
        return


# Errors
class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidCredentials(Error):
    """Raised when RR account credentials aren't valid"""
    pass


class TokenTestingError(Error):
    """Raised when failed to test bearer token"""
    pass


# If ran directly
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:  # If arguments given already
        # python login.py USERNAME PASSWORD
        if len(sys.argv) >= 3:
            username = sys.argv[1]
            password = sys.argv[2]
            print("Attempting to log in to RecNet with the following credentials...")
            print("Username:", username)
            print("Password:", password)
        else:
            sys.exit("Missing arguments! USERNAME, PASSWORD")
    else:
        # Ask for login credentials
        username = input("Username > ")
        password = input("Password > ")

        print("Attempting to log in to RecNet with the credentials...")

    login = login_to_recnet(username, password)
    if not login.success:
        # Login failed.
        sys.exit("Login didn't succeed!")  # Print error

    # Login succeeded, export details
    print("Success:", login.success)
    print()
    print("Access token:", login.access_token)
    print("Access token expiration:", login.access_expiration)
    print("Access token decoded:", login.decoded_access_token)
    print()
    print("Id token:", login.id_token)
    print("Id token expiration:", login.id_expiration)
    print("Id token decoded:", login.decoded_id_token)
    print()
    print("Data:", login.data)
    sys.exit("Successfully logged in!")
