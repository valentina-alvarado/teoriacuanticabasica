#valentina alvarado
#libreria teoria cuantica basica

import numpy as np
from vectoresmatricescomplejos import *

def probabilidadpo(posicion,ket):
    norm = modulo(ket[posicion]) ** 2
    norm2 = norma(ket) ** 2
    return norm/norm2

#aux transicion
def brave(vector):
    """funcion que le ayuda a calcular el bra de un vector dado"""
    return adjuntovect(vector)

def probtransicion(ket_1,ket_2):
    """ calcula la probabilidad de transitar de un vector ket a otro"""
    temp = transpuesta(ket_1)
    temp2 = transpuesta(ket_2)
    norm1 = norma(temp[0])
    norm2 = norma(temp[0])
    norma = norm1 * norm2
    bra_ket2 = brave(temp[0])
    transicion = innerpro(bra_ket2,temp[0])
    probabilidad = multiplicar([1/norma,0],transicion)
    return probabilidad

#aux observables

def media(matriz,ket,braket):
    action = accion(matriz,ket)
    med = innerpro(action,braket)
    return med
    
def varianza(matriz,ket,media,braket):
    matrizux = [[(0, 0) for j in range(len(matriz[0]))] for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matrizaux[i][j] = inversaaditiva(media)
                
    matrizaux = sumamtrices(matrizaux,matriz)
    multipli = multiplimatr(matrizaux,matrizaux)
    action = accion(multipli,ket)
    variance = innerpro(action,braket)
    return variance

def matrizobservable(matriz,ket):
    try:
        if hermitiana(matriz):
            braket = bra(ket)
            media = media(matriz,ket,braket)
            variance = varianza(matriz,ket,media,braket)
            return variance
    except:
        print("matriz debe ser hermitiana")
        
def valorespropios(matrix):
    valores, vectores = np.linalg.eig(matrix)
    val = []
    vect = []
    for k in range(len(valores)):
        val += [(valores[k].real, valores[k].imag)]
    for i in range(len(vectores)):
        vect2 = []
        for j in range(len(vectores[0])):
            vect2 += [(vectores[i][j].real, vectores[i][j].imag)]
        vect += [vect2]
    return val, vect

def dinamicasistema(pasos,matriz,estadoi):
    if unitaria(matriz):
        for i in range(pasos):
            matrizn = multiplimatr(matriz,matriz)
        resp = multiplimatr(matrizn,estadoi)
    return resp

 #problemas
 #problema 4.3.1
 def 4_3_1():
     vectori = [[1,0],[[0,0]]]
     obser = [[[0,0],[1,0]],[[1,0],[0,0]]]
     valoresp,vectoresp = valorespropios(obser)
     observable = accion(obser,vectori)
     print("valor propio: ",valoresp)
     print("vector propio: ",vectoresp)
     print("observable: ",observable)

#problema 4.3.2
def 4_3_2:
    vectori = [[1,0],[[0,0]]]
    obser = [[[0,0],[1,0]],[[1,0],[0,0]]]
    valoresp,vectoresp = valorespropios(obser)
    for i in range(len(vectoresp)):
        print(probtransicion(vectori,vectoresp[i]))

#problema 4.4.1
def 4_4_1:
    matriz1 = [[[0,0],[1,0]],[[1,0],[0,0]]]
    matriz2 = [[[(2**(1/2))/2, 0], [(2**(1/2))/2, 0]], [[(2**(1/2))/2, 0], [-(2**(1/2))/2, 0]]]
    if unitaria(matriz1) and unitaria(matriz2):
        mult = multiplimatr(matriz1,matriz2)
        print(unitaria(mult))

#problema 4.4.2
def 4_4_2:
    vectori = [[1,0],[0,0],[0,0],[0,0]]
    matriz = [[[0,0],[1/(2**(1/2)),0],[1/(2**(1/2)),0],[0,0]],
              [[1/(2**(1/2)),0],[0,0],[0,0],[1/(2**(1/2)),0]],
              [[1/(2**(1/2)),0],[0,0],[0,0],[1/(2**(1/2)),0]],
              [[0,0],[1/(2**(1/2)),0],[-1/(2**(1/2)),0],[0,0]]]
    pasos = 3
    print(dinamicasistema(pasos,matriz,vectori))
#print(4_3_1)
#print(4_3_2)
#print(4_4_1)
#print(4_4_2)


    
        
    
    
    


    
    

