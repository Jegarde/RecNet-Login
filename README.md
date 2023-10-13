# RecNet-Login 2
This is a Python package that allows you to acquire your [RecNet](https://rec.net/) bearer token and more with your cookie! 🍪

This is a rewritten version. Previous versions do not work anymore.

# Features
- No more account credentials!
- Automatically renewing token
- Supports 2FA accounts
- Decoding the bearer token
- Detailed exceptions

# Installation
Download the recnetlogin folder and place it in your project.

pip installation once this is stable.

# Setup
### Gathering your ASP.NET Core Identity
1. Login to [RecNet](https://rec.net/). While logging in, make sure you toggle on "Remember me / my machine".
2. Open your browser's DevTools (Inspect Element)
3. Open the `Storage` or `Application` tab on the top
4. Locate `Cookies` > `https://auth.rec.net` on the directory
5. Search for `.AspNetCore.Identity.Application` by filtering the cookies
6. Double click the value and copy it 
![image](https://github.com/Jegarde/RecNet-Login/assets/13438202/1fa41865-f8e4-43d8-9749-5b8dec070e93)

### Option 1/2: Storing it in your environment variables (Windows)
1. Search for environment variables and open the first result

![image](https://github.com/Jegarde/RecNet-Login/assets/13438202/c35ebeb9-de31-46ba-a264-f02138560321)

2. Click `Environment Variables...`

![image](https://github.com/Jegarde/RecNet-Login/assets/13438202/dd341365-fa90-4145-82aa-94a12f91019a)

3. Click `New` under System Variables

![image](https://github.com/Jegarde/RecNet-Login/assets/13438202/2d098f6f-145c-4232-b9ed-86000622a077)

4. Name the variable `RN_COOKIE` and paste the copied value

![image](https://github.com/Jegarde/RecNet-Login/assets/13438202/1aa8cfe0-a7a2-4237-b19d-9787d49b225b)

5. Press OK on all the opened tabs

6. Restart your computer for it to take effect

### Option 2/2: Storing it in a .env.secret file
1. Make a new file named `.env.secret` in your project's directory
2. Type `RN_COOKIE=` in the file and paste the copied value

![image](https://github.com/Jegarde/RecNet-Login/assets/13438202/f6ffe81c-a810-4651-bbc6-5019bba71a0c)

3. If the file is not in your project's directory, make sure to specify it
```py
rnl = RecNetLogin(env_path="")  # Env path defaults to local directory
```

# Usage

### Getting your token
```py
from RecNetLogin import RecNetLogin

rnl = RecNetLogin()
token = rnl.get_token()
decoded_token = rnl.get_decoded_token()  # JWT decoded
print(token, decoded_token)
```

### Making authorized calls
```py
from recnetlogin import RecNetLogin

rnl = RecNetLogin()

# Fetch using RecNetLogin's HTTPX client
r = rnl.client.get("https://accounts.rec.net/account/me")
for key, value in r.json().items():
    print(key, value)
```
