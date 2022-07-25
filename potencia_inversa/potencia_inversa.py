import numpy as np
import potencia_regular as pr

#metodo da potencia inversa nada mais é do que o metodo da potencia regular aplicada em cima da matriz inversa
def Potencia_inversa(matriz, vetor, epson):
    a1_inversa = np.linalg.inv(matriz)
    lambda1_a1, x_dominante = pr.Potencia_Regular(a1_inversa, vetor, epson) #vai devolver o autovalor dominante da matriz inversa (lambda)
    x_n = x_dominante
    lambda_n_a1 = 1/lambda1_a1 #lambda N é o inverso do lambda dominante da matriz inversa
    return [lambda_n_a1, x_n] #autovalor e autovetor

def run():
    print("\n-------------- BEM VINDO AO PROGRAMA --------------")
    print("            Método da potência inversa")
    print( "---------------------------------------------------\n")

    A = [
    [-40, 8,  4,  2,  1],
    [8,  -30, 12, 6,  2],
    [4,  12, 20, 1,  2],
    [2,  6,  1,  25, 4],
    [1,  2,  2,  4,  5]]

    # hh = pr.householder.metodo_house_holder(A, 5)
    v1 = [1, 1, 1, 1, 1]
    # tridiagonal, H_acumulada = hh.metodo()

    ## autovalor e auto_vetor da matriz tridiagonal
    autovalor, auv = Potencia_inversa(A, v1, 0.00001)

    #autovetor_da_A = pr.matriz_x_vetor(auv, H_acumulada)

    print("autovalor: {}, autovetor: ({}, {}, {}, {}, {}\n\n\n)".format(autovalor, auv[0], auv[1], auv[2], auv[3], auv[4]))

    print("USANDO NUMPY PRA COMPARAR\n")

    print(np.linalg.eig(A))

run()


