# matriculas.py
from util import (
    carregar_dados, salvar_dados,
    listar_registros, atualizar_registro, excluir_registro
)

ARQUIVO = "matriculas.json"

def cadastrar_matricula():
    estudante = input("Digite o nome ou matrícula do estudante: ").strip()
    disciplina = input("Digite o código da disciplina: ").strip().upper()
    turma = input("Digite o código da turma: ").strip().upper()

    matricula = {
        "estudante": estudante,
        "disciplina": disciplina,
        "turma": turma
    }

    matriculas = carregar_dados(ARQUIVO)
    matriculas.append(matricula)
    salvar_dados(ARQUIVO, matriculas)
    print("Matrícula realizada com sucesso!")

def listar_matriculas():
    listar_registros(ARQUIVO, ["estudante", "disciplina", "turma"])

def atualizar_matricula():
    atualizar_registro(ARQUIVO, ["estudante", "disciplina", "turma"])

def excluir_matricula():
    excluir_registro(ARQUIVO)
