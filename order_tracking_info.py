import random
import textwrap

class OrderTrackingInfo:
    def __init__(self):
        self.responses = [
            "Para seguir tu pedido, inicia sesión en tu cuenta y ve a la sección 'Mis pedidos'. Allí podrás ver el estado actual del envío.",
            "Puedes consultar el seguimiento del pedido desde el correo de confirmación que te enviamos. Incluye un enlace con la información del transporte.",
            "El seguimiento de tu pedido está disponible en tu perfil. Si ya fue enviado, verás el número de seguimiento y el transportista asignado."
        ]

    def get_response(self):
        texto_formateado = textwrap.fill(random.choice(self.responses), width=80)
        print(texto_formateado)