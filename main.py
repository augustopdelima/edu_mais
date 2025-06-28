from controller.professor_controller import ProfessorController
from controller.aluno_controller import AlunoController
from controller.disciplina_controller import DisciplinaController
from controller.turma_controller import TurmaController
from controller.coordenador_controller import CoordenadorController
from controller.formulario_controller import FormularioController
from controller.avalicao_controller import AvaliacaoController
from controller.historico_controller import HistoricoAvaliacaoController
from repository.professor_repository import ProfessorRepository
from service.historico_service import HistoricoAvaliacaoService
from repository.historico_repository import HistoricoAvaliacaoRepository
from service.professor_service import ProfessorService


def exibir_menu():
    print("\n=== Sistema de Avaliação Acadêmica ===")
    print("1. Professores")
    print("2. Alunos")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Coordenadores")
    print("6. Formulários")
    print("7. Avaliações")
    print("8. Histórico de Avaliações")
    print("0. Sair")


def menu_professor():
    professor_repository = ProfessorRepository()
    professor_service = ProfessorService(professor_repository)
    controller = ProfessorController(professor_service)

    controller.cadastrar_professor("João Silva", "joao@edu.com")
    controller.cadastrar_professor("Ana Lima", "ana@edu.com")

    controller.listar_professores()
    controller.mostrar_professor_por_id(1)


def menu_aluno():
    controller = AlunoController()
    controller.cadastrar_aluno()
    controller.listar_aluno()


def menu_disciplina():
    controller = DisciplinaController()
    controller.cadastrar_disciplina()
    controller.listar_disciplinas()


def menu_turma():
    controller = TurmaController()
    controller.cadastrar_turma_interativo()
    controller.listar_turmas()


def menu_coordenador():
    controller = CoordenadorController()
    controller.cadastrar_coordenador()
    controller.listar_coordenadores()


def menu_formulario():
    controller = FormularioController()
    controller.cadastrar_formulario()
    controller.listar_formularios()


def menu_avaliacao():
    controller = AvaliacaoController()
    controller.realizar_avaliacao()
    controller.listar_avaliacoes()


def menu_historico():
    repo = HistoricoAvaliacaoRepository()
    service = HistoricoAvaliacaoService(repo)
    controller = HistoricoAvaliacaoController(service)
    controller.listar_todos()


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_professor()
        elif opcao == "2":
            menu_aluno()
        elif opcao == "3":
            menu_disciplina()
        elif opcao == "4":
            menu_turma()
        elif opcao == "5":
            menu_coordenador()
        elif opcao == "6":
            menu_formulario()
        elif opcao == "7":
            menu_avaliacao()
        elif opcao == "8":
            menu_historico()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
