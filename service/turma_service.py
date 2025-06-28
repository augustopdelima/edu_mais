from typing import List, Optional
from model.turma import Turma
from repository.turma_repository import TurmaRepository
from model.disciplina import Disciplina
from model.aluno import Aluno


class TurmaService:
    def __init__(self, turma_repository: TurmaRepository):
        print("[Serviço] Inicializando TurmaService")
        self.turma_repository = turma_repository

    def cadastrar_turma(
        self,
        nome: str,
        ano: int,
        semestre: int,
        disciplina: Disciplina,
        alunos: List[Aluno] = None
    ) -> Turma:
        print("[Serviço] Cadastrando turma")
        novo_id = len(self.turma_repository.listar_todos()) + 1
        turma = Turma(novo_id, nome, ano, semestre, disciplina, alunos)
        self.turma_repository.salvar(turma)
        return turma

    def listar_turmas(self) -> List[Turma]:
        print("[Serviço] Listando turmas")
        return self.turma_repository.listar_todos()

    def buscar_turma_por_id(self, id: int) -> Optional[Turma]:
        print(f"[Serviço] Buscando turma por ID {id}")
        return self.turma_repository.buscar_por_id(id)
