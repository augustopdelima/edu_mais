from typing import List
from model.avaliacao import Avaliacao
from model.formulario import Formulario


def solicitar_respostas(formulario: Formulario) -> List[str]:
    print(
        f"\nRespondendo formulário da disciplina: {formulario.disciplina.nome}")
    respostas = []
    for i, questao in enumerate(formulario.perguntas, start=1):
        resposta = input(f"{i}. {questao.pergunta} ")
        respostas.append(resposta)
    return respostas


def exibir_avaliacao(avaliacao: Avaliacao):
    print("\n=== Avaliação ===")
    print(f"ID: {avaliacao.id}")
    print(f"Aluno: {avaliacao.aluno.nome}")
    print(f"Professor Avaliado: {avaliacao.professor_avaliado.nome}")
    print(f"Disciplina: {avaliacao.formulario.disciplina.nome}")
    print("Respostas:")
    for i, r in enumerate(avaliacao.respostas, start=1):
        print(f"{i}. {r.questao.pergunta} => {r.resposta}")
    print("======================\n")


def listar_avaliacoes(avaliacoes: List[Avaliacao]):
    print("=== Lista de Avaliações ===")
    for a in avaliacoes:
        print(
            f"[{a.id}] Aluno: {a.aluno.nome} -> Professor: {a.professor_avaliado.nome}")
    print("===========================\n")


def exibir_avaliacao_nao_encontrada(id: int):
    print(f"Avaliação com ID {id} não encontrada.\n")


def mostrar_mensagem_sucesso(mensagem: str):
    print(f"✅ {mensagem}\n")
