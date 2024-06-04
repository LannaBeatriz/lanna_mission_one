# Função para verificar se um número é primo
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Digite o início do intervalo: "))
end = int(input("Digite o final do intervalo: "))

print("Números primos no intervalo de", start, "a", end, ":")

for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=" ")
print("\nLoop for concluído.")

print("\nNúmeros primos no intervalo de", start, "a", end, "usando while loop:")
num = start
while num <= end:
    if is_prime(num):
        print(num, end=" ")
    num += 1
print("\nLoop while concluído.")
