def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro positivo: "))

if is_prime(numero):
    print(numero, "é um número primo.")
elif numero == 0:
    print("O número é zero.")
else:
    print(numero, "não é um número primo.")

for i in range(1, 6):
    if i % 2 == 0:
        print(i, "é par.")
    elif i % 2 != 0:
        print(i, "é ímpar.")
else:
    print("Loop for concluído.")

contador = 0
while contador < 3:
    if contador % 2 == 0:
        print("Este é um passo par do loop while.")
    elif contador % 2 != 0:
        print("Este é um passo ímpar do loop while.")
    contador += 1
else:
    print("Loop while concluído.")
