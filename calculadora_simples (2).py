"""
CALCULADORA SIMPLES
"""

def mostrar_menu():
    print("Selecione a operação desejada:") # Função para mostrar o menu de operações
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

def calculadora():
    while True:
        mostrar_menu()  # Exibir o menu de operações

        operacao = input("Digite o número da operação (1/2/3/4) ou 'sair' para encerrar: ")  # Solicitar ao usuário que escolha uma operação

        if operacao.lower() == 'sair':  # Opção para sair do programa
            print("Saindo do programa...")
            break
        
        if operacao in ['1', '2', '3', '4']:  # Validar se a operação é válida
            try:
                num1 = float(input("Digite o primeiro número: "))  # Solicitar o primeiro número para o usuário
                num2 = float(input("Digite o segundo número: "))  # Solicitar o segundo número para o usuário
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
                continue

            if operacao == '1':  # Executar a operação escolhida
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacao == '4':
                if num2 != 0:  # Verificar se o segundo número é zero para evitar divisão por zero
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida!")
        else:  # Caso a operação seja inválida
            print("Operação inválida. Tente novamente.")

# Executar a calculadora
calculadora() 
