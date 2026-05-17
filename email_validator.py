def validate_email(email):
    if "@" in email and "." in email:
        return "Valid Email"
    else:
        return "Invalid Email"

# User input
email = input("Enter your email: ")

# Function call
result = validate_email(email)

# Output
print(result)