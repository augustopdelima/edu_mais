from model.usuario import Usuario
from security.permissao import Permissao


class Professor(Usuario):
    def __init__(self, id: int, nome: str, email: str, senha: str):
        super().__init__(id=id, email=email, nome=nome,
                         senha=senha, permissao=Permissao.PROFESSOR)
