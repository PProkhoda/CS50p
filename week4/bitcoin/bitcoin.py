import requests
import json
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass
o = response.json()
bit = o["bpi"]["USD"]["rate_float"]
amount = float(bit)*n
print(f"${amount:,.4f}")
