# Currency converter program with INR as base currency

# Conversion rates (with INR as the base currency)
conversion_rates = {
    "INR": 1.0,  # Base currency
    "USD": 1 / 82.70,  # 1 INR = 1/82.70 USD
    "EUR": 1 / 88.70,  # Example conversion rate, you can update it
    "GBP": 1 / 101.20,
    "AUD": 1 / 56.40,
    "JPY": 1 / 0.57
}

def display_currencies():
    print("Available currencies:")
    for currency in conversion_rates.keys():
        print(currency)

def convert_currency(amount, from_currency, to_currency):
    # Convert from INR first (as base), then to the target currency
    amount_in_inr = amount * conversion_rates[from_currency]
    converted_amount = amount_in_inr * conversion_rates[to_currency]
    return converted_amount

# Program starts here
print("Welcome to the Currency Converter!")
display_currencies()

# User input
from_currency = input("Enter the currency you have (e.g., USD, EUR, GBP, AUD, JPY): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., INR, USD, EUR): ").upper()
amount = float(input(f"Enter the amount in {from_currency}: "))

if from_currency in conversion_rates and to_currency in conversion_rates:
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
else:
    print("Invalid currency code. Please check and try again.")
 
