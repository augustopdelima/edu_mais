from typing import List, Optional
from model.coordenador import Coordenador
from repository.coordenador_repository import CoordenadorRepository


class CoordenadorService:
    def __init__(self, coordenador_repository: CoordenadorRepository):
        print("[Serviço] Inicializando CoordenadorService")
        self.coordenador_repository = coordenador_repository

    def cadastrar_coordenador(self, nome: str, email: str, senha: str) -> Coordenador:
        print(f"[Serviço] Cadastrando coordenador: {nome}, {email}")
        # Retorna um objeto dummy para exemplo
        return Coordenador(1, nome, email, senha)

    def atualizar_coordenador(self, id: int, nome: str, email: str, senha: str) -> Optional[Coordenador]:
        print(
            f"[Serviço] Atualizando coordenador ID {id} com dados: {nome}, {email}")
        return None

    def listar_coordenadores(self) -> List[Coordenador]:
        print("[Serviço] Listando coordenadores")
        return []

    def buscar_coordenador_por_id(self, id: int) -> Optional[Coordenador]:
        print(f"[Serviço] Buscando coordenador por ID: {id}")
        return None

    def buscar_coordenador_por_email(self, email: str) -> Optional[Coordenador]:
        print(f"[Serviço] Buscando coordenador por email: {email}")
        return None

    def remover_coordenador(self, id: int) -> None:
        print(f"[Serviço] Removendo coordenador com ID: {id}")
