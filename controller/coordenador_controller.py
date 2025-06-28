from service.coordenador_service import CoordenadorService
from view.coordenador_view import exibir_coordenador, listar_coordenadores, exibir_coordenador_nao_encontrado, mostrar_mensagem_sucesso, mostrar_mensagem_erro


class CoordenadorController:
    def __init__(self, coordenador_service: CoordenadorService):
        print("[Controlador] Inicializando CoordenadorController")
        self.coordenador_service = coordenador_service

    def cadastrar_coordenador(self, nome: str, email: str, senha: str) -> None:
        print(f"[Controlador] Cadastrando coordenador: {nome}")
        coordenador = self.coordenador_service.cadastrar_coordenador(
            nome, email, senha)
        mostrar_mensagem_sucesso(
            f"Coordenador {coordenador.nome} cadastrado com sucesso!")

    def atualizar_coordenador(self, id: int, nome: str, email: str, senha: str) -> None:
        print(f"[Controlador] Atualizando coordenador ID {id}")
        coordenador = self.coordenador_service.atualizar_coordenador(
            id, nome, email, senha)
        if coordenador:
            mostrar_mensagem_sucesso(
                f"Coordenador ID {id} atualizado com sucesso!")
        else:
            mostrar_mensagem_erro(
                f"Coordenador ID {id} não encontrado para atualização.")

    def listar_coordenadores(self) -> None:
        print("[Controlador] Listando coordenadores")
        coordenadores = self.coordenador_service.listar_coordenadores()
        listar_coordenadores(coordenadores)

    def mostrar_coordenador_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando coordenador ID {id}")
        coordenador = self.coordenador_service.buscar_coordenador_por_id(id)
        if coordenador:
            exibir_coordenador(coordenador)
        else:
            exibir_coordenador_nao_encontrado(id)

    def deletar_coordenador(self, id: int) -> None:
        print(f"[Controlador] Deletando coordenador ID {id}")
        self.coordenador_service.remover_coordenador(id)
        mostrar_mensagem_sucesso(f"Coordenador ID {id} removido com sucesso!")
