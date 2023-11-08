# Sorts
## Repositório para o estudo dos tipos de sort 
### O que é um sort?
Um sort, é um algoritmo usado para organizar listas, de forma que os elementos fiquem em ordem crescente ou decrescente.

### Tipos de sort
Neste repositório, desenvolverei os algoritmos e conceitos de 8 tipos de sort de maneira recursiva sempre que possível, sendo eles:
- [Bubble Sort][minha-ancora] 
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Counting Sort
- Radix Sort


1. **Bubble Sort** <a name="minha-ancora"></a>

Ele consiste num algoritmo que troca os elementos adjacentes até que toda a lista esteja ordenada.
Basicamente, ele compara o elemento atual com o próximo, caso o at
ual seja menor a lista permanecerá do jeito que está, caso contrário, eles trocam de lugar.
Esse processo é repetido várias vezes e cada vez ele deixa de comparar com o último elemento da lista, visto que ele
sempre será maior que todos os antecedentes.

Apesar de simples, ele acaba não sendo muito eficiente do ponto de vista computacional, limitando o uso deles para listas
pequenas.

Na função feita em python, eu fiz uma definição recursiva do bubble sort, porém, 
com o mesmo funcionamento.

Nessa parte do código, eu inverto os elementos caso o atual seja maior que o próximo, caso contrário, ele vai direto para a 
próxima iteração e após isso a definição recursiva é chamada.
```python
if lista[i] > lista[i+1]:
    lista[i], lista[i+1] = lista[i+1], lista[i]
```

2. **Selection Sort**

O selection sort é um algoritmo que percorre toda a lista, procurando o menor elemento e o colocando na primeira posição.
Repetindo isso para todos os elementos, a lista fica ordenada.

Vantagens: Muito simples de desenvolver, fácil de entender e implementar; Uso muito baixo de memória e Desempenho Constante.

Desvantagens: Muito ineficiente para listas grandes.

Nesta parte do código eu procuro o menor elemento da lista e o removo, após isso, eu chamo a definição recursiva da função
```python
mini = min(lista)
lista.remove(mini)
return [mini] + selection_sort(lista)
```

