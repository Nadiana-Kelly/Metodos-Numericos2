import numpy as np

t_0 = 0     # tempo inicial
v_0 = 5     # velocidade inicial
y_0 = 200   # altitude inicial
k = 0.25    # constante de aerodinâmica
m = 2       # massa do objeto
g = 10      # gravidade

dts_ls = [0.1, 0.01, 0.001, 0.0001]

# Método de Runge-Kutta de terceira ordem
def runge_kutta(t_0, v_0, y_0, k, m, g, dt):
    s_0 = np.array([v_0, y_0])
    i = 1
    y_max = y_0
    t_max = t_0
    v_final = 0
    while (s_0[1] >= 0):
        v_meio = v_0 + (dt/2) * (-g - (k/m * v_0))
        y_meio = y_0 + (dt/2) * v_0

        v_1 = v_0 + dt * (-g - (k/m * v_0))
        y_1 = y_0 + dt * v_0
        
        s_1 = s_0 + dt *((1/6)*(np.array([-g-(k/m * v_0), v_0])) + (4/6)*(np.array([-g-(k/m * v_meio), v_meio])) + (1/6)*(np.array([-g-(k/m * v_1), v_1])))

        t_0 = t_0 + dt
        i += 1
        v_final = v_0
        v_0 = s_1[0]
        y_0 = s_1[1]
        s_0 = s_1
        if y_0 > y_max:
            y_max = y_0
            t_max = t_0
    
    print(f"Δt                = {dt}:")
    print(f"altura_max        = {y_max}")
    print(f"tempo_max_altura  = {t_max}")
    print(f"tempo_total       = {t_0-dt}")
    print(f"velocidade_final  = {abs(v_final)}\n\n")

for dt in dts_ls:
    runge_kutta(t_0, v_0, y_0, k, m, g, dt)
