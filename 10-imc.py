print("Programa para cálculo de IMC")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("digite a sua altura (em metros): "))
imc = peso / (altura ** 2)

print(f"Seu IMc é {imc:.2f}.")
print("Classificação do IMC:")
if imc < 18.5:
    print("Abaixo do peso normal")
elif 18.5 <= imc < 25:
    print("Peso Normal")
elif 25 <= imc < 35:
    print("Sobrepeso.")
else:
    print("Obesidade")
    
