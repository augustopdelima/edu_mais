from model.disciplina import Disciplina
from model.aluno import Aluno
from typing import List


class Turma:
    def __init__(
        self,
        id: int,
        nome: str,
        ano: int,
        semestre: int,
        disciplina: Disciplina,
        alunos: List[Aluno] = None
    ):
        self.id = id
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.disciplina = disciplina
        self.alunos = alunos or []
