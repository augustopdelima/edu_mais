from typing import List
from model.questao import Questao


def exibir_questao(questao: Questao) -> None:
    print("=== Detalhes da Questão ===")
    print(f"ID: {questao.id}")
    print(f"Tipo: {questao.tipo}")
    print(f"Pergunta: {questao.pergunta}")
    print("===========================\n")


def listar_questoes(questoes: List[Questao]) -> None:
    print("=== Lista de Questões ===")
    for q in questoes:
        print(f"[{q.id}] ({q.tipo}) {q.pergunta}")
    print("=========================\n")


def exibir_questao_nao_encontrada(id: int) -> None:
    print(f"Questão com ID {id} não encontrada.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")


def mostrar_mensagem_erro(mensagem: str) -> None:
    print(f"Erro: {mensagem}\n")
