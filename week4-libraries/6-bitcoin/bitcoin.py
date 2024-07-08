import requests
import sys

if len(sys.argv) == 2:
    try:
        if float(sys.argv[1]):
            while True:
                try:
                    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
                    bitcoin = float(request["bpi"]["USD"]["rate_float"]) * float(sys.argv[1])
                    print(f"${bitcoin:,.4f}")
                    break
                except requests.RequestException:
                    pass
    except ValueError:
        sys.exit("Command-line argument is not a number")

else:
    sys.exit("Missing command-line argument")
