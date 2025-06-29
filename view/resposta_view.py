from typing import List
from model.resposta import Resposta


def exibir_resposta(resposta: Resposta) -> None:
    print("=== Detalhes da Resposta ===")
    print(f"ID: {resposta.id}")
    print(f"Formulario ID: {resposta.formulario.id}")
    print(f"Resposta: {resposta.resposta}")
    print("============================\n")


def listar_respostas(respostas: List[Resposta]) -> None:
    print("=== Lista de Respostas ===")
    for r in respostas:
        print(f"[{r.id}] Formulario ID: {r.formulario.id} | Resposta: {r.resposta}")
    print("==========================\n")


def exibir_resposta_nao_encontrada(id: int) -> None:
    print(f"Resposta com ID {id} não encontrada.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")
