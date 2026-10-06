import re
email = input("Enter your email address: ").strip()

"""
^ = start
$ = end
.+ = one or more characters
[^] = characters you want to exclude
[] = set of characters ([a-zA-Z0-9_])
{} = requires at least one character
\\w = any word character
\\d = decimal digit
\\D not a decimal digit
\\s whitespace character
\\S not a whitespace character
? = optional
"""

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")