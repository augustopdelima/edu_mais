from controller.professor_controller import ProfessorController
from model.aluno import Aluno
from model.avaliacao import Avaliacao
from model.disciplina import Disciplina
from model.formulario import Formulario
from model.professor import Professor
from model.relatorio import Relatorio
from model.resposta import Resposta
from repository.aluno_repository import AlunoRepository
from repository.coordenador_repository import CoordenadorRepository
from repository.disciplina_repository import DisciplinaRepository
from repository.professor_repository import ProfessorRepository
from repository.turma_repository import TurmaRepository


from service.aluno_service import AlunoService
from service.coordenador_service import CoordenadorService
from service.disciplina_service import DisciplinaService
from service.professor_service import ProfessorService
from service.turma_service import TurmaService
from controller.aluno_controller import AlunoController
from controller.coordenador_controller import CoordenadorController
from controller.disciplina_controller import DisciplinaController
from controller.turma_controller import TurmaController


from model.coordenador import Coordenador
from model.turma import Turma
from model.questao import Questao


def menu_aluno():
    aluno_repo = AlunoRepository()
    aluno_service = AlunoService(aluno_repo)
    controller = AlunoController(aluno_service)

    controller.cadastrar_aluno(
        nome='Aluno Teste', email='aluno@teste.com', matricula='12234')
    controller.listar_alunos()


def menu_coordenador():
    coord_repo = CoordenadorRepository()
    coord_service = CoordenadorService(coord_repo)
    controller = CoordenadorController(coord_service)

    controller.cadastrar_coordenador(
        nome='Coord Teste', email='coord@teste.com')
    controller.listar_coordenadores()


def menu_disciplina():
    disciplina_repo = DisciplinaRepository()
    disciplina_service = DisciplinaService(disciplina_repo)
    controller = DisciplinaController(disciplina_service)

    controller.cadastrar_disciplina(nome='Disciplina Teste', descricao='Teste', professor=Professor(
        nome="João Silva", email="joao@edu.com", id=1), semestre='2')
    controller.listar_disciplinas()


def menu_turma():
    turma_repo = TurmaRepository()
    turma_service = TurmaService(turma_repo)
    controller = TurmaController(turma_service)

    # Criando dados exemplo
    alunos = [
        Aluno(id=1, nome="Carlos Silva",
              email="carlos@teste.com", matricula="2024001"),
        Aluno(id=2, nome="Mariana Souza",
              email="mariana@teste.com", matricula="2024002"),
    ]
    disciplina = Disciplina(id=1, nome="Matemática", descricao="Matemática básica",
                            semestre="1", professor=None)  # Passe o professor se necessário

    # Chamando o método de cadastro com dados preenchidos
    controller.cadastrar_turma(
        nome="Turma A",
        ano=2025,
        semestre=1,
        disciplina=disciplina,
        alunos=alunos
    )


def menu_professor():
    professor_repo = ProfessorRepository()
    professor_service = ProfessorService(professor_repo)
    controller = ProfessorController(professor_service)

    # Exemplos de uso:
    controller.cadastrar_professor(nome='João Silva', email='joao@edu.com')
    controller.cadastrar_professor(nome='Ana Lima', email='ana@edu.com')

    controller.listar_professores()
    controller.mostrar_professor_por_id(1)


def exibir_menu():
    print("\n=== Sistema de Avaliação Acadêmica ===")
    print("1. Professores")
    print("2. Alunos")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Coordenadores")
    print("6. Formulários")
    print("0. Sair")


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
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
