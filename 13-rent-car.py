#Variaveis
dias_locados = int(input("Dias alugados: "))
km_percorridos = float(input("Quantos km foram percorridos: "))

#Calculo do preco total
total = (dias_locados*60)+(km_percorridos*0.15)
print(f"O valor total a pagar é r${total:.2f}")
