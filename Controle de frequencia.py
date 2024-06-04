def controle_de_frequência(idade): 
    if idade >= 18: 
        print("Entrada Liberada.")
    else: 
        print("Não é permetido a entrada de menores de 18.")

idade_visitante = int(input("Informe a sua idade: "))
controle_de_frequência(idade_visitante)