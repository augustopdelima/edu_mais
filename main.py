from controller.professor_controller import ProfessorController


def main() -> None:
    controller = ProfessorController()

    controller.cadastrar_professor("João Silva", "joao@edu.com")
    controller.cadastrar_professor("Ana Lima", "ana@edu.com")

    controller.listar_professores()

    controller.mostrar_professor_por_id(1)


if __name__ == "__main__":
    main()
