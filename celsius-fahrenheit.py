#celsius.fahrenheit.py = Escreva um programa que converta uma temperatura 
#Digitada em °C em °F
#A fórmula para essa conversão é:
#F = (C*9/5) +32

celsius = float(input("Digite a temperatura em  °C:"))
fahrenheit = 9* celsius /5 +32
print(f"{celsius:.2f}/C é igual a {fahrenheit:.2f}°F")