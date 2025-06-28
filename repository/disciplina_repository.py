from typing import List, Optional
from model.disciplina import Disciplina


class DisciplinaRepository:

    def __init__(self):
        self.disciplinas = list[Disciplina]

    def salvar(self, disciplina: Disciplina) -> None:
        print(f"[Repositório] Salvando disciplina: {disciplina.nome}")

    def listar_todos(self) -> List[Disciplina]:
        print("[Repositório] Listando todas as disciplinas")
        return []

    def buscar_por_id(self, id: int) -> Optional[Disciplina]:
        print(f"[Repositório] Buscando disciplina pelo ID: {id}")
        return None

    def deletar(self, id: int) -> None:
        print(f"[Repositório] Deletando disciplina com ID: {id}")
