# username_validator.py

def validate_username(username):
    username = username.strip().lower().replace(" ", "_")

    if len(username) > 5 and username.replace("_", "").isalnum():
        return True, username
    else:
        return False, username


user = input("Enter username: ")

valid, formatted_username = validate_username(user)

if valid:
    print("✅ Valid username:", formatted_username)
else:
    print("❌ Invalid username")