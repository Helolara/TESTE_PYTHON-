numero = int(input("Digite um número para ver sua tabuada: "))

print("Tabuada de", numero, ":")
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
