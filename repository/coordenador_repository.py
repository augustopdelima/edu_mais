from typing import List, Optional
from model.coordenador import Coordenador


class CoordenadorRepository:

    def __init__(self):
        self.coordenadores = list[Coordenador]

    def salvar(self, coordenador: Coordenador) -> None:
        """Salva um novo coordenador ou atualiza um existente."""
        pass

    def listar_todos(self) -> List[Coordenador]:
        """Retorna todos coordenadores cadastrados."""
        pass

    def buscar_por_id(self, id: int) -> Optional[Coordenador]:
        """Busca coordenador pelo ID."""
        pass

    def buscar_por_email(self, email: str) -> Optional[Coordenador]:
        """Busca coordenador pelo email (útil para login)."""
        pass

    def deletar(self, id: int) -> None:
        """Deleta coordenador pelo ID."""
        pass
