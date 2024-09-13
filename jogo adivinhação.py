import random  # Importa o módulo random para gerar números aleatórios

def jogo_adivinhacao():
    """
    Função para o jogo de adivinhação onde o usuário tem até 5 tentativas para adivinhar um número.
    """
    numero_secreto = random.randint(1, 50)  # Escolhe um número aleatório entre 1 e 50
    tentativas = 5  # Define o número máximo de tentativas

    print("Bem-vindo ao jogo de adivinhação!")  # Mensagem de boas-vindas
    print("Eu escolhi um número entre 1 e 50.")  # Informa o intervalo dos números
    print("Você tem 5 tentativas para adivinhar o número.")  # Informa o número de tentativas

    while tentativas > 0:  # Loop enquanto o usuário ainda tem tentativas
        try:
            palpite = int(input("Digite seu palpite: "))  # Recebe o palpite do usuário

            if palpite < 1 or palpite > 50:  # Verifica se o palpite está dentro do intervalo permitido
                print("Por favor, escolha um número entre 1 e 50.")  # Mensagem de erro
                continue  # Pede um novo palpite

            if palpite < numero_secreto:  # Verifica se o palpite é menor que o número secreto
                print("O número é maior que o seu palpite.")  # Informa que o número é maior
            elif palpite > numero_secreto:  # Verifica se o palpite é maior que o número secreto
                print("O número é menor que o seu palpite.")  # Informa que o número é menor
            else:  # Caso o palpite esteja correto
                print(f"Parabéns! Você acertou o número {numero_secreto}!")  # Mensagem de vitória
                break  # Encerra o loop

            tentativas -= 1  # Reduz o número de tentativas restantes
            if tentativas > 0:  # Verifica se ainda há tentativas restantes
                print(f"Você ainda tem {tentativas} tentativas.")  # Informa o número de tentativas restantes
            else:  # Caso não haja mais tentativas
                print(f"Você perdeu! O número era {numero_secreto}.")  # Mensagem de perda

        except ValueError:  # Captura erro caso a entrada não seja um número válido
            print("Por favor, digite um número válido.")  # Mensagem de erro para entrada inválida

# Executa o jogo apenas se o script for executado diretamente
if __name__ == "__main__":
    jogo_adivinhacao()
