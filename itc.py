from collections import deque

def checkTransicao(vetorVar,numEstados):
    transicao = input('digite a transicao: ').split()
    transicao0 = int(transicao[0])
    transicao2 = int(transicao[2])

    if((transicao0 >= 0 and  transicao0 <= numEstados -1) and (transicao2 >= 0 and  transicao2 <= numEstados -1)):
        if(transicao[1] in vetorVar):
            return transicao
        else:
            print('erro')
    else:
        print('erro')

def dicionarioTransicao(transicoes):
    dicionarioTransicoes = {}
    for transicao in transicoes:
        estado_atual, simbolo, proximo_estado = transicao
        if (estado_atual, simbolo) in dicionarioTransicoes:
            dicionarioTransicoes[(estado_atual, simbolo)].add(proximo_estado)
        else:
            dicionarioTransicoes[(estado_atual, simbolo)] = {proximo_estado}
    return dicionarioTransicoes

def checkVariaveis(vetorVar,maxSimbolos):
    variaveis =  list(input())
    if(len(variaveis) < maxSimbolos):
        for i in range(len(variaveis)):
            if(variaveis[i] not in vetorVar):
                print("erro")
        cadeiasEntradas.append(variaveis)
    else:
        print("Passou do tamnho")

def automato(estados, simbolos_terminais, estados_finais, estado_inicial, transicoes):
    automato = {
        'estados': set(estados),
        'simbolos_terminais': set(simbolos_terminais),
        'estados_finais': set(estados_finais),
        'estado_inicial': estado_inicial,
        'transicoes': dict(transicoes)
    }
    return automato

def testeEntradas(automato, entrada):
    fila = deque([(automato['estado_inicial'], 0)])  # Inicializa a fila com o estado inicial
    visitados = set()  # Conjunto para rastrear os estados já visitados

    while fila:
        estado, indice = fila.popleft()  # Remove o próximo estado da fila
        if (estado, indice) in visitados:
            continue  # Se já visitamos este estado nesta posição, vamos para o próximo
        visitados.add((estado, indice))  # Marca o estado atual como visitado

        if estado in automato['estados_finais']:
            if indice == len(entrada):
                return True  # Aceita se estamos em um estado final e chegamos ao final da entrada

        if indice == len(entrada):  # Se chegamos ao final da entrada
            continue  # Vamos para o próximo estado

        simbolo = entrada[indice]  # Próximo símbolo da entrada

        # Adiciona os próximos estados de acordo com as transições
        transicoes = automato['transicoes'].get((estado, simbolo), set())
        for prox_estado in transicoes:
            fila.append((prox_estado, indice + 1))

        # Adiciona os próximos estados para transições vazias
        transicoes_vazias = automato['transicoes'].get(('', simbolo), set())
        for prox_estado in transicoes_vazias:
            fila.append((prox_estado, indice))
    
    return False
    
        
#Entrada do número de estados
numEstados =  int(input("Digite os estados: ")) 
if(numEstados >= 1  and numEstados <= 10): #
    estados = []
    for i in range(numEstados):
        estados.append(i)
else:
    print()

#Estado inicial sempre é o 0
estadoInicial = '0'

#Entrada dos Simbolos Terminais
readSimbolos = input("Digite o numero de simbolos:  ").split()
numSimbolos =  int(readSimbolos[0])
simbolosTerminais = []

if(numSimbolos >= 1 and numSimbolos <= 10):
    print()
else:
    print()

for i in  range(numSimbolos):
    simbolosTerminais.append(readSimbolos[i+1])

#Entrada dos Estados Finais
readEstadosFinais = input("Digite o numero de estados finais: ").split()
numEstadosFinais =  int((readEstadosFinais[0]))
estadosFinais = []

if(len(readEstadosFinais) - 1 ==  numEstadosFinais):
    for i in range(numEstadosFinais):
        if(int(readEstadosFinais[i+1]) >= 0 and int(readEstadosFinais[i+1]) <= numEstados -1):
            estadosFinais.append(readEstadosFinais[i+1])
else:
    print(':(')

simbolosTerminais.append('-')
vetorTransicao = []

numInteracoes = int(input('Digite o número de interações: '))
if(numInteracoes >= 1 and numInteracoes <= 50):
    for i in range(numInteracoes):
        transicao = checkTransicao(simbolosTerminais, numEstados)
        vetorTransicao.append(transicao)
        # Se a transição for vazia, insira uma transição vazia para cada símbolo do alfabeto
        if transicao[1] == '-':
            for simbolo in simbolosTerminais:
                if (transicao[0], simbolo) not in vetorTransicao:
                    vetorTransicao.append((transicao[0], simbolo, transicao[2]))
else:
    print('Número de interações inválido')

transicoes = dicionarioTransicao(vetorTransicao)

cadeiasEntradas= []
simbolosTerminais.remove('-')
numEntradas = int(input('Digite o numero de entradas: '))
if(numEntradas >= 1 and numEntradas <= 10):
     for i in range(numEntradas):  
         checkVariaveis(simbolosTerminais,20)    
else:
    print('Entradas erro')

autômato = automato(estados, simbolosTerminais, estadosFinais, estadoInicial, transicoes)

for i in range(len(cadeiasEntradas)):
    if testeEntradas(autômato, cadeiasEntradas[i]) == True:
        print('aceita')
    else:
        print('rejeita')