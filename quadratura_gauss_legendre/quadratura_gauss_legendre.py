import math

def f(x):
    return math.pow(math.sin(2*x) + 4*math.pow(x,2) + 3*x, 2)

def x(sk, xi, xf): 
    x_final = (xi + xf) / 2 + ((xf - xi) / 2) * sk
    return x_final

def gauss_Legendre_2pontos(a_inicio, b_fim, erro_estimado): 
    s = math.sqrt(1/3)
    raizes_s = [s, -s]
    w = 1
    pesos_w = [w, w]

    return funcao_geral_integracao(2, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)

def gauss_Legendre_3pontos(a_inicio, b_fim, erro_estimado): 
    s = math.sqrt(3/5)
    raizes_s = [s, 0, -s]
    w = 5/9
    w_2 = 8/9
    pesos_w = [w, w_2, w]

    return funcao_geral_integracao(3, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)

def gauss_Legendre_4pontos(a_inicio, b_fim, erro_estimado): 
    raizes_s = [0.861136, -0.861136, 0.339981, -0.339981]
    w = 0.34785
    w_3 = 0.65214 
    pesos_w = [w, w, w_3, w_3]

    return funcao_geral_integracao(4, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def funcao_geral_integracao(qtd_pontosInterpolacao, pesos_w, raizes_s, epson, a, b):
    #definindo as variaveis
    delta = 0
    xi = 0
    xf = 0
    erro = 0 #erro inicial para comparar com o epson dado
    resultadoAnterior = 0
    resultado = 0
    resultado_aux = 0 #precisamos desse para guardar o resultado anterior
    N = 1

    while True:
        resultadoAnterior = resultado
        resultado_aux = resultado
        resultado = 0
        interacoes = 0
        
        delta = (b - a) / N
        for i in range(N): # aqui vamos realizar o método de gauss por partição, começando com 1 depois N*2
            xi = a + i*delta
            xf = xi + delta
            somatorio = 0
            for k in range(qtd_pontosInterpolacao):
                somatorio += (pesos_w[k] * f(x(raizes_s[k], xi, xf))) #aqui fazemos o somatorio do próprio método de gauss com a quantidade de pontos especifico
           
            resultado  += ((xf - xi) / 2) * somatorio # interamos o resultado
           
            interacoes += 1
          
        N = N*2
        resultadoAnterior = resultado_aux
      
        erro = abs((resultadoAnterior - resultado)/ resultado)

        if (erro < epson): 
            break

    print("\nPARTIÇÕES:", N)
    return interacoes, resultado


print("\n-------------- BEM VINDO AO PROGRAMA --------------\n")

a = input('Qual será o intervalo [a]? ')
a = int(a)
b = input('Qual será o intervalo [b]? ')
b = int(b)

epson = input('Qual será o erro aproximado? ex: 0.000001\n')
epson = float(epson)
print("              Quadraturas de Gauss-Legendre")
print("1 - Com dois pontos")
print("2 - Com três pontos")
print("3 - Com quatro pontos")
print("0 - Voltar")
response = input('Qual abordagem você deseja? ')
response = int(response)

if(response==1):
    result_grau2 = gauss_Legendre_2pontos(a, b, epson)
    print("\n     --------------------------------")
    print("      Resultado: " , result_grau2[1])
    print("      Interações: " , result_grau2[0])
    print("     --------------------------------")
    
elif(response==2):
    result_grau3 = gauss_Legendre_3pontos(a, b, epson)
    print("\n     --------------------------------")
    print("      Resultado: " , result_grau3[1])
    print("      Interações: " , result_grau3[0])
    print("     --------------------------------")

elif(response==3):
    result_grau4 = gauss_Legendre_4pontos(a, b, epson)
    print("\n     --------------------------------")
    print("      Resultado: " , result_grau4[1])
    print("      Interações: " , result_grau4[0])
    print("     --------------------------------")
