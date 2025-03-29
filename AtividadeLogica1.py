def CalcularQuadrado():
    numero = int(input("Digite um número inteiro para descobrir seu quadrado: "))
    quadrado = numero * numero
    print("O quadrado do número que você inseriu é:", quadrado)

def CalcularSoma():
    soma1 = int(input("Digite um número inteiro: "))
    soma2 = int(input("Digite um segundo número inteiro: "))
    resultado = soma1 + soma2
    print("O resultado da soma dos dois números que você inseriu é:", resultado)

def CalcularIdade():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = 2024 - ano_nascimento
    print("Você tem:", idade, "anos")

def CalcularMedia():
    materia = input("Digite uma matéria escolar: ")
    nota1 = float(input("Digite sua nota no primeiro bimestre: "))
    nota2 = float(input("Digite sua nota no segundo bimestre: "))
    nota3 = float(input("Digite sua nota no terceiro bimestre: "))
    nota4 = float(input("Digite sua nota no quarto bimestre: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Sua média anual na matéria {materia} foi de: {media:.2f}")

def CalcularValor():
    produto = float(input("Qual o valor do produto que você comprou? "))
    quantidade = int(input("Quantas unidades você comprou? "))
    total = produto * quantidade
    print("O valor final da compra é de: R$", total)

def CalcularDesconto():
    produto = float(input("Qual o valor do produto que você comprou? "))
    quantidade = int(input("Quantas unidades você comprou? "))
    valor_compra = produto * quantidade
    desconto = 15 * valor_compra / 100
    valor_final = valor_compra - desconto
    print(f"O valor final da compra com 15% de desconto é de: R$ {valor_final:.2f}")

while True:
    print("\nEscolha uma opção:")
    print("1 - Calcular o quadrado de um número")
    print("2 - Calcular a soma de dois números")
    print("3 - Calcular idade")
    print("4 - Calcular média de matéria")
    print("5 - Calcular o valor da compra")
    print("6 - Calcular o valor da compra com 15% de desconto")
    print("7 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        CalcularQuadrado()
    elif escolha == "2":
        CalcularSoma()
    elif escolha == "3":
        CalcularIdade()
    elif escolha == "4":
        CalcularMedia()
    elif escolha == "5":
        CalcularValor()
    elif escolha == "6":
        CalcularDesconto()
    elif escolha == "7":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
