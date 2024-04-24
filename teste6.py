def calcular_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma


numeros = [16, 21, 46, 79]




while True:
    try:
        entrada = input("Digite um número: ")
        if entrada.lower() == 'fim':
            break
        numeros.append(float(entrada))
    except ValueError:
        print("Por favor, digite apenas números.")




    try:
        soma_total = calcular_soma(numeros)
        print("A soma dos números é:", soma_total)
    except:
        print("Ocorreu um erro ao calcular a soma.")


