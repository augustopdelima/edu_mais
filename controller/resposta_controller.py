from service.resposta_service import RespostaService
from view.resposta_view import (
    exibir_resposta,
    listar_respostas,
    exibir_resposta_nao_encontrada,
    mostrar_mensagem_sucesso,
)


class RespostaController:
    def __init__(self, resposta_service: RespostaService):
        print("[Controlador] Inicializando RespostaController")
        self.resposta_service = resposta_service

    def cadastrar_resposta(self, formulario, resposta_texto: str) -> None:
        print("[Controlador] Cadastrando resposta")
        resposta = self.resposta_service.cadastrar_resposta(
            formulario, resposta_texto)
        mostrar_mensagem_sucesso(
            f"Resposta ID {resposta.id} cadastrada com sucesso!")

    def listar_respostas(self) -> None:
        print("[Controlador] Listando respostas")
        respostas = self.resposta_service.listar_respostas()
        listar_respostas(respostas)

    def mostrar_resposta_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando resposta ID {id}")
        resposta = self.resposta_service.buscar_resposta_por_id(id)
        if resposta:
            exibir_resposta(resposta)
        else:
            exibir_resposta_nao_encontrada(id)

    def deletar_resposta(self, id: int) -> None:
        print(f"[Controlador] Deletando resposta ID {id}")
        self.resposta_service.deletar_resposta(id)
        mostrar_mensagem_sucesso(f"Resposta ID {id} deletada com sucesso!")
