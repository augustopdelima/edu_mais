from model.formulario import Formulario
from service.relatorio_service import RelatorioService
from view.relatorio_view import (
    exibir_relatorio,
    listar_relatorios,
    exibir_relatorio_nao_encontrado,
    mostrar_mensagem_sucesso,
)


class RelatorioController:
    def __init__(self, relatorio_service: RelatorioService):
        print("[Controlador] Inicializando RelatorioController")
        self.relatorio_service = relatorio_service

    def criar_relatorio(self, indicadores: str, graficos: str, formulario: Formulario) -> None:
        print("[Controlador] Criando relatório")
        relatorio = self.relatorio_service.criar_relatorio(
            indicadores, graficos, formulario)
        mostrar_mensagem_sucesso(
            f"Relatório ID {relatorio.id} criado com sucesso!")

    def listar_relatorios(self) -> None:
        print("[Controlador] Listando relatórios")
        relatorios = self.relatorio_service.listar_relatorios()
        listar_relatorios(relatorios)

    def mostrar_relatorio_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando relatório ID {id}")
        relatorio = self.relatorio_service.buscar_relatorio_por_id(id)
        if relatorio:
            exibir_relatorio(relatorio)
        else:
            exibir_relatorio_nao_encontrado(id)

    def deletar_relatorio(self, id: int) -> None:
        print(f"[Controlador] Deletando relatório ID {id}")
        self.relatorio_service.deletar_relatorio(id)
        mostrar_mensagem_sucesso(f"Relatório ID {id} deletado com sucesso!")
