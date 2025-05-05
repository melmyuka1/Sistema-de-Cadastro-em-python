
from util import (
    carregar_dados, salvar_dados,
    listar_registros, atualizar_registro, excluir_registro, codigo_existe
)

ARQUIVO = "disciplinas.json"

def cadastrar_disciplina():
    nome = input("Digite o nome da disciplina: ").strip()
    codigo = input("Digite o código da disciplina (ex: MAT101): ").strip().upper()

    if codigo_existe(ARQUIVO, "codigo", codigo):
        print("Já existe uma disciplina com esse código.")
        return

    disciplina = {
        "nome": nome,
        "codigo": codigo
    }

    disciplinas = carregar_dados(ARQUIVO)
    disciplinas.append(disciplina)
    salvar_dados(ARQUIVO, disciplinas)
    print("Disciplina cadastrada com sucesso!")

def listar_disciplinas():
    listar_registros(ARQUIVO, ["nome", "codigo"])

def atualizar_disciplina():
    atualizar_registro(ARQUIVO, ["nome", "codigo"])

def excluir_disciplina():
    excluir_registro(ARQUIVO)
