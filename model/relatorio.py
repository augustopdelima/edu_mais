from model.formulario import Formulario


class Relatorio:
    def __init__(self, id: int, indicadores: str, graficos: str, formulario: Formulario):
        self.id = id
        self.indicadores = indicadores
        self.graficos = graficos
        self.formulario = formulario
