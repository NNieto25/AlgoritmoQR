from math import sqrt
# Algoritmo QR a
#posiblemente los rangos deban disminuir en 1 en limite superior

def QR(n, ar, br, TOL, m):
    l = 0
    k = 1
    shift = 0
    ans = []

    while(k <= m): #Pasos 3 - 19 
        if(abs(br[n]) <= TOL):
            l = ar[n] + shift
            ans.append(l)
            n = n - 1
        if(abs(br[1]) <= TOL):
            l = ar[0] + shift
            ans.append(l)
            n = n - 1
            ar[0] = ar[1]
            for j in range (1, n):
                ar[j] = ar[j + 1]
                br[j] = br[j + 1]
        if(n == 0):
            return ans
        if(n == 1):
            l = ar[0] + shift
            ans.append(l)
            return ans
        for j in range (2, n - 1):
            if(br[j] <= TOL ):
                print('Dividido en ', ar[0:j], br[1:j])
                print('y', ar[j:n + 1], br[j + 1: n + 1])
                print('Cambio: ', shift)
                return ans
        b =  - ( ar[n - 1] + ar[n])
        c = ar[n] * ar[n -1] - (br[n] ** 2) 
        d = sqrt(((b ** 2)  - 4 * c))
        if(b > 0):
            miu1 = (-2 * c) / (b + d)
            miu2 = - (b + d) / 2
        else:
            miu1 = (d - b) / 2
            miu2 = (2 * c) / (d - b)
        if(n == 2):
            l = miu1 + shift
            ans.append(l)
            l = miu2 + shift
            ans.append(l)
            return ans
        if abs(miu1 - ar[n]) < abs(miu2 - ar[n]):
            sigma = abs(miu1-ar[n])
        else:
            sigma = abs(miu2-ar[n])
        shift = shift + sigma
        d = []
        for j in range(0, n):
            d.append(ar[j] - sigma)

        #Calcular R^k
        x = []
        y = []
        x.append(d[0])
        y.append(br[0])
        
        aux = sigma
        sigma = []
        sigma.append(aux)
        aux = c
        c = [] 
        c.append(c)
        z = []
        q = []
        r = []
        for j in range (1, n):
            z.append(sqrt(x[j - 1] ** 2 + br[j] ** 2))
            c.append(x[j - 1] / z[j - 1])
            sigma.append(br[j] / z[j - 1])
            q.append(c[j] * y[j - 1] + sigma[j] * d[j])
            x.append((- sigma[j] * y[ j - 1] + c[j] * d[j]))
            if (j != n):
                r.append(sigma[j] * br[j + 1])
                y.append(c[j] * br[j + 1])

        # Se calcula A^(k + 1)
        z[n] = x[n]
        ar[0] = sigma[1] * q[0] + c[1] * z[0]
        br[1] = sigma[1] * z[1]   
        for j in range(1, n - 1):
            ar[j] = sigma[j + 1] * q[j] + c[j] * c[j + 1] * z[j]
            br[j + 1] = sigma[j + 1] * z[j + 1]
        
        ar[n] = c[n] * z[n]
        k = k + 1
    
    print('Cantidad de iteraciones ha sido excedida.')
    return ans

eigenvalues = QR(3, [3, 3, 3], [1, 1], 0.001, 100)