#Criação de um programa de calculo de IMC
#Utilizando a linguagem de programação Python.


#Começamops pedindo os valores de entrada para o usuario 
altura = float(input("Qual é a sua altura?: "))
peso = float(input("qual o seu peso em kg: "))
 #calculo  divide-se o peso (em kg) pelo quadrado da altura (em metros).
calculo_um = altura * altura 
calculo_dois = peso / calculo_um   
#Entao chamamos o print para mostrar o resultado na tela
# o metodo format, ajuda a reduzir o tamanho do numero final do calculo
# {:.4f} significa e a quantidade de numeros que vem depois do ponto. 
print ("Este é o IMC o seu IMC {:.4f}".format(calculo_dois) )

# Criar um relatório no final da atividade.


