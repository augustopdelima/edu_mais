from model.professor import Professor


class Disciplina:
    def __init__(self, id: int, nome: str, semestre: str, descricao: str, professor: Professor):
        self.id = id
        self.nome = nome
        self.semestre = semestre
        self.descricao = descricao
        self.professor = professor
