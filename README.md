# RecNet-Login
This is a Python module, that allows you to acquire your RecNet authorization bearer token with your account credentials!

# Usage
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
