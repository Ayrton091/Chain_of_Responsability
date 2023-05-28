from abc import ABC, abstractmethod


class Request:
    def __init__(self, amount):
        self.amount = amount


# Interfaz para los manejadores de solicitud
class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    @abstractmethod
    def handle_request(self, request):
        pass


# Primer manejador solo maneja solicitudes con un monto menor o igual a $100
class LowAmountHandler(Handler):
    def handle_request(self, request):
        if request.amount <= 100:
            print("La solicitud de valor", request.amount," ha sido aprobada por el manejador de monto bajo.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


# Segundo manejador solo maneja solicitudes con un monto entre $101 y $500
class MediumAmountHandler(Handler):
    def handle_request(self, request):
        if 101 <= request.amount <= 500:
            print("La solicitud de valor", request.amount," ha sido aprobada por el manejador de monto medio.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


# Tercer manejador solo maneja solicitudes con un monto mayor a $500
class HighAmountHandler(Handler):
    def handle_request(self, request):
        if request.amount > 500:
            print("La solicitud de valor", request.amount," ha sido aprobada por el manejador de monto alto.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


# Creación de la cadena de responsabilidad
low_amount_handler = LowAmountHandler()
medium_amount_handler = MediumAmountHandler()
high_amount_handler = HighAmountHandler()

low_amount_handler.set_next_handler(medium_amount_handler)
medium_amount_handler.set_next_handler(high_amount_handler)


request1 = Request(50)
low_amount_handler.handle_request(request1)

request2 = Request(200)
low_amount_handler.handle_request(request2)

request3 = Request(1000)
low_amount_handler.handle_request(request3)
