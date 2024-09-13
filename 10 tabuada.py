def imprimir_tabuada(numero):
    # Função para imprimir a tabuada de um número de 1 a 10
    for i in range(1, 11):  # Loop de 1 a 10
        print(f"{numero} x {i} = {numero * i}")  # Imprime o resultado da multiplicação

def main():
    try:
        numero = int(input("Digite um número maior que 0 para ver a tabuada: "))  # Solicita o número ao usuário e converte para inteiro
    except ValueError:
        print("Por favor, digite um número válido.")  # Mensagem de erro se a entrada não for um número
        return  # Encerra a função principal

    if numero > 0:  # Verifica se o número é maior que 0
        imprimir_tabuada(numero)  # Chama a função para imprimir a tabuada
    else:
        print("O número deve ser maior que 0.")  # Mensagem de erro se o número não for maior que 0

# Executa o programa chamando a função principal
main()
