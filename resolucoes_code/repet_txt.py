# Vamos solicitar como entrada uma string e um número e repetir essa string tantas vezes quanto indicado pelo número.

# Solicita ao usuário que insira uma string
texto = input("Digite uma string: ")

# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Repite a string o número de vezes indicado
resultado = (texto + ' ')* numero

# Exibe o resultado
print("Resultado:", resultado)
