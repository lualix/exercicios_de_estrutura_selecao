# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Inicia o loop para percorrer todos os números de 1 até o número inserido
for i in range(1, numero + 1):
    # Verifica se o número atual é par
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        # Se não for par, então é ímpar
        print(f"{i} é ímpar")
