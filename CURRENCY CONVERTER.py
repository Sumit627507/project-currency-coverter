from forex_python.converter import CurrencyRates

def currency_converter():
    c = CurrencyRates()

    print("Currency Converter")
    print("Supported currencies: USD, EUR, INR, GBP, AUD, etc.")

    from_currency = input("Enter the base currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., INR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    currency_converter()
 
