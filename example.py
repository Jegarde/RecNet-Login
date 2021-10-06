import sys
import os
from recnetlogin import login_to_recnet

# Ask for login credentials
print("Enter RecNet account credentials")
username = input("Username > ")
password = input("Password > ")

# Login
login = login_to_recnet(username, password)  # LOGIN FUNCTION FROM MODULE
if not login['success']:  # If the login was successful, this will be true
    # Login failed.
    sys.exit(login['error'])  # Print error included in the returned dictionary

# Login succeeded, export details
file_name = "token_details.txt"
with open(file_name, "w") as txt:
    txt.write(f"Hello, {login['account_data']['displayName']}!\n\n{login['bearer_token']}\n\n{login['account_data']}")
os.startfile(file_name)  # Open the text file
sys.exit("Successful!")
