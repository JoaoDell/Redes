
#Esse código é um teste de modelagem de uma rede de difusão de massa em um sistema simples
#Para que um sistema seja de difusão, é necessário que, principalmente:

#- A somatória das massas no final do tempo rodado deve ser igual à somatória inicial
#- A matriz de adjacência deve ser composta por elementos <=1, por se tratar de uma rede de difusão
#- A somatória das colunas da matriz de adjacência deve ser <=1
#- As linhas n da matriz dizem respeito a quanto o elemento n transfere sua massa para os outros elementos  


Rede = [0,0,1,0] #Essa linha inicializa os elementos do sistema, com o terceiro elemento com massa 1

M = [[0.3,0.40,0,0.50],[0.1,0,0.5,0.50],[0,0.30,0,0],[0.6,0.30,0.5,0]] #Essa linha inicializa a matriz de adjacência do sistema

print("Quantos segundos irão passar?")
iter = int(input()) #Aqui se escolhe quantos segundos o sistema irá realizar as trocas de massa
print(" ")

print("A massa no tempo t = 0s é:")
print("[" + ', '.join(str(Rede[u]) for u in range(len(Rede) - 1)) + ", " + str(Rede[-1]) + "]") #Se printa a massa no tempo t = 0s
print(" ")

for l in range(iter): 
    for i in range(len(Rede)):
        for j in range(len(Rede)):
            Rede[i] += M[i][j]*Rede[j] #Se adiciona a quantidade de massa do elemento receptor
            Rede[j] -= M[i][j]*Rede[j] #Se tira a quantidade de massa do elemento que ofereceu
    print("A massa no tempo t = " + str(l + 1) + "s" + " é:")
    print("[" + ', '.join(str(Rede[x]) for x in range(len(Rede) - 1)) + ", " + str(Rede[-1]) + "]")
    print(" ")


input() #Necessário para o sistema não fechar imediatamente após o fim do programa
