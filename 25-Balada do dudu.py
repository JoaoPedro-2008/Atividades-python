# Solicitando a idade do usuário
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você está liberado para entrar na balada.")
else:
    if idade >= 16:
        autorizacao = input("Você tem autorização dos pais? (S/N): ")
        if autorizacao.upper() == "S":
            print("Você está liberado para entrar na balada.")
        else:
            print("Você não está liberado para entrar na balada.")
    else:
        print("Você não está liberado para entrar na balada.")
