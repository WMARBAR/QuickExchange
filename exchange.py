import requests

class ExchangeRateConverter:
    API_URL = "https://api.exchangerate-api.com/v4/latest/"

    def __init__(self):
        self.rates_cache = {}

    def get_exchange_rates(self, base_currency):
        """Obtiene las tasas de cambio desde la API para una moneda base"""
        if base_currency not in self.rates_cache:
            try:
                response = requests.get(f"{self.API_URL}{base_currency}")
                response.raise_for_status()
                self.rates_cache[base_currency] = response.json().get("rates", {})
            except requests.exceptions.RequestException as e:
                print(f"Error al obtener tasas de cambio: {e}")
                return {}
        return self.rates_cache[base_currency]

    def convert_currency(self, amount, from_currency, to_currency):
        """Convierte el monto ingresado de una moneda a otra"""
        try:
            amount = float(amount)
            rates = self.get_exchange_rates(from_currency)
            rate = rates.get(to_currency)

            if rate:
                return round(amount * rate, 2)
            else:
                return "Error: Moneda no disponible"
        except ValueError:
            return "Error: Entrada no válida"
