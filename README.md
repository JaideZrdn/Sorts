# Sorts
## Estudando e entendendo alguns algoritmos de ordenação
### O que é um sort?
Um sort, é um algoritmo usado para organizar listas, de forma que os elementos fiquem em ordem crescente ou decrescente.

### Tipos de sort
Neste repositório, desenvolverei os algoritmos e conceitos de 5 tipos de sort sendo eles:
- [Bubble Sort](#a1) 
- [Selection Sort](#a2)
- [Insertion Sort](#a3)
- [Merge Sort](#a4)
- [Quick Sort](#a5)

1. **Bubble Sort** <a name="a1"></a>

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

2. **Selection Sort** <a name="a2"></a>

O selection sort é um algoritmo que percorre toda a lista, procurando o menor elemento e o colocando na primeira posição.
Repetindo isso para todos os elementos, a lista fica ordenada.

As vantagens do Selection Sort são, muito simples de desenvolver, fácil de entender e implementar, uso muito baixo de memória  e desempenho constante.
Porém, ele é muito ineficiente para listas grandes.

3. **Insertion Sort** <a name="a3"></a>

O Insertion Sort é um algoritmo que percorre uma lista de elementos da esquerda para a direta.
Durante essa passagem, ele seleciona um elemento eo compara com os seus anteriores, caso o anterior seja maior que ele
ele moverá uma casa para direita e assim sucessivamente até que o elemento seja inserido na posição correta.

Essa passagem à direita é feita da seguinte maneira:
```python
while j >= 0 and lista[j] > chave:
    lista[j+1] = lista[j]
    j -= 1
```
Basicamente o que está escrito é que enquanto o elemento aneterior (j) for maior que a nossa chave, ele vai para a posição seguinte (j+1).

4. **Merge Sort** <a name="a4"></a>

O Merge Sort consiste em basicamente dividir uma lista em sublistas até
que cada sublista tenha apenas um elemento, depois disso ele junta as sublistas fazendo
uma intercalação ordenada.

Para definíla de maneira recursiva, eu defini uma função que intercala duas listas já ordenadas, após isso, defini a função __merge_sort__
de maneira recursiva.
```python
 def intercala(xs, ys):
        if len(xs) == 0 or len(ys) == 0: return xs+ys
        elif xs[0]<ys[0]: return [xs[0]] + intercala(xs[1:], ys)
        else: return [ys[0]] + intercala(xs, ys[1:])
```
Após isso, fazemos a intercalação do merge sort da parte da diretita com o da parte da esquerda.

O Merge Sort é bom para casos longos pois apresenta uma boa constância de tempo, porém, ele não é muito eficiente para casos pequenos.

5. **Quick Sort** <a name="a5"></a>

O Quick Sort é um dos mais famosos algoritmos de ordenação, ele é conceituado 
como um algoritmo de divisão e conquista, pois, ele divide a lista em duas partes,
as com os elementos menores que o pivô e as com os elementos maiores que o pivô.
Após isso, ele ordena as duas partes de maneira recursiva.

O Quick Sort em geral é muito eficiente, porém, ele pode ser muito ineficiente em alguns casos, como por exemplo, quando a lista já está parcialmente ordenada.


