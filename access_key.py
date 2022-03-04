access_key = 'e32496a631cec655d3a1fb47547d9006'
# import requests
# import json
#
# quote = 'EUR'
# base = 'RUB'
# amount = 10
#
# r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&symbols={quote}')
# total_quote = json.loads(r.content)[keys[rates]][quote]
# r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&symbols={base}')
# total_base = json.loads(r.content)['rates'][base]
# total_amount = amount / total_quote * total_base
# print(total_quote)
# print(total_base)
# print(total_amount)