import requests
import sys
import json


try:
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        response = (requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")).json()
        usd_rate = response["bpi"]["USD"]["rate_float"]
        price = usd_rate * float(sys.argv[1])
        print(f"${price:,.4f}")
except requests.RequestException:
    pass
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)




