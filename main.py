# main.py

from estudantes import (
    cadastrar_estudante, listar_estudantes,
    atualizar_estudante, excluir_estudante
)
from professores import (
    cadastrar_professor, listar_professores,
    atualizar_professor, excluir_professor
)
from disciplinas import (
    cadastrar_disciplina, listar_disciplinas,
    atualizar_disciplina, excluir_disciplina
)
from turmas import (
    cadastrar_turma, listar_turmas,
    atualizar_turma, excluir_turma
)
from matriculas import (
    cadastrar_matricula, listar_matriculas,
    atualizar_matricula, excluir_matricula
)

def menu(titulo, opcoes):
    print(f"\n=== {titulo} ===")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def menu_estudantes():
    while True:
        opcao = menu("Menu Estudantes", [
            "Cadastrar Estudante", "Listar Estudantes",
            "Atualizar Estudante", "Excluir Estudante"
        ])
        if   opcao == "1": cadastrar_estudante()
        elif opcao == "2": listar_estudantes()
        elif opcao == "3": atualizar_estudante()
        elif opcao == "4": excluir_estudante()
        elif opcao == "0": break
        else: print("Opção inválida.")

def menu_professores():
    while True:
        opcao = menu("Menu Professores", [
            "Cadastrar Professor", "Listar Professores",
            "Atualizar Professor", "Excluir Professor"
        ])
        if   opcao == "1": cadastrar_professor()
        elif opcao == "2": listar_professores()
        elif opcao == "3": atualizar_professor()
        elif opcao == "4": excluir_professor()
        elif opcao == "0": break
        else: print("Opção inválida.")

def menu_disciplinas():
    while True:
        opcao = menu("Menu Disciplinas", [
            "Cadastrar Disciplina", "Listar Disciplinas",
            "Atualizar Disciplina", "Excluir Disciplina"
        ])
        if   opcao == "1": cadastrar_disciplina()
        elif opcao == "2": listar_disciplinas()
        elif opcao == "3": atualizar_disciplina()
        elif opcao == "4": excluir_disciplina()
        elif opcao == "0": break
        else: print("Opção inválida.")

def menu_turmas():
    while True:
        opcao = menu("Menu Turmas", [
            "Cadastrar Turma", "Listar Turmas",
            "Atualizar Turma", "Excluir Turma"
        ])
        if   opcao == "1": cadastrar_turma()
        elif opcao == "2": listar_turmas()
        elif opcao == "3": atualizar_turma()
        elif opcao == "4": excluir_turma()
        elif opcao == "0": break
        else: print("Opção inválida.")

def menu_matriculas():
    while True:
        opcao = menu("Menu Matrículas", [
            "Cadastrar Matrícula", "Listar Matrículas",
            "Atualizar Matrícula", "Excluir Matrícula"
        ])
        if   opcao == "1": cadastrar_matricula()
        elif opcao == "2": listar_matriculas()
        elif opcao == "3": atualizar_matricula()
        elif opcao == "4": excluir_matricula()
        elif opcao == "0": break
        else: print("Opção inválida.")

def main():
    while True:
        opcao = menu("Sistema Educacional", [
            "Gerenciar Estudantes",
            "Gerenciar Professores",
            "Gerenciar Disciplinas",
            "Gerenciar Turmas",
            "Gerenciar Matrículas"
        ])
        if   opcao == "1": menu_estudantes()
        elif opcao == "2": menu_professores()
        elif opcao == "3": menu_disciplinas()
        elif opcao == "4": menu_turmas()
        elif opcao == "5": menu_matriculas()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
