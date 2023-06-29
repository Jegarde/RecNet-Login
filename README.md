# RecNet-Login
This is a Python package that allows you to acquire your [RecNet](https://rec.net/) bearer token and more with your ASP.NET Core Identity!
This is a rewritten version. Previous versions do not work anymore.

# Features
- Automatically renewing token
- Supports 2FA accounts
- Decoding the bearer token
- Detailed exceptions

# Installation
Done via pip:
```py
pip install -U recnetlogin
```

# Usage
## Gathering your ASP.NET Core Identity
1. Login to [RecNet](https://rec.net/)
2. Open your browser's DevTools (Inspect Element)
3. Open the `Storage` tab on the top
4. Locate `Cookies` on the directory
5. Paste in `.AspNetCore.Identity.Application` to the filter or manually search for it
6. Double click the value and copy it 
![image](https://github.com/Jegarde/RecNet-Login/assets/13438202/1fa41865-f8e4-43d8-9749-5b8dec070e93)

## Storing it in your environment variables (Windows)
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

