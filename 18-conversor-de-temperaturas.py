def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def menu():
    print("\nMenu de Conversão de Temperaturas")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")
    print("7. Sair")
    
def main():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-7): ")
        
        if escolha == '7':
            print("Saindo do programa.")
            break
        
        if escolha in ['1', '2', '3', '4', '5', '6']:
            temperatura = float(input("Digite a temperatura: "))
            
            if escolha == '1':
                resultado = celsius_to_fahrenheit(temperatura)
                print(f"{temperatura:.2f}°C = {resultado:.2f}°F")
                
            elif escolha == '2':
                resultado = celsius_to_kelvin(temperatura)
                print(f"{temperatura:.2f}°C = {resultado:.2f}K")
                
            elif escolha == '3':
                resultado = fahrenheit_to_celsius(temperatura)
                print(f"{temperatura:.2f}°F = {resultado:.2f}°C")
                
            elif escolha == '4':
                resultado = fahrenheit_to_kelvin(temperatura)
                print(f"{temperatura:.2f}°F = {resultado:.2f}K")
                
            elif escolha == '5':
                resultado = kelvin_to_celsius(temperatura)
                print(f"{temperatura:.2f}K = {resultado:.2f}°C")
                
            elif escolha == '6':
                resultado = kelvin_to_fahrenheit(temperatura)
                print(f"{temperatura:.2f}K = {resultado:.2f}°F")
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
