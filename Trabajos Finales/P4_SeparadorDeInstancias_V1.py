import numpy as np

archivo = open("instancia_claseExplicacion.txt")
contenido = archivo.readlines()

x = contenido[3:3+int(contenido[1])]
x = [i.split(",") for i in x]
x = [list(map(float, i)) for i in x]

y = contenido[3+int(contenido[1]):]
y = [i.split(",") for i in y]
y = [list(map(float, i )) for i in y]

x = np.array(x)
y = np.array(y)

print("X:")
print(x)

print("Y:")
print(y)

print("Elementos X: ", x.shape)
print("Elementos Y: ", y.shape)

factorEntrenamiento = 0.8 #80% del total de elementos
regEntrenamiento = factorEntrenamiento * x.shape[1]
regPrueba = x.shape[1] - regEntrenamiento
print("Registros para entrenamiendo: ", regEntrenamiento)
print("Registros para prueba: ", regPrueba)
posSeleccionadas = []
datosEntrenamientoX = []
datosENtrenamientoY = []
import random as rnd
for i in range(regEntrenamiento):
    index = rnd.randint(0, regEntrenamiento-1)
    while index in posSeleccionadas:
        index = rnd.randint(0, regEntrenamiento-1)
    datosENtrenamientoY.append([
            y[0][index],
            y[1][index],
            y[2][index],
        ])
    datosEntrenamientoX.append([
            x[0][index],
            x[1][index],
            x[2][index],
            x[3][index]
        ])
    posSeleccionadas.append(index)

    print()