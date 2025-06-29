
from typing import List
from model.relatorio import Relatorio


def exibir_relatorio(relatorio: Relatorio) -> None:
    print("=== Detalhes do Relatório ===")
    print(f"ID: {relatorio.id}")
    print(f"Indicadores: {relatorio.indicadores}")
    print(f"Gráficos: {relatorio.graficos}")
    print(f"Formulário relacionado: {relatorio.formulario}")
    print("=============================\n")


def listar_relatorios(relatorios: List[Relatorio]) -> None:
    print("=== Lista de Relatórios ===")
    for r in relatorios:
        print(f"[{r.id}] Indicadores: {r.indicadores} | Gráficos: {r.graficos}")
    print("===========================\n")


def exibir_relatorio_nao_encontrado(id: int) -> None:
    print(f"Relatório com ID {id} não encontrado.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")


def mostrar_mensagem_erro(mensagem: str) -> None:
    print(f"Erro: {mensagem}\n")
