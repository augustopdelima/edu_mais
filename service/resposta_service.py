from typing import List, Optional
from model.resposta import Resposta
from model.formulario import Formulario
from repository.resposta_repository import RespostaRepository


class RespostaService:
    def __init__(self, resposta_repository: RespostaRepository):
        print("[Serviço] Inicializando RespostaService")
        self.resposta_repository = resposta_repository

    def cadastrar_resposta(self, formulario: Formulario, resposta_texto: str) -> Resposta:
        print("[Serviço] Cadastrando resposta")
        novo_id = len(self.resposta_repository.listar_todos()) + 1
        resposta = Resposta(novo_id, formulario, resposta_texto)
        self.resposta_repository.salvar(resposta)
        return resposta

    def listar_respostas(self) -> List[Resposta]:
        print("[Serviço] Listando respostas")
        return self.resposta_repository.listar_todos()

    def buscar_resposta_por_id(self, id: int) -> Optional[Resposta]:
        print(f"[Serviço] Buscando resposta por ID {id}")
        return self.resposta_repository.buscar_por_id(id)

    def deletar_resposta(self, id: int) -> None:
        print(f"[Serviço] Deletando resposta ID {id}")
        self.resposta_repository.deletar(id)
