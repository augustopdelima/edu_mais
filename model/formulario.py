from model.disciplina import Disciplina
from model.turma import Turma
from model.coordenador import Coordenador
from model.professor import Professor
from model.questao import Questao
from typing import List


class Formulario:
    def __init__(self, id: int, data_aplicacao: str, disciplina: Disciplina,
                 turma: Turma, criado_por: Coordenador,
                 avaliar: Professor, perguntas: List[Questao]):
        self.id = id
        self.data_aplicacao = data_aplicacao
        self.disciplina = disciplina
        self.turma = turma
        self.criado_por = criado_por
        self.avaliar = avaliar
        self.perguntas = perguntas
