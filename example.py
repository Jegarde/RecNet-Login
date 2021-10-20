from recnetlogin import login_to_recnet

username = ""
password = ""

login = login_to_recnet(username, password)

print("Success:", login.success)  # If login was successful
print()
print("Access token:", login.access_token)  # Access token / Bearer token
print("Access token expiration:", login.access_expiration)  # Its expiration Unix timestamp
print("Access token decoded:", login.decoded_access_token)  # Decoded
print()
print("Id token:", login.id_token)  # Id token
print("Id token expiration:", login.id_expiration)  # Its expiration Unix timestamp
print("Id token decoded:", login.decoded_id_token)  # Decoded
print()
print("Data:", login.data)  # Account data from /account/me
