import re
url = input("Enter URL: ").strip()

username = re.sub(r"^(https?://)?(www\.?)twitter.com/", "", url)
print(f"Username: {username}")