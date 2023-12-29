def convert_PoundsToDollars(pounds):
    USD = round(pounds*1.31, 2)
    return USD

Pounds = input("enter pounds here: ")
usd = convert_PoundsToDollars(float(Pounds))
print(f"\noutput: {usd} dollars")