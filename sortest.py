# Início do estudo dos tipos de sort
lista = [5, 3, 2, 4, 7, 1, 0, 6, 6, 9, 8, 10]
# Bubble Sort


def bubblesort(lista):

    if len(lista) == 0:
        return []
    for i in range(len(lista)-2):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
    return bubblesort(lista[0:(len(lista)-1)]) + [lista[-1]]

# Selection Sort


def selectionsort(lista):
    if len(lista) == 0: return []
    mini = min(lista)
    lista.remove(mini)
    return [mini] + selectionsort(lista)

print(selectionsort(lista))


