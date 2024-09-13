def calcular_fatorial(n): # recebe um número inteiro e calcula o fatorial desse número usando o for
    fatorial = 1 # é iniciado com 1

    for i in range(1, n + 1): # para cada número de 1 até n, multiplicamos o valor atual do fatorial por esse número.

        fatorial *= i
    return fatorial

while True:
    numero = int(input("Digite um número inteiro positivo (ou -1 para sair): "))
    
    if numero == -1: # se o usuario digitar -1 um o programa exibe uma mensagem e encerra
        print("Programa encerrado.") 
        break
    
    if numero < 0:
        print("Número inválido! Por favor, digite um número inteiro positivo.") # se for digitado um numero negativo programa exibe uma mensagem de erro
        continue # volta ao início do loop para solicitar um novo número.
    
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}") # Se o número for válido, a função calcular_fatorial é chamada para calcular o fatorial do número inserido, e o resultado é exibido.s
