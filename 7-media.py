def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Lista para armazenar os números
numeros = []

# Solicitar ao usuário que digite os números
while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

# Calcular e exibir a média
media = calcular_media(numeros)
print(f"A média aritmética dos números digitados é: {media:.2f}")
