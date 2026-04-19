"""
Username Validator
Rules:
  - Length: 3 to 20 characters
  - Allowed: letters (a-z, A-Z), digits (0-9), underscore (_)
  - No spaces allowed
"""

import re

MIN_LENGTH = 3
MAX_LENGTH = 20


def validate_username(username: str) -> tuple[bool, list[str]]:
    """
    Validates a username based on defined rules.
    Returns (is_valid: bool, errors: list[str])
    """
    errors = []

    # Rule 1: No spaces
    if " " in username:
        errors.append("❌ Spaces are not allowed.")

    # Rule 2: Length check
    if len(username) < MIN_LENGTH:
        errors.append(f"❌ Too short. Minimum {MIN_LENGTH} characters required (got {len(username)}).")
    elif len(username) > MAX_LENGTH:
        errors.append(f"❌ Too long. Maximum {MAX_LENGTH} characters allowed (got {len(username)}).")

    # Rule 3: Allowed characters only
    if not re.fullmatch(r"[a-zA-Z0-9_]+", username):
        errors.append("❌ Only letters, digits, and underscores (_) are allowed.")

    is_valid = len(errors) == 0
    return is_valid, errors


def main():
    print("=" * 40)
    print("      USERNAME VALIDATOR")
    print("=" * 40)
    print(f"Rules: {MIN_LENGTH}–{MAX_LENGTH} chars | Letters, digits, underscore only | No spaces")
    print("Type 'quit' to exit.\n")

    while True:
        username = input("Enter username: ").strip()

        if username.lower() == "quit":
            print("Goodbye!")
            break

        if username == "":
            print("⚠️  Please enter a username.\n")
            continue

        is_valid, errors = validate_username(username)

        if is_valid:
            print(f"✅ '{username}' is a valid username!\n")
        else:
            print(f"Invalid username '{username}':")
            for error in errors:
                print(f"  {error}")
            print()


if __name__ == "__main__":
    main()
