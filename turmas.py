from util import (
    carregar_dados, salvar_dados,
    listar_registros, atualizar_registro, excluir_registro, codigo_existe
)

ARQUIVO = "turmas.json"

def cadastrar_turma():
    codigo = input("Digite o código da turma (ex: T01): ").strip().upper()
    descricao = input("Digite a descrição da turma: ").strip()

    if codigo_existe(ARQUIVO, "codigo", codigo):
        print("Já existe uma turma com esse código.")
        return

    turma = {
        "codigo": codigo,
        "descricao": descricao
    }

    turmas = carregar_dados(ARQUIVO)
    turmas.append(turma)
    salvar_dados(ARQUIVO, turmas)
    print("Turma cadastrada com sucesso!")

def listar_turmas():
    listar_registros(ARQUIVO, ["codigo", "descricao"])

def atualizar_turma():
    atualizar_registro(ARQUIVO, ["codigo", "descricao"])

def excluir_turma():
    excluir_registro(ARQUIVO)
