from typing import List
from model.avaliacao import Avaliacao
from model.aluno import Aluno
from model.professor import Professor
from model.formulario import Formulario
from model.resposta import Resposta
from repository.avaliacao_repository import AvaliacaoRepository


class AvaliacaoService:
    def __init__(self, avaliacao_repository: AvaliacaoRepository):
        self.avaliacao_repository = avaliacao_repository

    def cadastrar_avaliacao(
        self,
        aluno: Aluno,
        formulario: Formulario,
        professor_avaliado: Professor,
        respostas_texto: List[str]
    ) -> Avaliacao:
        respostas = []
        for idx, pergunta in enumerate(formulario.perguntas):
            resposta = Resposta(
                id=idx + 1,
                formulario=formulario,
                questao=pergunta,
                resposta=respostas_texto[idx]
            )
            respostas.append(resposta)

        novo_id = len(self.avaliacao_repository.listar_todos()) + 1
        avaliacao = Avaliacao(novo_id, aluno, formulario,
                              professor_avaliado, respostas)
        self.avaliacao_repository.salvar(avaliacao)
        return avaliacao
