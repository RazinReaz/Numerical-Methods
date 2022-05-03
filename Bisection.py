def bisection(f, xlo, xhi, precision=1e-5):
    '''f is the function with x where we want to find
    the roots when f = 0. 
    xlo and xhi are the range within which
    we are searching for the root. 
    precision is for precision'''

    while xhi-xlo > precision:
        xmid = (xhi+xlo)/2
        fhi = f(xhi)
        flo = f(xlo)
        fmid = f(xmid)

        if(flo*fmid<0):
            #root is between lo and mid
            xhi = xmid
        elif(fmid*fhi<0):
            #root is between hi and mid
            xlo = xmid
        elif(fmid==0):
            return xmid
    return xmid
        