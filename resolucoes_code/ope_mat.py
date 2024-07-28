# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita ao usuário que insira o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que escolha a operação
operacao = input("Escolha a operação (adição, subtração, multiplicação, divisão): ").strip().lower()

# Realiza a operação escolhida e exibe o resultado
if operacao == "adição":
    resultado = num1 + num2
    print("Resultado da adição:", resultado)
elif operacao == "subtração":
    resultado = num1 - num2
    print("Resultado da subtração:", resultado)
elif operacao == "multiplicação":
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)
elif operacao == "divisão":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Escolha entre adição, subtração, multiplicação ou divisão.")
