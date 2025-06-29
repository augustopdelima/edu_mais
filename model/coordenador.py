from model.usuario import Usuario
from security.permissao import Permissao


class Coordenador(Usuario):
    def __init__(self, id: int, nome: str, email: str, senha: str):
        super().__init__(id=id, nome=nome, email=email,
                         senha=senha, permissao=Permissao.COORDENADOR)
