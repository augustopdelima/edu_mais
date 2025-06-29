from model.formulario import Formulario


class Resposta:
    def __init__(self, id: int, formulario: Formulario, resposta: str):
        self.id = id
        self.formulario = formulario
        self.reposta = resposta
