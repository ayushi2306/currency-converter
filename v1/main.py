popular_exchange = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "INR": "Indian Rupee",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "AED": "United Arab Emirates Dirham"
}
for keys,values in popular_exchange.items():
    print(f"{keys}: {values}")
    # Exchange rate matrix structure: exchange_rates[FROM_CURRENCY][TO_CURRENCY]
exchange_rates = {
    "USD": {
        "USD": 1.0,
        "EUR": 0.88,    # 1 USD = 0.88 EUR
        "GBP": 0.74,    # 1 USD = 0.74 GBP
        "JPY": 162.80,  # 1 USD = 162.80 JPY
        "INR": 94.95    # 1 USD = 94.95 INR
    },
    "EUR": {
        "USD": 1.14,    # 1 EUR = 1.14 USD
        "EUR": 1.0,
        "GBP": 0.84,    # 1 EUR = 0.84 GBP
        "JPY": 185.00,  # 1 EUR = 185.00 JPY
        "INR": 107.90   # 1 EUR = 107.90 INR
    },
    "GBP": {
        "USD": 1.35,    # 1 GBP = 1.35 USD
        "EUR": 1.19,    # 1 GBP = 1.19 EUR
        "GBP": 1.0,
        "JPY": 220.00,  # 1 GBP = 220.00 JPY
        "INR": 128.30   # 1 GBP = 128.30 INR
    },
    "JPY": {
        "USD": 0.0061,  # 1 JPY = 0.0061 USD
        "EUR": 0.0054,  # 1 JPY = 0.0054 EUR
        "GBP": 0.0045,  # 1 JPY = 0.0045 GBP
        "JPY": 1.0,
        "INR": 0.58     # 1 JPY = 0.58 INR
    },
    "INR": {
        "USD": 0.0105,  # 1 INR = 0.0105 USD
        "EUR": 0.0093,  # 1 INR = 0.0093 EUR
        "GBP": 0.0078,  # 1 INR = 0.0078 GBP
        "JPY": 1.72,    # 1 INR = 1.72 JPY
        "INR": 1.0
    }
}

# taking the amount as input 
print("Enter the amount you wanna convert:")
amount=float(input())
#taking the source currency
print("Enter the source currency:")
source_currency=input()
#taking the destination currency
print("Enter the destination currency:")
destination_currency=input()

USD_amount = amount*exchange_rates[source_currency]["USD"]
final_amount=USD_amount*exchange_rates["USD"][destination_currency]
print(final_amount)
