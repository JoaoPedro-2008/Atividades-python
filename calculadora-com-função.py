def obter_numero(mensagem):
    return int(input(mensagem))  # Função para obter um número do usuário.

def mostrar_opcoes():
    print("\n1 - Para Adição")
    print("2 - Para Subtração")
    print("3 - Para Multiplicação")
    print("4 - Para Divisão")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 != 0:  # Verifica se n2 não é zero.
        return n1 / n2
    else:
        return "Erro: Divisão por zero não é permitida."

def calcular():
    n1 = obter_numero("Informe o primeiro número: ")
    n2 = obter_numero("Informe o segundo número: ")
    
    mostrar_opcoes()
    o = int(input("Sua opção é: "))
    
    if o == 1:
        resultado = somar(n1, n2)
    elif o == 2:
        resultado = subtrair(n1, n2)
    elif o == 3:
        resultado = multiplicar(n1, n2)
    elif o == 4:
        resultado = dividir(n1, n2)
    else:
        resultado = "Opção inválida."
    
    print("\nO resultado é:", resultado)


calcular()
