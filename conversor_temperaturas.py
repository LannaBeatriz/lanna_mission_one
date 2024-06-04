class Temperatura:
    def __init__(self):
        pass

converter = input("Se você deseja converter de Fahrenheit para Celsius, digite 1. Se você deseja converter de Celsius para Fahrenheit, digite 2:\n")

if converter == "1":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit:\n"))
    celsius = (fahrenheit - 32) * 5/9
    print(f"A temperatura convertida é {celsius:.2f} graus Celsius.")
elif converter == "2":
    celsius = float(input("Digite a temperatura em Celsius:\n"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura convertida é {fahrenheit:.2f} graus Fahrenheit.")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")