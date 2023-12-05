#Busca sequencial em um vetor ordenado
#while 

def busca_sequencial_ordenada(lista, elemento):
    pos = 0
    encontrado = False 
    para = False

    while pos <len(lista) and not encontrado and not para:
        if lista[pos] == elemento:
            encontrado = True
        else:
            if lista[pos] > elemento:
                para = True
            else:
                pos = pos +1
    
    return encontrado

teste_lista = [1,2,8,10,13,15,18,20]
print(busca_sequencial_ordenada(teste_lista,5))
print(busca_sequencial_ordenada(teste_lista, 15))                 