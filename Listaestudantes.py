# Projeto - > Lista de Estudantes
# Feito pela - > Melissa Cristina Cardoso
# Matéria - > Raciocinio Computacional
# Curso - > Analise em Desenvolvimento de Sistemas


########### Lógica ############


import json # importa e biblioteca python que permite o uso de json, que vai servir para armazenar os dados

arquivo_json = "estudantes.json" #nome do arquivo json onde os dados serão armazenados

#serve pra carregar os dados que estão salvos no json
def carregar_dados():
    try:
        with open(arquivo_json, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

#serve pra salvar os novos dados ou alterações no json
def salvar_dados(estudantes):
    with open(arquivo_json, "w", encoding="utf-8") as file:
        json.dump(estudantes, file, indent=4, ensure_ascii=False)




# a 'def' abaixo está armazenando as informações que serão mostradas no terminal para o menu principal
def menu_principal():
    print("\n***** [MENU PRINCIPAL] *****")  # mostra o menu principal
    print("\n1 - Estudantes")  # essa opção  acessa o menu de estudantes
    print("2 - Disciplinas")  # essa opção  acessa o menu de disciplinas
    print("3 - Professores")  # essa opção  acessao menu de professores
    print("4 - Turmas")  # essa opção  acessa o menu de turmas
    print("5 - Matrículas")  # essa opção  acessa o menu de matrículas
    print("9 - Sair")  # essa opção serve para sair do sistema
    
# essa 'def' está armazenando as informações que serão mostradas no terminal para o que ffor executado dentro do menu de estudantes
def exibir_informacoes():
    print("\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****")
    print("\n1 - Incluir")  # opção para incluir um estudante
    print("2 - Listar")  # opção para listar estudantes cadastrados
    print("3 - Atualizar")  # opção para atualizar os dados de um estudante
    print("4 - Excluir")  # opção para excluir um estudante
    print("9 - Voltar ao menu principal")  # opção para voltar ao menu principal
    

    
   
 
def validar_nome():
    while True:
        nome = input("Digite o nome do estudante: ").strip()  
        if nome.replace("  ", " ").isalpha():  # logica que permite espaço entre as palavras
            return nome
        print("Nome invalido! Digite apenas letras.")


    
def validar_idade():
    while True:
        idade = input("Digite a idade do estudante:  ").strip()
        if idade.isdigit() and 1 <= int(idade) <= 99: #logica para que a idade seja valida e existente
            return idade
        print("Idade invalida! Digite um número entre 1 e 99.")

def validar_matricula():
    while True:
        matricula = input("Digite a matricula do estudante (maximo 8 caracteres, apenas números):  ").strip()
        if matricula.isdigit() and 1 <= len(matricula) <= 8: #faz uma logicazinha pra matricula ter um jeito especifico
            return matricula
        print("Matricula invalida! Deve conter no máximo 8 dígitos, sendo válido apenas números.")

   


# função para armazenar os dados e a lógica que vai coletar o nome do estudante
def IncluirEstudante():
    estudantes = carregar_dados()

    nome = validar_nome()
    idade = validar_idade()
    matricula = validar_matricula()


#meio que define o modo que o dado fica salvo no arquivo json
    estudante = {
    
        "nome": nome,
        "idade": idade,
        "matricula": matricula
    }
    
    estudantes.append(estudante)
    salvar_dados(estudantes)
    print("Estudante", nome, "que tem ", idade, " anos, e a matricula registrada como: ", matricula,   "cadastrado com Sucesso!")  # mostra uma mensagem confirmando a inclusão do estudante
     
     
     
# função para armazenar os dados e a lógica que vai mostrar os estudantes que foram adicionados anteriormente
def ListarEstudante():
    estudantes = carregar_dados()
    if estudantes:  # verifica se há estudantes cadastrados
        print("\nLista de Estudantes:")
        for idx, estudante in enumerate(estudantes, 1):  #meio que puxa as informações do json
            print(f"{idx}. Nome: {estudante['nome']}, Idade: {estudante['idade']}, Matrícula: {estudante['matricula']}")
    else:
        print("\nNenhum estudante foi incluído anteriormente")  # exibe uma mensagem caso não haja estudantes cadastrados

#função para editar os dados do estudante
def EditarEstudante():
    estudantes = carregar_dados()
    if not estudantes:
        print("\nNenhum estudante cadastrado para excluir.")
        return
    
    ListarEstudante()
    try:
        idx = int(input("\nDigite o numero do estudante que deseja alterar os dados:  ")) -1
        if 0  <= idx < len(estudantes):
            estudantes[idx]["nome"] = input("Novo nome: ") or estudantes[idx]["nome"]
            estudantes[idx]["idade"] = input("Nova Idade:") or estudantes[idx]["idade"]
            estudantes[idx]["matricula"] = input("Nova matricula: ") or estudantes[idx]["matricula"]
            salvar_dados(estudantes)
            print("Dados do estudante alterados com sucesso!")
            
        else: print("Estudante invalido")  
    except: print("Numero do estudante invalido! Digite um numero valido")  
    
    
def RemoverEstudantes():
    estudantes = carregar_dados()
    if not estudantes:
        print("Nenhum estudante encontrado!")
        return
    
    ListarEstudante()
    try:
        idx = int(input("\nDigite o número do estudante que deseja excluir: ")) - 1 
        if 0 <= idx < len(estudantes):
            estudante_removido = estudantes.pop(idx) #isso aqui remove o estudante do arquivo json
            salvar_dados(estudantes)
            print(f"Estudante {estudante_removido['nome']} Removido com sucesso!")
        else: print("Estudante invalido")  
    except ValueError: 
        print("Numero do estudante invalido! Digite um numero valido")      
  
    
    
    
# função principal do programa que controla a navegação entre os menus
def main():
    while True:  # o while é usado para criar a estrutura de navegação do menu principal
        menu_principal()  # chama a função que exibe o menu principal
        opcao_principal = input("\nEscolha uma opção: ")  # solicita ao usuário que escolha uma opção

        if opcao_principal == "1":  # se o usuário escolher "1", entra no menu de estudantes
            while True:  # cria um loop para navegar dentro do menu de operações dos estudantes
                exibir_informacoes()  # chama a função que exibe o menu de operações
                opcao = input("\nEscolha uma opção: ")  # solicita ao usuário que escolha uma operação

                if opcao == "1":  # se a opção for "1", chma a função para incluir estudante
                    IncluirEstudante()
                elif opcao == "2":  # se a opção for "2", chama a função paRa listar estudantes
                    ListarEstudante()
                elif opcao == "3":  # se a opção for "3, chama a função para editar estudantes
                    EditarEstudante()
                elif opcao == "4": # se a opção for "4, chama a função para de exluir estudantes
                    RemoverEstudantes ()   
                elif opcao == "9":  # se a opção for "9", volta para o menu principal
                    break  
                else:
                    print("opção invalida! Tente novamente.")  # exibe uma mensagem caso a opção seja invalida

       
        elif opcao_principal == "9":  # se o usuário escolher "9", o programa se encerra
            print("\nSaindo do sistema...")
            break

        else:
            print("\nopção invalida! Tente novamente.")  # exibe uma mensagem caso a opção seja invalida

if __name__ == "__main__":
    main()  # chama a função principal do programa, garantindo que o código execute corretamente  
