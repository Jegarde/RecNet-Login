# RecNet-Login
This is a Python package, that allows you to acquire your [RecNet](https://rec.net/) bearer token and more with your account credentials!

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
