def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def Multiplicacao(x, y):
    return x * y

def Divisao(x, y):
    return x / y


num1 = int(input("dugite o primeiro numeto: "))
num2 = int(input("dugite o segundo numeto: "))

escolha = input("Escolha a operação (soma, subtracao, multiplicacao, divisao): ")

if escolha == "soma":
    resultado = soma(num1, num2)
    print("O resultador da soma é: ", resultado)
elif escolha == "subtracao":
    resultado = subtracao(num1, num2)
    print("O resultado da subtracao é ", resultado)
elif escolha == "multiplicacao":
    resultado = Multiplicacao(num1, num2)
    print("O resultado da multiplicacao é: ", resultado)
elif escolha == "divisao":
    resultado = Divisao(num1, num2)
    print("O resultado da divisao é: ", resultado)
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
    