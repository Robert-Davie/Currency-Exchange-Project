'''
Title: API_test.py
Desc: This is just a test!!
'''

import requests
import json
import datetime

print("Start of API Script")

'''
currency_codes_json = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json")
print(f"Result 1: {result_1.json()}")
'''


currency_value_API = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/gbp.json"
all_currencies_response = requests.get(currency_value_API)

if all_currencies_response.status_code != 200:
    print(f"Non 200 code")
    exit(2)

'''
Printing all currency values.
'''
if all_currencies_response.status_code == 200:
    data = all_currencies_response.json()
    pretty_json = json.dumps(data, indent=2, sort_keys=True)  # Pretty print with indentation
    print("Currency Data (Prettified):\n", pretty_json)
else:
    print("Error fetching data from API.")

'''
Printing specific currency value from JSON result.
'''
target_currency = "gbp"
# if all_currencies_response.status_code == 200:
#     data = all_currencies_response.json()
#     # 2 layers
#     target_value = data.get("eur").get(target_currency)
    
#     if target_value is not None:
#         print(f"Value of {target_currency}: {target_value}")
#     else:
#         print(f"Key {target_currency} not found in JSON.")
# else:
#     print("Error fetching data from API.")

target_currencies = [
    "gbp", 
    "eur",
    "usd",
    "jpy",
    "inr",
    "rub"
    
]

exchange_rates = {}

exchange_rates["Date_from_API"] = data.get("date")
now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d-%H:%M")
exchange_rates["Current_Time"] = formatted_time

for currency in target_currencies:
    current_rate = data.get("gbp").get(currency)
    current_rate = round(current_rate, 3) 
    exchange_rates[currency] = current_rate
    #print(f"Currency: {currency} Current Rate: {current_rate}")
print(exchange_rates)


   



