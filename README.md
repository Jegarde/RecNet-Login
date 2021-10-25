# RecNet-Login
This is a Python package, that allows you to acquire your [RecNet](https://rec.net/) bearer token and more with your account credentials!

# Installation
Done via [git](https://git-scm.com):
```py
python -m pip install git+https://github.com/Jegarde/RecNet-Login.git#egg=recnetlogin
```

# Getting started
The absolute basics. This is basically all you need to know to get started.
```py
from recnetlogin import login_to_recnet

username = ""
password = ""
login = login_to_recnet(username, password)  # Login with account credentials

print(login.access_token)  # Print out the bearer token
```

# Usage
Logging in to RecNet is very simple with this package.

Begin by importing the package:
```py
from recnetlogin import login_to_recnet
```

Now let's try logging in:
```py
login = login_to_recnet("Coach", "recnet87")  # Let's pretend these are valid credentials
```

We now have a `login_to_recnet` object called `login`. All this information can be gotten from the object:
```py
print("Success:", login.success)  # If login was successful (It should raise an exception if unsuccessful, though)
print()
print("Access token:", login.access_token)  # Access token / Bearer token
print("Access token expiration:", login.access_expiration)  # Its expiration Unix timestamp
print("Access token decoded:", login.access_decoded)  # Decoded
print()
print("Id token:", login.id_token)  # Id token
print("Id token expiration:", login.id_expiration)  # Its expiration Unix timestamp
print("Id token decoded:", login.id_decoded)  # Decoded
print()
print("Data:", login.data)  # Account data from /account/me
```

If the login was unsuccessful, it will raise `InvalidCredentials`.
```py
try:
    login = login_to_recnet("Coach", "recnet87")
    print("Success!")  # Successfully logged in without errors!
except recnetlogin.login.InvalidCredentials:
    print("Unsuccess!")  # Incorrect account credentials.
```

# Attributes
If the login was successful, the following attributes will be available:
- `success` | If login was successful

- `access_token` | Your bearer authorization token
- `access_expiration` | Bearer token's expiration Unix timestamp
- `access_decoded` | Decoded bearer token

- `id_token` | Your id token
- `id_expiration` | Id token's expiration Unix timestamp
- `id_decoded` | Decoded id token

- `data` | Your data from /account/me

# Arguments
You can also directly run the [login.py](https://github.com/Jegarde/RecNet-Login/blob/main/recnetlogin/login.py) file. You can also run it with `username` and `password` arguments. Make sure to run it from the terminal to prevent it from shutting down on finish.
```py
python login.py USERNAME PASSWORD
```
If successful, it will print all possible data.

# Alternative ways of getting your bearer token
- Run this JS script on your browser's DevTools console.
```js
url = window.location.href
if (url.includes("rec.net")) {
   try {
    b_token = "Bearer " + JSON.parse(localStorage.getItem("oidc.user:https://auth.rec.net:recnet"))["access_token"]
    console.log(b_token)
    alert("Successfully printed bearer token on console!")
    }
    catch(err) {
        alert("Not logged in on RecNet!")
    } 
}
else {
    alert("Not in rec.net")
}
```
- Generate from cookie

[Rec Room API Tool Box](https://github.com/zigzatuzoo/Rec-Room-API-Tool-Box/blob/main/Tools/RRAutoAuth.py) made by [zigzatuzoo](https://github.com/zigzatuzoo)
