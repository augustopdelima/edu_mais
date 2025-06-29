from typing import List, Optional
from model.resposta import Resposta


class RespostaRepository:
    def __init__(self):
        self.respostas: List[Resposta] = []

    def salvar(self, resposta: Resposta) -> None:
        print(f"[Repositório] Salvando resposta ID {resposta.id}")
        self.respostas.append(resposta)

    def listar_todos(self) -> List[Resposta]:
        print("[Repositório] Listando todas as respostas")
        return self.respostas

    def buscar_por_id(self, id: int) -> Optional[Resposta]:
        print(f"[Repositório] Buscando resposta pelo ID {id}")

    def deletar(self, id: int) -> None:
        print(f"[Repositório] Deletando resposta ID {id}")
