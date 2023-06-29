from recnetlogin import RecNetLogin

"""
Barebones example on how to use RecNetLogin.

Make sure you have RN_COOKIE in your system environment variables or locally in a .env.secret file.
For more information, read the README https://github.com/Jegarde/RecNet-Login/
"""

rnl = RecNetLogin()
token = rnl.get_token()
decoded_token = rnl.get_decoded_token()
print(token, decoded_token)