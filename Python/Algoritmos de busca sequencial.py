#Algoritmos de busca sequencial
# while 
def busca_sequencial(lista, elemento):
     pos = 0 
     encontrado = False

 # A estrutura de repetição “while” permitirá percorrer a lista e comparar o elemento 
 # procurado com o elemento que está na posição da lista, nesse caso, enquanto a posição 
 # for menor que o tamanho da lista e o elemento não for encontrado.    
     while pos < len(lista) and not encontrado:

 #Na estrutura condicional “if”, “else” traz a condição para encontrar 
 # ou não o elemento do vetor – no caso, se a posição da lista corresponde ao elemento procurado (valor), 
 # será exibido True (verdadeiro), se não corresponder, haverá um incremento e o próximo elemento será visitado na sequência da lista.         
          if lista[pos] == elemento:
               encontrado = True
          else:
              pos = pos+1
  
          return encontrado
   
testelista = [2, 10, 8, 15, 18, 20, 12, 1] #é mostrado um vetor com 8 elementos (0 a 7 elementos).
 
print(busca_sequencial(testelista, 5)) # é buscado o elemento 5 na lista 
                                       #Como o elemento não está na lista, observe que todas posições serão percorridas, 
                                       #razão pela qual todos os elementos da lista serão visitados.


print(busca_sequencial(testelista, 15)) #busca o elemento de valor 15. Nesse caso, quatro
                                        #elementos da lista serão percorridos até que se encontre o valor 15.

#OBS ponto de teste(Breakpont), foram colocados para observar como o codigo funciona! 