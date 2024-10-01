def inicio():
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    
    print("\n1 - Para Adição")
    print("2 - Para Subtração")
    print("3 - Para Multiplicação")
    print("4 - Para Divisão")
    o = int(input("Sua opção é: "))
    
    if o == 1:
        print("\nO resultado é:", n1 + n2)
    elif o == 2:
        print("\nO resultado é:", n1 - n2)
    elif o == 3:
        print("\nO resultado é:", n1 * n2)
    elif o == 4:
        if n2 != 0:  # Verifica se n2 não é zero para evitar divisão por zero.
            print("\nO resultado é:", n1 / n2)
        else:
            print("\nErro: Divisão por zero não é permitida.")
    else:
        print("\nOpção inválida.")


inicio()

