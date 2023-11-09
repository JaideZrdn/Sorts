# Início do estudo dos tipos de sort
# Autor: Jaide Zardin
lista = [5, 3, 2, 4, 7, 1, 0, 6, 6, 9, 8, 10]
# Bubble Sort


def bubble_sort(lista):

    if len(lista) == 0:
        return []
    for i in range(len(lista)-2):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
    return bubble_sort(lista[0:(len(lista)-1)]) + [lista[-1]]

# Selection Sort


def selection_sort(lista):

    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Insertion Sort


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j>=0 and lista[j]>chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    return lista

# Merge Sort


def merge_sort(lista):
    if len(lista) <= 1: return lista
    def intercala(xs, ys):
        if len(xs) == 0 or len(ys) == 0: return xs+ys
        elif xs[0]<ys[0]: return [xs[0]] + intercala(xs[1:], ys)
        else: return [ys[0]] + intercala(xs, ys[1:])
    meio = len(lista)//2
    n = merge_sort(lista[:meio])
    m = merge_sort((lista[meio:]))
    return intercala(m, n)

# Quick Sort


def quick_sort(lista):

    if len(lista) <= 1: return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


