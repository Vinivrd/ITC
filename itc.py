def checkTransicao(vetorVar,numEstados):
    transicao = input('digite a transicao: ').split()
    transicao0 = int(transicao[0])
    transicao2 = int(transicao[2])
    ## tratar o else
    if((transicao0 >= 0 and  transicao0 <= numEstados -1) and (transicao2 >= 0 and  transicao2 <= numEstados -1)):
        if(transicao[1] in vetorVar):
            return transicao
        else:
            print('erro')
    else:
        print('erro')

def checkVariaveis(vetorVar,maxSimbolos):
    variaveis =  list(input())
    if(len(variaveis) < maxSimbolos):
        for i in range(len(variaveis)):
            if(variaveis[i] not in vetorVar):
                print("erro")
                ##tratar o else
        return variaveis
    else:
        print("Passou do tamnho")

##entradas
numEstados =  int(input("Digite os estados: ")) 
if(numEstados >= 1  and numEstados <= 10): #
    print()
else:
    print()

##var's
readSimbolos = input("Digite o numero de simbolos:  ").split()
numSimbolos =  int(readSimbolos[0])

simbolosTerminais = []
numEstadosFinais = input("Digite o numero de estados finais: ").split()

if(numSimbolos >= 1 and numSimbolos <= 10):
    print()
else:
    print()

for i in  range(numSimbolos):
    simbolosTerminais.append(readSimbolos[i+1])



if(len(numEstadosFinais)-1 ==  int(numEstadosFinais[0])):
    
    for i in range(int(numEstadosFinais[0])):
        if(int(numEstadosFinais[i+1]) < 0 or int(numEstadosFinais[i+1]) > numEstados -1):
            print('ERRO') ## mudar no final do código
else:
    print(':(')

vetorTransicao = []
numInteracoes = int(input('Digite o numero de interações: '))
if(numInteracoes >= 1 and numInteracoes <= 50):
    for i in range(numInteracoes):
        vetorTransicao.append(checkTransicao(simbolosTerminais,numEstados))
else:
    print('Interacoes erro')





numEntradas = int(input('Digite o numero de entradas: '))
if(numEntradas >= 1 and numEntradas <= 10):
     for i in range(numEntradas):  
         checkVariaveis(simbolosTerminais,20)    
else:
    print('Entradas erro')


