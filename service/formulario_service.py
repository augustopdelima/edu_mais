
from typing import List, Optional
from model.formulario import Formulario
from repository.formulario_repository import FormularioRepository
from model.disciplina import Disciplina
from model.turma import Turma
from model.coordenador import Coordenador
from model.professor import Professor
from model.questao import Questao


class FormularioService:
    def __init__(self, formulario_repository: FormularioRepository):
        print("[Serviço] Inicializando FormularioService")
        self.formulario_repository = formulario_repository

    def cadastrar_formulario(self, data_aplicacao: str, disciplina: Disciplina,
                             turma: Turma, criado_por: Coordenador,
                             avaliar: Professor, perguntas: List[Questao]) -> Formulario:
        print(
            f"[Serviço] Cadastrando formulário para disciplina {disciplina.nome}")
        # Retorna um valor qualquer para exemplo
        return Formulario(1, data_aplicacao, disciplina, turma, criado_por, avaliar, perguntas)

    def listar_formularios(self) -> List[Formulario]:
        print("[Serviço] Listando formulários")
        return []

    def buscar_formulario_por_id(self, id: int) -> Optional[Formulario]:
        print(f"[Serviço] Buscando formulário por ID: {id}")
        return None

    def remover_formulario(self, id: int) -> None:
        print(f"[Serviço] Removendo formulário com ID: {id}")
