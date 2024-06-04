quantidade_de_itens = int(input("Digite a quantidade de itens: "))
valor_total = float(input("Digite o valor total da compra: "))

if quantidade_de_itens > 5 or valor_total > 200:
    desconto = 0.1 * valor_total  # Supondo um desconto de 10%
    print("Parabéns! Você recebeu um desconto de", desconto, "reais.")
else:
    print("Desculpe, você não é elegível para um desconto.")
