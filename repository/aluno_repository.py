
from typing import List, Optional
from model.aluno import Aluno


class AlunoRepository:

    def __init__(self):
        self.alunos = list[Aluno]

    def salvar(self, aluno: Aluno) -> None:
        print(f"Salvando aluno: {aluno.nome}")

    def listar_todos(self) -> List[Aluno]:
        print("Listando todos os alunos")
        return []

    def buscar_por_id(self, id: int) -> Optional[Aluno]:
        print(f"Buscando aluno pelo ID: {id}")
        return None

    def deletar(self, id: int) -> None:
        print(f"Deletando aluno com ID: {id}")
