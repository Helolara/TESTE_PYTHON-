numeros = [5, 16, 41, 57, 66]


# processo de soma
soma = 0


# calcular
try:
    for numero in numeros:
        soma += numero
except Exception as e:
    print("Ocorreu um erro:", e)
else:
    print("A soma dos elementos é:", soma)
