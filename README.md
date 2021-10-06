# RecNet-Login
This is a Python package, that allows you to acquire your [RecNet](https://rec.net/) bearer token with your account credentials!

# Installation
Done via git:
```py
python -m pip install git+https://github.com/Jegarde/RecNet-Login.git#egg=recnetlogin
```

# Getting started
The absolute basics. This is basically all you need to know to get started.
```py
from recnetlogin import login_to_recnet

login = login_to_recnet("username", "password")

print(login)
```

A simple example on how the module is used. Another example script is found [here](https://github.com/Jegarde/RecNet-Login/blob/main/example.py).
```py
import sys
from recnetlogin import login_to_recnet

# RecNet account credentials
username = ''
password = ''

# Login function from the module
login = login_to_recnet(username, password)

if not login['success']:  # If the login was successful, this will be true
    # Login failed.
    sys.exit(login['error'])  # Print error included in the returned dictionary

# If login succeeded, print the details
bearer_token = login['bearer_token']
account_data = login['account_data']

print("Bearer token:", bearer_token)
print("Account data:", account_data)

```

# Details
The function `login_to_recnet(username, password)` returns the following data if the login was SUCCESSFUL;
```json
{
    "success": true,
    "bearer_token": "Bearer X",
    "account_data": {
       "availableUsernameChanges": 0,
       "email": "coach@email.com",
       "phone": "",
       "birthday":"0000-00-00T00:00:00Z",
       "accountId": 1,
       "username": "Coach",
       "displayName": "Coach",
       "profileImage": "DefaultProfileImage",
       "bannerImage": "",
       "isJunior": false,
       "platforms": 0,
       "createdAt": "0000-00-00T00:00:00.000Z"
    }
}
```
and if it was UNSUCCESSFUL:
```json
{
    "success": false,
    "error": "specified error"
}
```

# Arguments
You can also directly run the [login.py](https://github.com/Jegarde/RecNet-Login/blob/main/recnetlogin/login.py) file. You can also run it with `username` and `password` arguments. Make sure to run it from the terminal to prevent it from shutting down on finish.
```py
python login.py USERNAME PASSWORD
```
If successful, it will print your bearer token and account data.
