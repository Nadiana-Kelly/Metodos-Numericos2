import newtonCotes

a = input('Qual será o intervalo [a]? ')
a = int(a)
b = input('Qual será o intervalo [b]? ')
b = int(b)

eps = input('Qual será o erro aproximado? ex: 0.000001\n')
eps = float(eps)

print("              FÓRMULAS DE NEWTON-COTES")
print("1 - Abordagem aberta")
print("2 - Abordagem fechada")
print("0 - Sair do programa")
metodo_tipo = input('Qual abordagem você deseja? ')
metodo_tipo = int(metodo_tipo)

if(metodo_tipo == 1):
    print("\n              Abordagem aberta")
    print("1 - Polinômio de substituição de grau 1")
    print("2 - Polinômio de substituição de grau 2")
    print("3 - Polinômio de substituição de grau 3")
    print("4 - Polinômio de substituição de grau 4")
    methodIntegration = input('com qual polinômio você quer integrar? ')
    methodIntegration = int(methodIntegration)

    if(methodIntegration == 1):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "fechada1")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
    elif(methodIntegration == 2):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "fechada2")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
    elif(methodIntegration == 3):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "fechada3")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
    elif(methodIntegration == 4):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "fechada4")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
elif(metodo_tipo==2):
    print("\n              Abordagem fechada")
    print("1 - Polinômio de substituição de grau 1")
    print("2 - Polinômio de substituição de grau 2")
    print("3 - Polinômio de substituição de grau 3")
    print("4 - Polinômio de substituição de grau 4")
    print("0 - Sair do programa")
    methodIntegration = input('Com qual polinômio você quer integrar? ')
    methodIntegration = int(methodIntegration)
    if(methodIntegration == 1):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "aberta1")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
    elif(methodIntegration == 2):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "aberta2")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
    elif(methodIntegration == 3):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "aberta3")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
    elif(methodIntegration == 4):
        gr = newtonCotes.funcao_geral_integracao(a, b, eps, "aberta4")
        print("\n     --------------------------------")
        print("      Resultado: " , gr[1])
        print("      Interações: " , gr[0])
        print("     --------------------------------")
