from math import sqrt

# Algoritmo QR

#n : Tamaño de la matriz
#a : Arreglo que contiene los elementos de la diagonal principal
#b : arreglo que contiene los elementos de las subdiagonales
#TOL : maxima diferencia permitida respecto a 0 
#m : Cantidad máxima de iteraciones

def QR(n, a, b, TOL, m):
    c = []
    d = []
    q = []
    r = []
    x = []
    y = []
    z = []
    sigma = []

    #Se inicializan las listas con n elementos con valor de 0
    for j in range (0, n + 1):
        c.append(0)
        d.append(0)
        q.append(0)
        r.append(0)
        x.append(0)
        y.append(0)
        z.append(0)
        sigma.append(0)
    
    eigenvalues = []
    
    k = 1 # Primera iteración
    shift = 0
    eigenvalue = 0

    #Se agregan valores a las listas para facilitar la lectura del algoritmo
    a.insert(0,0)
    b.insert(0,0)
    b.insert(0,0)

    while k <= m:
        # Se verifica si los extremos de la diagonal contienen eigenvalores
        if(b[n] <= TOL):
            eigenvalue = a[n] + shift
            eigenvalues.append(eigenvalue)
            n = n - 1
        
        if(b[2] <= TOL):
            eigenvalue = a[1] + shift
            eigenvalues.append(eigenvalue)
            n = n - 1
            a[1] = a[2]
            # Se desplazan los valores en las diagonales  
            for j in range(2, n + 1):
                a[j] = a[j + 1]
                b[j] = b[j + 1]
        
        if n == 0 :
            return eigenvalues
        
        if n == 1 :
            eigenvalue = a[1] + shift
            eigenvalues.append(eigenvalue)
            return eigenvalues
        
        for j in range (3 , n):
            if( b[j] <= TOL):
                print('Dividido en ', a[1:j - 1], b[2: j -1])
                print('y ', a[j: n], b[j + 1 : n])
                print('Cambio: ', shift)
        
        b[0] = - (a[n - 1] + a[n])
        c[0] = a[n] * a[n - 1] - (b[n]) ** 2
        d[0] = sqrt(((b[0] ** 2) - 4 * c[0]))

        if(b[0] > 0):
            mu1 = -2 * c[0] / (b[0] + d[0])
            mu2 = - (b[0] + d[0]) / 2
        else:
            mu1 = (d[0] - b[0]) / 2
            mu2 = (2 * c[0]) / (d[0] - b[0])

        if(n == 2):
            eigenvalue = mu1 + shift
            eigenvalues.append(eigenvalue)
            eigenvalue = mu2 + shift
            eigenvalues.append(eigenvalue)

        if abs(mu1 - a[n]) < abs(mu2 - a[n]):
            sigma[0] = mu1-a[n]
        else:
            sigma[0] = mu2-a[n]

        shift = shift + sigma[0]

        for j in range(1, n + 1):
            d[j] = a[j] - sigma[0]

        #Calcular R^k
        x[1] = d[1]
        y[1] = b[2]
        c[1] = c[0]
        sigma[1] = sigma[0]
        for j in range (2, n + 1):
            z[j - 1] = sqrt((x[j - 1] ** 2) + (b[j] ** 2))
            c[j] = x[j - 1] / z[j - 1]
            sigma[j] =  b[j] / z[j - 1]

            q[j - 1] = c[j] * y[j - 1]  + sigma[j] * d[j]
            x[j] = - sigma[j] * y[j - 1] + c[j] * d[j]
            
            if(j != n):
                r[j - 1] = sigma[j] * b[j + 1]
                y[j] = c[j] * b[j + 1]
        
        #Calcular A ^ (k + 1)
        z[n] = x[n]
        a[1] = sigma[2] * q[1] + c[2] * z[1]
        b[2] = sigma[2] * z[2]

        for j in range(2, n):
            a[j] = (sigma[j + 1] * q[j]) + (c[j] * c[j + 1] * z[j])
            b[j + 1] = sigma[j + 1] * z[j + 1]

        a[n] = c[n] * z[n]

        k = k + 1

    print('Se ha superado el numero maximo de iteraciones')
    return eigenvalues

eigenvalues = QR(3, [3, 3, 3], [1, 1], 0.001, 100)
print(eigenvalues)