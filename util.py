# util.py
import json
import os

# Define o caminho base para a pasta onde os JSONs estão
CAMINHO_BASE = os.path.join(os.path.dirname(__file__), "JSON's")

def caminho_arquivo(nome_arquivo):
    return os.path.join(CAMINHO_BASE, nome_arquivo)

# Função  para carregar dados 
def carregar_dados(nome_arquivo):
    caminho = os.path.join(CAMINHO_BASE, nome_arquivo)
    try:
        with open(caminho, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Função genérica para salvar dados de qualquer entidade
def salvar_dados(nome_arquivo, dados):
    caminho = os.path.join(CAMINHO_BASE, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

# Função para validar nome (somente letras e espaços)
def validar_nome(entidade="nome"):
    while True:
        nome = input(f"Digite o {entidade}: ").strip()
        if all(palavra.isalpha() for palavra in nome.split()):
            return nome
        print(f"{entidade.capitalize()} inválido! Digite apenas letras.")

# Função para validar idade
def validar_idade():
    while True:
        idade = input("Digite a idade: ").strip()
        if idade.isdigit() and 1 <= int(idade) <= 99:
            return idade
        print("Idade inválida! Digite um número entre 1 e 99.")

# Função para validar matrícula (só números, máx 8 caracteres)
def validar_matricula():
    while True:
        matricula = input("Digite a matrícula (máx 8 dígitos): ").strip()
        if matricula.isdigit() and 1 <= len(matricula) <= 8:
            return matricula
        print("Matrícula inválida! Deve conter apenas números (até 8 dígitos).")

# Função para validar código numérico (usado em professor, disciplina, turma, etc)
def validar_codigo(tipo="código"):
    while True:
        codigo = input(f"Digite o {tipo}: ").strip()
        if codigo.isdigit():
            return int(codigo)
        print(f"{tipo.capitalize()} inválido! Deve ser um número inteiro.")

# Função para verificar duplicidade de código
def codigo_existe(nome_arquivo, chave, valor):
    dados = carregar_dados(nome_arquivo)
    return any(str(item.get(chave)) == str(valor) for item in dados)

# Função genérica para listar registros
def listar_registros(nome_arquivo, campos_exibir):
    registros = carregar_dados(nome_arquivo)
    if registros:
        for idx, item in enumerate(registros, 1):
            print(f"{idx}. " + ", ".join(f"{campo}: {item.get(campo, '')}" for campo in campos_exibir))
    else:
        print("Nenhum registro encontrado.")

# Função genérica para excluir registros
def excluir_registro(nome_arquivo):
    registros = carregar_dados(nome_arquivo)
    if not registros:
        print("Nenhum registro encontrado.")
        return

    listar_registros(nome_arquivo, registros[0].keys())
    try:
        idx = int(input("Digite o número do registro que deseja excluir: ")) - 1
        if 0 <= idx < len(registros):
            removido = registros.pop(idx)
            salvar_dados(nome_arquivo, registros)
            print(f"{removido} removido com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

# Função genérica para atualizar registros
def atualizar_registro(nome_arquivo, campos):
    registros = carregar_dados(nome_arquivo)
    if not registros:
        print("Nenhum registro encontrado.")
        return

    listar_registros(nome_arquivo, campos)
    try:
        idx = int(input("Digite o número do registro que deseja atualizar: ")) - 1
        if 0 <= idx < len(registros):
            for campo in campos:
                novo_valor = input(f"Novo valor para {campo} (deixe em branco para manter): ").strip()
                if novo_valor:
                    registros[idx][campo] = novo_valor
            salvar_dados(nome_arquivo, registros)
            print("Registro atualizado com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")
