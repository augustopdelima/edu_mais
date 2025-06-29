from model.usuario import Usuario
from security.permissao import Permissao


def validar_permissao(usuario: Usuario, permissoes_permitidas: list[Permissao]) -> bool:
    """
    Verifica se o usuário tem permissão para executar a ação.
    """
    if usuario.permissao in permissoes_permitidas:
        return True
    print(f"[PERMISSÃO NEGADA] Usuário '{usuario.nome}' não tem permissão.")
    return False
