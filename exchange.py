import requests

class ExchangeRateConverter:
    API_URL = "https://api.exchangerate-api.com/v4/latest/COP"  # COP como moneda base

    def __init__(self):
        self.rates = self.get_exchange_rates()
    
    def get_exchange_rates(self):
        """Obtiene las tasas de cambio desde la API"""
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            return response.json().get("rates", {})
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener tasas de cambio: {e}")
            return {}

    def convert_currency(self, amount, to_currency):
        """Convierte el monto ingresado a la moneda seleccionada"""
        try:
            amount = float(amount)
            rate = self.rates.get(to_currency, None)
            if rate:
                return round(amount * rate, 2)
            else:
                return "Error: Moneda no disponible"
        except ValueError:
            return "Error: Entrada no válida"
