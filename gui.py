import customtkinter as ctk
from exchange import ExchangeRateConverter


class CurrencyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QuickExchange")
        self.geometry("500x350")
        # Configurar el icono
        self.iconbitmap("static/icoST.ico")  # Reemplaza "icono.ico" con la ruta de tu archivo .ico

        # Cambiar el tema de colores
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="black")  # Fondo negro de la app

        # Inicializar el convertidor de moneda
        self.converter = ExchangeRateConverter()

        # Configuración de las fuentes y colores personalizados
        self.title_font = ("Consolas", 20, "bold")
        self.button_font = ("Consolas", 20, "bold")
        self.entry_font = ("Consolas", 20)  # Fuente personalizada para el campo de entrada
        self.title_color = "#00FF00"  # Verde Matrix
        self.button_bg_color = "#00FF00"
        self.button_text_color = "black"
        self.dropdown_bg_color = "black"
        self.dropdown_arrow_color = "#00FF00"
        self.hover_color = "#D3D3D3"  # Gris claro para el hover

        # Etiqueta para ingresar la cantidad
        self.entry_label = ctk.CTkLabel(
            self, 
            text="Ingrese la cantidad del dinero:", 
            font=self.title_font, 
            text_color=self.title_color
        )
        self.entry_label.pack(pady=5)

        # Entrada y menú desplegable para la moneda de entrada
        entry_frame = ctk.CTkFrame(self, fg_color="black")
        entry_frame.pack(pady=5)

        # Campo de entrada con fuente Consolas
        self.entry = ctk.CTkEntry(entry_frame, width=150, font=self.entry_font)
        self.entry.grid(row=0, column=0, padx=5)

        # Configurar validación de entrada para que solo permita números
        self.entry.bind("<KeyPress>", self.validate_input)

        # Menú desplegable para seleccionar la moneda de entrada
        self.input_currencies = {
                                    "Pesos Colombianos (COP)": "COP",
                                    "Euros (EUR)": "EUR",
                                    "Dólares (USD)": "USD",
                                    "Bolivianos (BOB)": "BOB",
                                    "Soles Peruanos (PEN)": "PEN",
                                    "Reales Brasileños (BRL)": "BRL",
                                    "Pesos Argentinos (ARS)": "ARS",
                                    "Pesos Mexicanos (MXN)": "MXN",
                                    "Pesos Uruguayos (UYU)": "UYU",
                                    "Guaraníes Paraguayos (PYG)": "PYG",
                                    "Pesos Chilenos (CLP)": "CLP",
                                    "Dólares Ecuatorianos (USD)": "USD",  # Ecuador usa el USD
                                    "Bolívares Venezolanos (VES)": "VES"
                                }
        
        self.input_currency_menu = ctk.CTkOptionMenu(
            entry_frame, 
            values=list(self.input_currencies.keys()), 
            font=self.button_font,
            text_color=self.button_text_color,
            fg_color=self.button_bg_color,
            dropdown_fg_color=self.dropdown_bg_color,
            button_color=self.dropdown_arrow_color,
            button_hover_color=self.hover_color
        )
        self.input_currency_menu.grid(row=0, column=1, padx=5)

        # Título para la sección de moneda de cambio
        self.change_label = ctk.CTkLabel(
            self, 
            text="Moneda de cambio", 
            font=self.title_font, 
            text_color=self.title_color
        )
        self.change_label.pack(pady=10)

        # Menú desplegable para seleccionar la moneda de destino
        self.output_currencies = self.input_currencies.copy()
        self.output_currency_menu = ctk.CTkOptionMenu(
            self, 
            values=list(self.output_currencies.keys()), 
            font=self.button_font,
            text_color=self.button_text_color,
            fg_color=self.button_bg_color,
            dropdown_fg_color=self.dropdown_bg_color,
            button_color=self.dropdown_arrow_color,
            button_hover_color=self.hover_color
        )
        self.output_currency_menu.pack(pady=5)

        # Botón para procesar
        self.process_button = ctk.CTkButton(
            self, 
            text="Procesar", 
            command=self.process_input, 
            font=self.button_font, 
            text_color=self.button_text_color,
            fg_color=self.button_bg_color,
            hover_color=self.hover_color
        )
        self.process_button.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.result_label = ctk.CTkLabel(
            self, 
            text="Resultado: ", 
            font=self.title_font, 
            text_color=self.title_color
        )
        self.result_label.pack(pady=10)

    def process_input(self):
        """Convierte la cantidad ingresada a la moneda seleccionada y muestra el resultado"""
        user_input = self.entry.get()
        input_currency = self.input_currencies[self.input_currency_menu.get()]
        output_currency = self.output_currencies[self.output_currency_menu.get()]

        converted_amount = self.converter.convert_currency(user_input, input_currency, output_currency)
        self.result_label.configure(text=f"Resultado: {converted_amount} {output_currency}")

    def validate_input(self, event):
        """Permite solo la entrada de números en el campo de texto, pero deja borrar o editar"""
        valid_keys = ("BackSpace", "Delete", "Left", "Right", "Home", "End", "Tab")  # Teclas permitidas para edición
        if not (event.char.isdigit() or event.char == '.' or event.keysym in valid_keys):
            return "break"  # Bloquea cualquier entrada no válida
