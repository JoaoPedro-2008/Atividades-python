def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Solicitar ao usuário que digite um ano
try:
    ano_usuario = int(input("Digite um ano: "))
    if eh_bissexto(ano_usuario):
        print(f"{ano_usuario} é um ano bissexto.")
    else:
        print(f"{ano_usuario} não é um ano bissexto.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")


