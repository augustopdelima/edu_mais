from typing import List
from model.formulario import Formulario


def exibir_formulario(formulario: Formulario) -> None:
    print("=== Detalhes do Formulário ===")
    print(f"ID: {formulario.id}")
    print(f"Data da Aplicação: {formulario.data_aplicacao}")
    print(f"Disciplina: {formulario.disciplina.nome}")
    print(f"Turma: {formulario.turma.nome}")
    print(f"Criado por: {formulario.criado_por.nome}")
    print(f"Avaliar: {formulario.avaliar.nome}")
    print(f"Perguntas:")
    for i, pergunta in enumerate(formulario.perguntas, start=1):
        print(f"  {i}. {pergunta.texto}")
    print("==============================\n")


def listar_formularios(formularios: List[Formulario]) -> None:
    print("=== Lista de Formulários ===")
    for f in formularios:
        print(f"[{f.id}] {f.disciplina.nome} - {f.turma.nome} - {f.data_aplicacao}")
    print("============================\n")


def exibir_formulario_nao_encontrado(id: int) -> None:
    print(f"Formulário com ID {id} não encontrado.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")


def mostrar_mensagem_erro(mensagem: str) -> None:
    print(f"Erro: {mensagem}\n")
