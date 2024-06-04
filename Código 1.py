numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
i = 0
for i in range(5):
    print("Este é o passo", i + 1, "do loop for.")

contador = 0
while contador < 3:
    print("Este é o passo", contador + 1, "do loop while.")
    contador += 1
else:
    print("Loop while concluído.")
