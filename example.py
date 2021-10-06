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
name = login['account_data']['displayName']
acc_data = login['account_data']
b_token = login['bearer_token']
account_details = ""
for key in acc_data:  # Display the details nicely formatted
    account_details += f"{key}: {acc_data[key]}\n"

# Save details
file_name = "token_details.txt"
with open(file_name, "w") as txt:
    txt.write(f"Hello, {name}!\n\n{b_token}\n\n{account_details}")
os.startfile(file_name)  # Open the text file
sys.exit("Successful!")  # Close
