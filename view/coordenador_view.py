
from typing import List
from model.coordenador import Coordenador


def exibir_coordenador(coordenador: Coordenador) -> None:
    print("=== Detalhes do Coordenador ===")
    print(f"ID: {getattr(coordenador, 'id', 'N/A')}")
    print(f"Nome: {coordenador.nome}")
    print(f"Email: {coordenador.email}")
    print("==============================\n")


def listar_coordenadores(coordenadores: List[Coordenador]) -> None:
    print("=== Lista de Coordenadores ===")
    for c in coordenadores:
        print(f"[{getattr(c, 'id', 'N/A')}] {c.nome} - {c.email}")
    print("=============================\n")


def exibir_coordenador_nao_encontrado(id: int) -> None:
    print(f"Coordenador com ID {id} não encontrado.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")


def mostrar_mensagem_erro(mensagem: str) -> None:
    print(f"Erro: {mensagem}\n")
