from typing import List, Optional
from model.formulario import Formulario


class FormularioRepository:
    def salvar(self, formulario: Formulario) -> None:
        print(f"[Repositório] Salvando formulário ID {formulario.id}")

    def listar_todos(self) -> List[Formulario]:
        print("[Repositório] Listando todos os formulários")
        return []

    def buscar_por_id(self, id: int) -> Optional[Formulario]:
        print(f"[Repositório] Buscando formulário pelo ID: {id}")
        return None

    def deletar(self, id: int) -> None:
        print(f"[Repositório] Deletando formulário com ID: {id}")
