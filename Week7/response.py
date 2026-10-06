import validators

email = input("What's your email? ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")