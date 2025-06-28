from service.cadastro_service import CadastroService
from view.coordenador_view import exibir_coordenador, listar_coordenadores, exibir_coordenador_nao_encontrado, mostrar_mensagem_sucesso, solicitar_dados_coordenador


class CoordenadorController:
    def __init__(self):
        self.coordenador_repository = []
        self.cadastro_service = CadastroService(
            coordenadores=self.coordenador_repository)

    def cadastrar_coordenador(self):
        nome, email = solicitar_dados_coordenador()
        coordenador = self.cadastro_service.cadastrar_coordenador(nome, email)
        mostrar_mensagem_sucesso(coordenador)

    def listar_coordenadores(self):
        coordenadores = self.coordenador_repository.listar_todos()
        listar_coordenadores(coordenadores)

    def mostrar_coordenador_por_id(self, id: int):
        coordenador = self.coordenador_repository.buscar_por_id(id)
        if coordenador:
            exibir_coordenador(coordenador)
        else:
            exibir_coordenador_nao_encontrado(id)
