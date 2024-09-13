while True:  # Loop infinito para continuar perguntando até o usuário decidir parar
    idade = input("Digite a idade da pessoa (ou 'sair' para encerrar): ")  # Pede a idade ou um comando para sair

    if idade.lower() == 'sair':  # Verifica se o usuário digitou 'sair' para encerrar o programa
        print("Encerrando o programa...")
        break  # Sai do loop

    try:
        idade = int(idade)  # Tenta converter a entrada para um número inteiro
    except ValueError:
        print("Por favor, insira um número válido ou 'sair' para encerrar.")  # Mensagem de erro se não for número
        continue  # Volta ao início do loop para pedir nova entrada

    if idade < 18:  # Verifica se a pessoa é menor de idade
        print("Menor de idade")
    elif 18 <= idade < 60:  # Verifica se a pessoa é adulta
        print("Adulto")
    else:  # Se a idade for 60 ou mais, a pessoa é considerada idosa
        print("Idoso")