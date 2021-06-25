def qr(n, a_array, b_array, tol, max):
    n = n-1
    k = 1
    shift = 0
    x = []
    y = []
    q = []
    r = []
    s = []
    z = []

    while k <= max:
        if abs(b_array[n-1]) <= tol:
            eigen_val = a_array[n] + shift
            print(str(eigen_val))
            n = n - 1

        if abs(b_array[0]) <= tol:
            eigen_val = a_array[0] + shift
            print(str(eigen_val))
            n = n - 1
            a_array[0] = a_array[1]
            for j in range(1, n):
                a_array[j] = a_array[j+1]
                b_array[j] = b_array[j+1]

        if n == -1:
            break

        if n == 0:
            eigen_val = a_array[0] + shift
            print(eigen_val)
            break

        #No entendí kp2 con el print
        for j in range(2, n-1):
            if abs(b_array[j]) <= tol:
                print("a")
        
        b = -(a_array[n-1] + a_array[n])
        c = a_array[n]*a_array[n-1]-(b_array[n-1])**2
        d = (b**2-4*c)**(1/2)

        if b > 0:
            mu1 = -2*c/(b+d)
            mu2 = -(b+d)/2
        else:
            mu1 = (d-b)/2
            mu2 = 2*c/(d-b)

        if n == 1:
            eigen1 = mu1 + shift
            eigen2 = mu2 + shift
            print(str(eigen1) + " - " + str(eigen2))
            break

        if abs(mu1 - a_array[n]) < abs(mu2 - a_array[n]):
            sigma = mu1-a_array[n]
        else:
            sigma = mu2-a_array[n]

        shift = shift + sigma

        d = []
        for j in range(0, n):
            d.append(a_array[j] - sigma)

        x.append(d[0])
        y.append(b_array[0])
        
        aux = sigma
        sigma = []
        sigma.append(aux)
        aux = c
        c = [] 
        c.append(c)

        for j in range(1, n):
            z.append(((x[j-1])**2 + (b_array[j])**2)**(1/2))
            c.append(x[j-1] / z[j-1])
            sigma.append(b_array[j] / z[j-1])

            #Esa s npi de dónde sale
            q.append(c[j] * y[j-1] + s[j] * d[j])
            x.append(-sigma[j] * y[j-1] + c[j] * d[j])

            if j != n:
                r.append(sigma[j] * b_array[j+1])
                y.append(c[j] * b_array[j+1])

            #Para A^k+1
            z[n] = x[n]
            a_array[0] = sigma[1] * q[0] + c[1] * z[0]
            b_array[0] = sigma[1] * z[1]

            for j in range(1, n-1):
                a_array[j] = sigma[j+1] * q[j] + c[j] * c[j+1] * z[j]
                b_array[j+1] = sigma[j+1] * z[j+1]
            
            a_array[n] = c[n] * z[n]

            k = k + 1

qr(3, [3, 3, 3], [1, 1], 0.001, 100)