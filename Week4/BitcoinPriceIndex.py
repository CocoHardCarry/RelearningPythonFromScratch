import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=3"

params = {"apiKey": "YOUR_API_KEY"}

try:
    r = requests.get(url, params=params)
    r.raise_for_status()
except requests.RequestException:
    sys.exit("API request failed")

data = r.json()
price = float(data["data"]["priceUsd"])

amount = bitcoins * price

print(f"${amount:,.4f}")
