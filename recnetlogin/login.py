import requests


def login_to_recnet(username, password):
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
    body = f"Input.Username={username}&Input.Password={password}&Input.RememberMe=true&button=login" \
           f"&__RequestVerificationToken={request_verification_token}&Input.RememberMe=false "
    r = session.post(url, headers=headers, data=body, allow_redirects=True)
    url = r.url

    # GATHER AUTHORIZATION TOKEN
    try:
        # Get the token from the url
        token = url.split("access_token=")[1].split("&token_type=")[0]
    except IndexError:
        # Invalid url, faulty login credentials
        return {"success": False, "error": "Invalid login credentials!"}

    # TEST TOKEN
    bearer_token = "Bearer " + token
    r = session.get("https://accounts.rec.net/account/me", headers={"Authorization": bearer_token})
    if not r.ok:
        # Invalid token!
        return {"success": False, "error": "Something went wrong!"}
    acc_data = r.json()

    # SUCCESSFULLY ACQUIRED TOKEN, RETURN
    return {"success": True, "bearer_token": bearer_token, "account_data": acc_data}


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
    if not login['success']:
        # Login failed.
        sys.exit(login['error'])  # Print error

    # Login succeeded, export details
    print(login['account_data'])
    print(login['bearer_token'])
    sys.exit("Successfully logged in!")
