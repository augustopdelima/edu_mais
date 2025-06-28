from typing import List, Optional
from model.relatorio import Relatorio
from repository.relatorio_repository import RelatorioRepository


class RelatorioService:
    def __init__(self, relatorio_repository: RelatorioRepository):
        print("[Serviço] Inicializando RelatorioService")
        self.relatorio_repository = relatorio_repository

    def criar_relatorio(self, indicadores: str, graficos: str) -> Relatorio:
        print("[Serviço] Criando relatório")
        novo_id = len(self.relatorio_repository.listar_todos()) + 1
        relatorio = Relatorio(novo_id, indicadores, graficos)
        self.relatorio_repository.salvar(relatorio)
        return relatorio

    def listar_relatorios(self) -> List[Relatorio]:
        print("[Serviço] Listando relatórios")
        return self.relatorio_repository.listar_todos()

    def buscar_relatorio_por_id(self, id: int) -> Optional[Relatorio]:
        print(f"[Serviço] Buscando relatório por ID: {id}")
        return self.relatorio_repository.buscar_por_id(id)

    def deletar_relatorio(self, id: int) -> None:
        print(f"[Serviço] Deletando relatório ID: {id}")
        self.relatorio_repository.deletar(id)
