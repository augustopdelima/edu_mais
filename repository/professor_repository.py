from typing import List, Optional
from model.professor import Professor


class ProfessorRepository:
    def __init__(self):
        self.professores: List[Professor] = []

    def salvar(self, professor: Professor) -> None:
        print(f"[Repositório] Salvando professor: {professor.nome}")
        self.professores.append(professor)

    def listar_todos(self) -> List[Professor]:
        print("[Repositório] Listando todos os professores")
        return self.professores

    def buscar_por_id(self, id: int) -> Optional[Professor]:
        print(f"[Repositório] Buscando professor pelo ID: {id}")

    def remover(self, id: int) -> None:
        print(f"[Repositório] Removendo professor com ID: {id}")
