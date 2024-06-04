# Usando for loop
for num in [-3, 0, 5, -8, 10]:
    if num > 0:
        print(num, "é positivo")
    elif num < 0:
        print(num, "é negativo")
    else:
        print(num, "é zero")
else:
    print("Loop for concluído.")

numeros = [-3, 0, 5, -8, 10]
index = 0
while index < len(numeros):
    num = numeros[index]
    if num > 0:
        print(num, "é positivo")
    elif num < 0:
        print(num, "é negativo")
    else:
        print(num, "é zero")
    index += 1
else:
    print("Loop while concluído.")
