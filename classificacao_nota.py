def calcular_media(notas):
    return sum(notas) / len(notas) # recebe uma lista de notas e retorna a média dessas notas.

def classificar_aluno(media): # recebe a média de um aluno e retorna a classificação dele 
    if media >= 7: # se a media for igual a 7 ou maior
        return "Aprovado"
    elif media >= 5: # se a media for igual ou ate 6.9
        return "Recuperação"
    else: # se for menor que 5
        return "Reprovado"

while True:
    notas = []
    while True:
        nota = float(input("Digite a nota do aluno (ou -1 para finalizar): ")) 
        if nota == -1:
            break # se digitado um numero negativo o codigo para
        notas.append(nota)
    
    if not notas:
        print("Nenhuma nota inserida. Encerrando o programa.") # se nenhuma nota for inserida o programa exibe uma mensagem e encerra.
        break
    
    media = calcular_media(notas) # calcula a média das notas inseridas
    classificacao = classificar_aluno(media)
    
    print(f"Média do aluno: {media:.2f}") # exibe a média
    print(f"Classificação: {classificacao}") # exibe a classificacao
    
    continuar = input("Deseja inserir notas de outro aluno? (s/n): ").lower() # pergunta ao usuario se deseja inserir mais notas
    if continuar != 's': # se a respostas for s continua
        break # se nao encerra