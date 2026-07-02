from api import get_exchange_rates

data = get_exchange_rates("USD")

if data:

    print("Connection Successful!\n")

    print(data["rates"]["INR"])

else:

    print("Unable to fetch exchange rates.")