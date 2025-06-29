from typing import List, Optional
from model.aluno import Aluno
from repository.aluno_repository import AlunoRepository


class AlunoService:
    def __init__(self, aluno_repository: AlunoRepository):
        self.aluno_repository = aluno_repository

    def cadastrar_aluno(self, nome: str, email: str, senha: str, matricula: str) -> Aluno:
        print(f"Cadastrando aluno: {nome}, {email}, {matricula}")
        # Retornando objeto dummy
        return Aluno(1, nome, email, senha, matricula)

    def atualizar_aluno(self, id: int, nome: str, email: str, senha: str, matricula: str) -> Optional[Aluno]:
        print(
            f"Atualizando aluno ID {id} com: {nome}, {email}, {senha} ,{matricula}")
        return None

    def listar_alunos(self) -> List[Aluno]:
        print("Listando alunos no serviço")
        return []

    def buscar_aluno_por_id(self, id: int) -> Optional[Aluno]:
        print(f"Buscando aluno por ID {id} no serviço")
        return None

    def remover_aluno(self, id: int) -> None:
        print(f"Removendo aluno ID {id} no serviço")
