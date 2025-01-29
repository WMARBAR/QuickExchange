import customtkinter as ctk
from exchange import ExchangeRateConverter

# Configurar la ventana principal
class CurrencyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CambioXpress")
        self.geometry("400x300")
        
        # Inicializar el convertidor de moneda
        self.converter = ExchangeRateConverter()
        
        # Etiqueta y entrada para ingresar cantidad en Pesos Colombianos
        self.entry_label = ctk.CTkLabel(self, text="Ingrese cantidad en COP:")
        self.entry_label.pack(pady=5)
        
        self.entry = ctk.CTkEntry(self, width=150)
        self.entry.pack(pady=5)
        
        # Menú desplegable para seleccionar la moneda de destino
        self.currencies = {"Euros (EUR)": "EUR", "Dólares (USD)": "USD"}
        self.currency_var = ctk.StringVar(value="EUR")
        self.currency_menu = ctk.CTkOptionMenu(self, values=list(self.currencies.keys()), command=self.update_currency)
        self.currency_menu.pack(pady=5)
        
        # Botón para procesar
        self.process_button = ctk.CTkButton(self, text="Procesar", command=self.process_input)
        self.process_button.pack(pady=10)
        
        # Etiqueta para mostrar el resultado debajo
        self.result_label = ctk.CTkLabel(self, text="Resultado: ")
        self.result_label.pack(pady=10)
    
    def update_currency(self, choice):
        """Actualiza la moneda seleccionada"""
        self.currency_var.set(self.currencies[choice])
    
    def process_input(self):
        """Convierte la cantidad ingresada de COP a la moneda seleccionada y muestra el resultado"""
        user_input = self.entry.get()
        selected_currency = self.currency_var.get()
        converted_amount = self.converter.convert_currency(user_input, selected_currency)
        self.result_label.configure(text=f"Resultado: {converted_amount} {selected_currency}")

