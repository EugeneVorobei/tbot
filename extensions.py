import requests
import json
from keys import keys
from access_key import access_key


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту{base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество{amount}')

        # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        # total_base = json.loads(r.content)[keys[base]] * amount

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&symbols={quote}')
        total_quote = json.loads(r.content)['rates'][quote]
        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&symbols={base}')
        total_based = json.loads(r.content)['rates'][base]
        total_base = amount / total_quote * total_based

        return total_base
