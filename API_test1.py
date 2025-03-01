import requests
import json
import datetime

# 2 parameters (?)
# base_currency, if second is None, then loop through target currencies, if second is something else, get that currency?? 

'''
def api_response():
'''

def select_target_currencies(base_currency, target_currencies_in, response):
    res = {}
    for currency in target_currencies_in:
        current_rate = response.get(base_currency).get(currency)
        current_rate = round(current_rate, 3) 
        res[currency] = current_rate
    return res
        
def query_api(base_currency_in, target_currencies_in): 
    query = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base_currency_in}.json"
    all_currencies_response = requests.get(query)
    # Get data
    data = all_currencies_response.json()
    if all_currencies_response.status_code != 200:
        print(f"Non 200 code")
        exit(2)
    exchange_rates = {}
    exchange_rates["Date_from_API"] = data.get("date")
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d-%H:%M")
    exchange_rates["Current_Time"] = formatted_time
    exchange_rates.update(select_target_currencies(base_currency_in, target_currencies_in, data))
    print(f"{exchange_rates}")
    return exchange_rates
    

def main():
    
    target_currencies = [
        "gbp",
        "eur",
        "usd",
        "jpy",
        "inr",
        "rub",
        "hkd"
    ]
        
    result = query_api("gbp", target_currencies)
    print(result)
    return result

if __name__ == '__main__':
    main()