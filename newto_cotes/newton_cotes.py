import math

def F(x):
    return math.pow(math.sin(2*x) + 4*math.pow(x,2) + 3*x,2)

def funcao_geral_integracao(a, b, epson, tipo):
    delta  = 0
    Xi     = 0
    err    = 0
    result = 0
    iter   = 0
    N      = 2
    before_result = 0

    while True:
        iter += 1
        delta = (b-a)/N
        integral = 0
        for i in range(N):
            Xi = a + i*delta
            Xf = Xi + delta
            if(tipo=="fechada1"):
                integral += fechada1(Xi, Xf)
            elif(tipo=="fechada2"):
                integral += fechada2(Xi, Xf)
            elif(tipo=="fechada3"):
                integral += fechada3(Xi, Xf)
            elif(tipo=="fechada4"):
                integral += fechada4(Xi, Xf)
            elif(tipo=="aberta1"):
                integral += aberta1(Xi, Xf)
            elif(tipo=="aberta2"):
                integral += aberta2(Xi, Xf)
            elif(tipo=="aberta3"):
                integral += aberta3(Xi, Xf)
            elif(tipo=="aberta4"):
                integral += aberta4(Xi, Xf)
        N = N*2
        before_result = result
        result = integral
        err = abs((result-before_result)/result)
        
        if (err < epson): 
            break
    
    return iter, result

def fechada1(Xi, Xf): ## N = 1
    return (Xf-Xi)/2*(F(Xi)+F(Xf))
    
def fechada2(Xi, Xf):## N = 2
    h = (Xf-Xi)/2
    return (h)/3*(F(Xi) + 4*F(Xi+h) + F(Xi+2*h))

def fechada3(Xi, Xf): ## N = 3
    h = (Xf-Xi)/3
    return (3*(h)/8)*(F(Xi) + 3*F(Xi+h) + 3*F(Xi+2*h) +F(Xi+3*h))

def fechada4(Xi, Xf): ## N = 4
    h = (Xf-Xi)/4
    return (2*(h)/45)*(7*F(Xi) + 32*F(Xi+h) + 12*F(Xi+2*h) +32*F(Xi+3*h)+7*F(Xi+4*h))
        
def aberta1(Xi, Xf): ## N = 1
    h = (Xf-Xi)/3
    return (Xf-Xi)/2*(F(Xi+h)+F(Xi+2*h))

def aberta2(Xi, Xf): ## N = 2
    h = (Xf-Xi)/4
    return ((4*h)/3)*(2*F(Xi+h) - F(Xi+2*h) + 2*F(Xi+3*h))   

def aberta3(Xi, Xf): ## N = 3
    h = (Xf-Xi)/5
    return ((5*(Xf-Xi)/5)/24)*(11*F(Xi+h) + F(Xi+2*h) + F(Xi+3*h) + 11*F(Xi+4*h))

def aberta4(Xi, Xf): ## N = 4
    h = (Xf-Xi)/6
    return ((6*h)/20)*(11*F(Xi+h) - 14*F(Xi+2*h) + 26*F(Xi+3*h) - 14*F(Xi+4*h)+ 11*F(Xi+5*h))
