from util import (
    carregar_dados, salvar_dados,
    validar_nome, validar_idade, validar_matricula,
    listar_registros, atualizar_registro, excluir_registro, codigo_existe
)

ARQUIVO = "professores.json"

def cadastrar_professor():
    nome = validar_nome("nome do professor")
    idade = validar_idade()
    matricula = validar_matricula()

    if codigo_existe(ARQUIVO, "matricula", matricula):
        print("Já existe um professor com essa matrícula.")
        return

    professor = {
        "nome": nome,
        "idade": idade,
        "matricula": matricula
    }

    professores = carregar_dados(ARQUIVO)
    professores.append(professor)
    salvar_dados(ARQUIVO, professores)
    print("Professor cadastrado com sucesso!")

def listar_professores():
    listar_registros(ARQUIVO, ["nome", "idade", "matricula"])

def atualizar_professor():
    atualizar_registro(ARQUIVO, ["nome", "idade", "matricula"])

def excluir_professor():
    excluir_registro(ARQUIVO)
