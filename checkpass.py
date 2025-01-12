def check_length(password):  # Checks if the password has a minimum length of 8 characters
    if len(password) < 8:
        print("Your password should have at least 8 characters.")
        return "F"
    return "T"

def check_uppercase(password):  # Checks if the password contains at least one uppercase character
    if password.islower():
        print("Your password should include at least one uppercase character.")
        return "F"
    return "T"

def check_lowercase(password):  # Checks if the password contains at least one lowercase character
    if password.isupper():
        print("Your password should include at least one lowercase character.")
        return "F"
    return "T"

def check_isalnum(password):  # Checks if the password has both letters and digits
    if password.isalnum():
        print("Your password should include both letters and numbers.")
        return "F"
    return "T"

def check_special_case(password):  # Checks if the password contains special characters
    if not password.isalnum():
        return "T"
    print("Your password should include at least one special character.")
    return "F"

def check_password(password):  # Checks all conditions to validate the password
    if (check_length(password) == "T" and
        check_lowercase(password) == "T" and
        check_uppercase(password) == "T" and
        check_isalnum(password) == "T" and
        check_special_case(password) == "T"):
        return "T"
    return "F"

def main():
    password = input("Please enter a password: ")
    if check_password(password) == "F":
        print("Your password isn't strong enough.")
    else:
        print("Password submitted successfully.")

main()
