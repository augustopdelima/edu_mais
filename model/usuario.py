from security.permissao import Permissao


class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str, permissao: Permissao):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.permissao = permissao
