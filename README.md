# RecNet-Login
This is a Python module, that allows you to acquire your RecNet authorization bearer token with your account credentials!

# Getting started
A simple example on how the module is used.
```py
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
The function returns the following data if the login was SUCCESSFUL;
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
