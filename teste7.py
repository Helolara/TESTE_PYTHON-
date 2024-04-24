def calcular_media(lista):
    if not lista:
        raise ValueError("A lista está vazia.")
    return sum(lista) / len(lista)

valores = [5, 12, 19, 25, 30]


try:
    media = calcular_media(valores)
    print("A média dos valores é:", media)
except ZeroDivisionError:
    print("A lista está vazia. Não é possível calcular a média.")
except ValueError as e:
    print(e)


