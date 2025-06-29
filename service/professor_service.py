
from typing import List, Optional
from model.professor import Professor
from repository.professor_repository import ProfessorRepository


class ProfessorService:
    def __init__(self, professor_repository: ProfessorRepository):
        print("[Serviço] Inicializando ProfessorService")
        self.professor_repository = professor_repository

    def cadastrar_professor(self, nome: str, email: str, senha: str) -> Professor:
        print(f"[Serviço] Cadastrando professor: {nome}")
        # Retorna um dummy para exemplo
        return Professor(1, nome, email, senha)

    def listar_professores(self) -> List[Professor]:
        print("[Serviço] Listando professores")
        return []

    def buscar_professor_por_id(self, id: int) -> Optional[Professor]:
        print(f"[Serviço] Buscando professor por ID: {id}")
        return None

    def remover_professor(self, id: int) -> None:
        print(f"[Serviço] Removendo professor com ID: {id}")
