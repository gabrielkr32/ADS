#lgoritmo de busca binária com utilização do mesmo vetor 
def buscar_binario(lista, elemento):
    minimo = 0
    maximo = len(lista) -1 
    encontrado = False



# A estrutura de repetição “while”, que será executada 
# enquanto o primeiro elemento da lista (mínimo) for menor ou igual 
# ao máximo (último elemento) e o elemento procurado não for encontrado.
    while minimo <= maximo and not encontrado:
        meio_lista =(minimo + maximo) // 2 #identificamos o índice associado à metade da lista.

#temos uma estrutura de condição “if” em razão da qual, basicamente, verifica-se que, se o elemento do meio da lista for o valor procurado, será retornado o True         
        if lista [meio_lista] == elemento:  
            encontrado = True

        else:#temos a condição “else”, que verifica se o elemento 
            #procurado é menor que o valor do meio da lista. 
            # #Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada); 
            # se não for, a busca acontecerá na metade inferior da sequência (a superior é descartada).
            if elemento < lista[meio_lista]:
                maximo = meio_lista -1 

            else:
                minimo = meio_lista +1

    return encontrado 


teste_lista = [1, 2, 8, 10, 13, 15, 18, 20]
print(buscar_binario(teste_lista, 5))
print(buscar_binario(teste_lista, 15))
