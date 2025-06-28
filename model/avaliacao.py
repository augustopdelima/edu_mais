from model.aluno import Aluno
from model.professor import Professor
from model.formulario import Formulario
from model.resposta import Resposta
from typing import List


class Avaliacao:
    def __init__(
        self,
        id: int,
        aluno: Aluno,
        formulario: Formulario,
        professor_avaliado: Professor,
        respostas: List[Resposta]
    ):
        self.id = id
        self.aluno = aluno
        self.formulario = formulario
        self.professor_avaliado = professor_avaliado
        self.respostas = respostas
