from typing import List, Optional
from model.disciplina import Disciplina
from repository.disciplina_repository import DisciplinaRepository
from model.professor import Professor


class DisciplinaService:
    def __init__(self, disciplina_repository: DisciplinaRepository):
        print("[Serviço] Inicializando DisciplinaService")
        self.disciplina_repository = disciplina_repository

    def cadastrar_disciplina(self, nome: str, semestre: str, descricao: str, professor: Professor) -> Disciplina:
        print(f"[Serviço] Cadastrando disciplina: {nome}, semestre {semestre}")
        # Retorna um dummy para exemplo
        return Disciplina(1, nome, semestre, descricao, professor)

    def listar_disciplinas(self) -> List[Disciplina]:
        print("[Serviço] Listando disciplinas")
        return []

    def buscar_disciplina_por_id(self, id: int) -> Optional[Disciplina]:
        print(f"[Serviço] Buscando disciplina por ID: {id}")
        return None

    def remover_disciplina(self, id: int) -> None:
        print(f"[Serviço] Removendo disciplina com ID: {id}")
