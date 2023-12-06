

print("\n******************* Calculadora em Python *******************")

def soma(x, y):
    return num_1 + num_2

def subtração(x, y):
    return num_1 - num_2

def multiplicacao(x, y):
    return num_1 * num_2

def divisão(x, y):
    return num_1 / num_2

def potencia(x, y):
    return num_1 ** num_2 


print("\n Selecione o número da operação\n")
print("1- Adição")
print("2- Subtração")
print("3- Divisão")
print("4- Multiplicação")
print("5- Potència")
print("\n")


      
escolha = int(input("Escolha a operação(1 / 2 / 3 / 4 / 5 ): "))

num_1 = float(input("Insira o primeiro número:"))
num_2 = float(input("Insira o segundo número: "))

if escolha == float(1):
    print(num_1,"+",num_2,"=",soma(num_1, num_2))
    print("\n")

elif escolha == float(2):
    print(num_1,"-",num_2,"=",subtração(num_1, num_2))
    print("\n")

elif escolha == float(3):
    print(num_1,"x",num_2,"=",multiplicacao(num_1, num_2))
    print("\n")

elif escolha == float(4):
    print(num_1,"/",num_2,"=",divisão(num_1, num_2))
    print("\n")

elif escolha == float(5):
    print(num_1,"**",num_2,"=",potencia(num_1, num_2))
    print("\n")

else:
    print("Operação invalida")