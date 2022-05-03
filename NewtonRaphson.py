def newtonRaphson(f, x, precision=1e-9):
    xold = xnew = x
    delta = 1e-9
    rdelta = 1/delta
    while f(xnew) > precision:
        xold = xnew
        fx = f(xold)
        
        #derivative
        y1 = f(xold+delta)-f(xold-delta)
        y2 = f(xold+2*delta)-f(xold-2*delta)
        dfx = (y2+8*y1)*rdelta/12
        #dfx = (f(xold+delta)-fx)*rdelta
        xnew = xold - fx/dfx
    return xnew
