# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Função principal
def main():
    try:
        # Entrada de dados
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))

        # Verificação básica para evitar divisão por zero
        if altura <= 0:
            print("A altura deve ser um valor positivo.")
            return
        
        # Cálculo do IMC
        imc = calcular_imc(peso, altura)

        # Classificação do IMC
        classificacao = classificar_imc(imc)

        # Exibição do resultado
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")

# Execução do programa
if __name__ == "__main__":
    main()
    