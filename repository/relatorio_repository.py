from typing import List, Optional
from model.relatorio import Relatorio


class RelatorioRepository:
    def __init__(self):
        self.relatorios = list[Relatorio]

    def salvar(self, relatorio: Relatorio) -> None:
        print(f"[Repositório] Salvando relatório ID: {relatorio.id}")
        self.relatorios.append(relatorio)

    def listar_todos(self) -> List[Relatorio]:
        print("[Repositório] Listando todos os relatórios")
        return self.relatorios

    def buscar_por_id(self, id: int) -> Optional[Relatorio]:
        print(f"[Repositório] Buscando relatório pelo ID: {id}")
        for relatorio in self.relatorios:
            if relatorio.id == id:
                return relatorio
        return None

    def deletar(self, id: int) -> None:
        print(f"[Repositório] Deletando relatório com ID: {id}")
        self.relatorios = [r for r in self.relatorios if r.id != id]
