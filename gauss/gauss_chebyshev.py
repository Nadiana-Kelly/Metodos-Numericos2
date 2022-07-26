import math

def f(x): 
    return math.pow(math.sin(2*x) + 4*math.pow(x,2) + 3*x,2)

def gauss_Chebyshev_2pontos(): 
    s = math.sqrt(2)
    raizes_s = [-1/s, s]
    w = math.pi/2
    pesos_w = [w, w]

    return funcao_geral_integracao(2, pesos_w, raizes_s)

def gauss_Chebyshev_3pontos(): 
    s = math.sqrt(3)
    raizes_s = [-s/2, 0, s/2]
    w = math.pi/3
    pesos_w = [w, w, w]

    return funcao_geral_integracao(3, pesos_w, raizes_s)

def gauss_Chebyshev_4pontos(): 
    s = math.sqrt(0.14644)
    s_2 = math.sqrt(0.85355)

    raizes_s = [s, -s, s_2, -s_2]
    w = math.pi/4
    pesos_w = [w, w, w, w]

    return funcao_geral_integracao(4, pesos_w, raizes_s)

def funcao_geral_integracao(qtd_grau, pesos_w, raizes_s):
    somatorio = 0
    for k in range(qtd_grau):
        somatorio += (pesos_w[k] * f(raizes_s[k]))

    return somatorio