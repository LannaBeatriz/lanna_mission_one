# Usando for loop
for num in range(1, 6):
    if num % 2 == 0:
        print(num, "é par")
    else:
        print(num, "é ímpar")
else:
    print("Loop for concluído.")

num = 1
while num <= 5:
    if num % 2 == 0:
        print(num, "é par")
    else:
        print(num, "é ímpar")
    num += 1

else:
     print("Loop while concluído.")