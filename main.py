import math
import numpy as np
import time

def matrixSimple ():
    array = np.random.randint(10, size=(1000, 1000))
    return array

a = matrixSimple()
b = matrixSimple()
c = a*b

c[4][4]=19
c[16][16]=31
c[25][25]=89
c[36][36]=97
c[64][64]=83
#%%
meta = 90.0

def vefMatrizMult (a,b,c,meta):
    MR = a * b
    sumando = 0.0
    largo = len(MR)
    flag = True
    for i in range(largo):
        for j in range(largo):
            if MR[i][j] == c[i][j]:
                sumando = sumando + 1

    meta = (math.pow(largo,2)*meta)/100

    print(sumando)
    print(meta)

    if meta <= sumando:
        flag = True
    else:
        flag = False

    print(flag)
    return

inicio = time.time()
vefMatrizMult(a,b,c,meta)
fin = time.time()
print(fin-inicio)
#%%
def Freivalds(a, b, c, N):
    # Generar un vector aleatorio
    largos = len(a)
    X = [0] * largos

    X=np.random.randint(N, size=largos)

    BX = [0] * largos

    for i in range(0, largos):
        for j in range(0, largos):
            BX[i] = BX[i] + b[i][j] * X[j]

    CX = [0] * largos
    for i in range(0, largos):
        for j in range(0, largos):
            CX[i] = CX[i] + c[i][j] * X[j]


    ABX = [0] * largos
    for i in range(0, largos):
        for j in range(0, largos):
            ABX[i] = ABX[i] + a[i][j] * BX[j]

    for i in range(0, largos):
        if (ABX[i] - CX[i] != 0):
            print("False")
            return False
    print("True")
    return True

N=2
inicio2 = time.time()
Freivalds(a,b,c,N)
fin2 = time.time()
print(fin2-inicio2)
#%%

def Freivalds(a, b, c, N):
    largos = len(a)
    X = [0] * largos

    X=np.random.randint(N, size=largos)

    BX = [0] * largos

    for i in range(0, largos):
        for j in range(0, largos):
            BX[i] = BX[i] + b[i][j] * X[j]

    CX = [0] * largos
    for i in range(0, largos):
        for j in range(0, largos):
            CX[i] = CX[i] + c[i][j] * X[j]

    ABX = [0] * largos
    for i in range(0, largos):
        for j in range(0, largos):
            ABX[i] = ABX[i] + a[i][j] * BX[j]

    #print("axbr")
    #print(ABX)

    for i in range(0, largos):
        if (ABX[i] - CX[i] != 0):
            return False
    return True

def RepeatFreivalds(a,b,c,N,K):
    sumando = 0
    final = [0] * K
    for i in range(0, K):
        final[i] = Freivalds(a,b,c,N)
    for j in range(0, K):
        if (final[1] != final[j]):
            sumando = sumando + 1
    print(final)
    if (sumando > 0):
        print("False")
        return False
    print("True")
    return True

N=2
K=10
inicio3 = time.time()
RepeatFreivalds(a,b,c,N,K)
fin3 = time.time()
print(fin3-inicio3)