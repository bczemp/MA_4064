def euler(f, t, y, h):
    der = f(y)
    new_y = [y[i] + h * der[i] for i in range(len(y))]
    return [t + h, new_y]

def rk4(f, t, y, h):
    k1 = f(y)
    k2 = f([y[i] + h * k1[i]/2 for i in range(len(y))])
    k3 = f([y[i] + h * k2[i]/2 for i in range(len(y))])
    k4 = f([y[i] + h * k3[i] for i in range(len(y))]) 
    
    new_y = [y[i] + h/6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(len(y))]

    return [t + h, new_y]

def rkdp(f, t, y, dt, error=1e-6):
    pass
    
