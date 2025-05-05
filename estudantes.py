from util import (
    carregar_dados,
    salvar_dados,
    validar_nome,
    validar_idade,
    validar_matricula,
    listar_registros,
    excluir_registro,
    atualizar_registro,
    codigo_existe
)

ARQUIVO = "estudantes.json"

def cadastrar_estudante():
    nome = validar_nome("nome do estudante")
    idade = validar_idade()
    matricula = validar_matricula()
   

    if codigo_existe(ARQUIVO, "matricula", matricula):
        print("Já existe um estudante com essa matrícula.")
        return

    estudante = {
        "nome": nome,
        "idade": idade,
        "matricula": matricula
    }

    estudantes = carregar_dados(ARQUIVO)
    estudantes.append(estudante)
    salvar_dados(ARQUIVO, estudantes)
    print("Estudante cadastrado com sucesso!")

def listar_estudantes():
    listar_registros(ARQUIVO, ["nome", "idade", "matricula"])

def excluir_estudante():
    excluir_registro(ARQUIVO)

def atualizar_estudante():
    atualizar_registro(ARQUIVO, ["nome", "idade", "matricula"])