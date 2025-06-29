from model.coordenador import Coordenador  # ajuste conforme seu projeto
from typing import List, Optional


class CoordenadorRepository:
    def __init__(self):
        self.coordenadores: List[Coordenador] = []
        print("[CoordenadorRepository] Inicializado")

    def salvar(self, coordenador: Coordenador) -> None:
        print(
            f"[CoordenadorRepository] Salvando coordenador: {coordenador.nome}")

    def listar_todos(self) -> List[Coordenador]:
        print("[CoordenadorRepository] Listando todos os coordenadores")
        return []

    def buscar_por_id(self, id: int) -> Optional[Coordenador]:
        print(f"[CoordenadorRepository] Buscando coordenador pelo ID: {id}")
        return None

    def deletar(self, id: int) -> None:
        print(f"[CoordenadorRepository] Deletando coordenador com ID: {id}")
