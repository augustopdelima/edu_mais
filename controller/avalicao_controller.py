from model.usuario import Usuario
from security.permissao import Permissao
from security.validador_permissao import validar_permissao
from service.avaliacao_service import AvaliacaoService
from model.aluno import Aluno
from model.professor import Professor
from model.formulario import Formulario
from view.avalicao_view import (
    solicitar_respostas,
    mostrar_mensagem_sucesso,
    exibir_avaliacao,
    exibir_avaliacao_nao_encontrada,
    listar_avaliacoes
)


class AvaliacaoController:
    def __init__(self, avaliacao_service: AvaliacaoService):
        self.avaliacao_service = avaliacao_service

    def realizar_avaliacao(self, usuario: Usuario, aluno: Aluno, formulario: Formulario, professor: Professor):

        validar_permissao(usuario, [Permissao.ALUNO])

        respostas = solicitar_respostas(formulario)
        avaliacao = self.avaliacao_service.cadastrar_avaliacao(
            aluno=aluno,
            formulario=formulario,
            professor_avaliado=professor,
            respostas_texto=respostas
        )
        mostrar_mensagem_sucesso(
            f"Avaliação ID {avaliacao.id} realizada com sucesso.")

    def listar_avaliacoes(self):
        avaliacoes = self.avaliacao_service.listar_avaliacoes()
        listar_avaliacoes(avaliacoes)

    def mostrar_avaliacao_por_id(self, id: int):
        avaliacao = self.avaliacao_service.buscar_avaliacao_por_id(id)
        if avaliacao:
            exibir_avaliacao(avaliacao)
        else:
            exibir_avaliacao_nao_encontrada(id)
