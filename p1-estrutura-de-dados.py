import time # importando a biblioteca de tempo para cronometrar o tempo de execução
import matplotlib.pyplot as plt # importando a biblioteca matplotlib para criar o gráfico

# criando uma lista de listas para representar uma matriz
elementos = [[0,1,2,3], [11,12,13,4], [10,15,14,5], [9,8,7,6]] # Listas solicitadas no exercício
elementos2 = elementos[0] + elementos[1] + elementos[2] + elementos[3] # Soma todos as sublistas e junta em uma única

lista_crescente = [] # Criando uma lista crescente
lista_decrescente = [] # Criando uma lista decrescente
tempos = [] # Criando uma lista vazia para armazenar o tempo cronometrado

for n in elementos2:
    # medindo o tempo de execução do algoritmo de ordenação crescente
    start = time.perf_counter() # Inicia a cronometragem
    lista_crescente.append(n) # Adiciona os itens a lista lista_crescente
    lista_crescente.sort() # Organiza a lista em ordem crescente
    # medindo o tempo de execução do algoritmo de ordenação decrescente
    lista_decrescente.append(n) # Adiciona os itens a lista lista_decrescente
    lista_decrescente.sort(reverse=True) # Organiza a lista em ordem decrescente
    end = time.perf_counter() # Finaliza a cronometragem
    # calculando o tempo total de execução e adicionando-o à lista de tempos
    tempo = end - start # Cálculo de eficiencia do código
    tempos.append(tempo) # Adiciona o resutlado a lista Tempo

# imprimindo as listas ordenadas
print(lista_crescente) # Imprime a lista crescente
print(lista_decrescente) # Imprime a Lista decrescente

# plotando os gráficos de tempo versus tamanho da lista para cada algoritmo
plt.plot(lista_crescente, tempos) # Adiciona os itens a tabela de forma crescente
plt.plot(lista_decrescente, tempos) # Adiciona os itens a tabela de forma descrescente
plt.xlabel('Tamanho da lista') # Escreve um texto na posição x da tabela
plt.ylabel('Tempo (segundos)') # Escreve um texto na posição y da tabela
plt.title('Notação Big O') # Adiciona um titulo a tabela
plt.show() # Imprime a tabela

# O GRUPO ESTÁ DEVENDO 1 PALHA ITÁLIANA PARA GABRIEL SOUZA E JOÃO FRANÇA

