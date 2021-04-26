'''
LAMBDA = factor de aprendizaje = 0.2

CÁLCULOS

Cálculo del error = e = (y - z)
e permite ajustar cambio de umbral (theta) = DELTA THETA = - (LAMBDA * e)
Wi se ajustan sumándoles = DELTA Wi = LAMBDA * e * Xi

FUNCIÓN DE ACTIVACIÓN

y = (SUM((Wi * Xi) - THETA) >= 0) ? 1 : 0

ENTRENAMIENTO FUNCIÓN OR

LAMBDA = 0.2
W1 = 0.3
W2 = 0.5
THETA = 0.4

Al ser una función OR, la salida de los valores (valor deseado d) debe ser 1 en el perceptrón (según la función de activación)
1. x1 = 0, x2 = 0
z = (0 * 0.3 + 0 * 0.5) - 0.4 = -0.4. z < 0 --> z = 0

2. x1 = 0, x2 = 1
z = (0 * 0.3 + 1 * 0.5) - 0.4 = 0.1. z >= 0 --> z = 1

3. x1 = 1, x2 = 0
z = (1 * 0.3 + 0 * 0.5) - 0.4 = -0.1. z < 0 --> z = 0

Como d = 1 y z = 0, se calcula el error:
e = (d - z) = (1 + 0) = 1

AJUSTAR PESOS Y UMBRAL
THETA = - (LAMBDA - e) = -(0.2 * 1) = -0.2
W1 = LAMBDA * e * x1 = 0.2 * 1 * 1 = 0.2
W1 = LAMBDA * e * x2 = 0.2 * 1 * 0 = 0

SUMAR RESULTADOS AL UMBRAL Y LOS PESOS
THETA = 0.4 + (-0.2) = 0.2
w1 = 0.3 + 0.2 = 0.5
w2 = 0.5 + 0 = 0.5

ITERAR TODA LA COMPUERTA OR Y REALIZAR LOS AJUSTES NECESARIOS
x1 = 0, x2 = 0
x1 = 0, x2 = 1
x1 = 1, x2 = 0
x1 = 1, x2 = 1
'''
import openpyxl as x
import pandas as pd

def entrenar(theta, fac_ap, w1, w2, epochs, x1, x2, d, n_muestras):
    error = True
    while error:
        error = False
        print(f"\nIteración {epochs + 1}")
        for i in range(0, n_muestras):
            z = ((x1[i] * w1) + (x2[i] * w2)) - theta
            #z = (0 * 0.3 + 0 * 0.5) - 0.4 = -0.4. z < 0 --> z = 0
            print(f"\n{i + 1}.- x1 = {x1[i]}, x2 = {x2[i]}")
            print(f"\tZ = (({x1[i]} * {w1}) + ({x2[i]} * {w2})) - {theta}")
            print(f"\tZ = {'{:.3f}'.format(z)}. {'Z < 0 POR LO TANTO Z = 0' if z < 0 else 'Z >= 0 POR LO TANTO Z = 1'}")

            z = 1 if z >= 0 else 0

            if z != d[i]:
                error = True
                #Cálculo error
                e = (d[i] - z)
                #Ajuste theta
                theta = theta + (-(fac_ap * e))
                #Ajustar pesos
                w1 = w1 + (x1[i] * e * fac_ap)
                w2 = w2 + (x2[i] * e * fac_ap)
                epochs += 1

    return w1, w2, epochs, theta


def main():
    #Leer archivo excel
    file = pd.read_excel("perceptron_data.xlsx")
    theta = 0.4
    fac_ap = 0.2
    w1 = 0.3
    w2 = 0.5
    #Número de veces que se ajustan los pesos
    epochs = 0
    x1 = file["x1"]
    x2 = file["x2"]
    d = file ["d"]
    n_muestras = len(d)
    
    w1, w2, epochs, theta = entrenar(theta, fac_ap, w1, w2, epochs, x1, x2, d, n_muestras)
    print(f"W1 = {w1}\nW2 = {w2}\nTheta = {theta}\nEpochs = {epochs}")

if __name__ == '__main__':
    main()
     