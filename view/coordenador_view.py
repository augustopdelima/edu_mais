from model.coordenador import Coordenador
from typing import List


def exibir_coordenador(coordenador: Coordenador):
    print("=== Coordenador ===")
    print(f"ID: {coordenador.id}")
    print(f"Nome: {coordenador.nome}")
    print(f"Email: {coordenador.email}")
    print("===================\n")


def listar_coordenadores(coordenadores: List[Coordenador]):
    print("=== Lista de Coordenadores ===")
    for c in coordenadores:
        print(f"[{c.id}] {c.nome} <{c.email}>")
    print("==============================\n")


def exibir_coordenador_nao_encontrado(id: int):
    print(f"Coordenador com ID {id} não encontrado.\n")


def solicitar_dados_coordenador():
    print("=== Cadastro de Coordenador ===")
    nome = input("Nome do coordenador: ").strip()
    email = input("Email do coordenador: ").strip()
    return nome, email


def mostrar_mensagem_sucesso(coordenador: Coordenador):
    print(
        f"Coordenador '{coordenador.nome}' cadastrado com sucesso! (ID: {coordenador.id})\n")
