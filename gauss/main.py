import gauss_chebyshev
import gauss_hermite
import gauss_laguerre


print("          Fórmulas de Gauss para integrações especiais.")
print("1 - Gauss-Hermite")
print("2 - Gauss-Laguerre")
print("3 - Gauss-Chebyshev")
response = input('Qual método você deseja? ')
response = int(response)

if(response==1):
    grau2 = gauss_hermite.gauss_Hermite_2pontos()
    grau3 = gauss_hermite.gauss_Hermite_3pontos()
    grau4 = gauss_hermite.gauss_Hermite_4pontos()
    print("\n     --------------------------------")
    print("      Resultados: " )
    print("      Grau 2: ", grau2)
    print("      Grau 3: ", grau3)
    print("      Grau 4: ", grau4)
    print("     --------------------------------")
    
elif(response==2):
    grauL2 = gauss_laguerre.gauss_Laguerre_2pontos()
    grauL3 = gauss_laguerre.gauss_Laguerre_3pontos()
    grauL4 = gauss_laguerre.gauss_Laguerre_4pontos()
    print("\n     --------------------------------")
    print("      Resultados: " )
    print("      Grau 2: ", grauL2)
    print("      Grau 3: ", grauL3)
    print("      Grau 4: ", grauL4)
    print("     --------------------------------")
elif(response==3):
    grauC2 = gauss_chebyshev.gauss_Chebyshev_2pontos()
    grauC3 = gauss_chebyshev.gauss_Chebyshev_3pontos()
    grauC4 = gauss_chebyshev.gauss_Chebyshev_4pontos()
    print("\n     --------------------------------")
    print("      Resultados: " )
    print("      Grau 2: ", grauC2)
    print("      Grau 3: ", grauC3)
    print("      Grau 4: ", grauC4)
    print("     --------------------------------")