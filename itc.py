##AFD - Autômato Finito Deterministico
M = {Q, ∑, &, q0, F}
Q = {q0, q1}
∑ = {0,1}
& = {
&: (q0, 0) -> q1,
&: (q0, 1) -> q1,
&: (q1, 0) -> q1,
&: (q1, 1) -> q1
}
q0 = q0
F = {q1}
estados = []
alfabeto = []
transicao = {}
estado_inicial = ""
estados_aceit = []

##recebe dados automatos
estados = input().split()

alfabeto = input().split()

estados_aceit = input().split()

for estado in estados:
    for simbolo in alfabeto:
        proximo_estado = input()

        if proximo_estado == "-": 
            transicao[(estado, simbolo)] = None
        else:
            transicao[(estado, simbolo)] = proximo_estado


estados_inicial = input()





#reconhecendo linguagem

entrada = input()

estado_atual = estado_inicial

for simbolo in entrada:
    estado_atual = transicao[(estado_atual, simbolo)]

    if estado_atual == None:
        break
if estado_atual in estados_aceit:
    print("")
else:
    print("")