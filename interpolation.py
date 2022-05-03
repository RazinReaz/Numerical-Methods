import numpy as np
import matplotlib.pyplot as plt

def choose(points, n, pivot):
    '''Picks n elements from the points array with pivot in the middle'''
    begin = pivot-n//2
    if n%2==0 :
        end = pivot+n//2-1
    else:
        end = pivot+n//2
    return points[begin:end+1]

def closestPoints(points, x, n):
    '''Picks n closest points from x in the points array'''
    for i in range(len(points)):
        if x < points[i][0]:
            return choose(points,n,i)
    

def interpolation(p, x, n = None, printTable = False):
    ''' p   : array of (x,y) tupples
        x   : the x at which the result will be evaluated
        n   : will default to the number of points
        
        returns : the value of f(x)'''
    if n is None:
        n = len(p)
    else:
        p.sort(key=lambda p: p[0])
        p = closestPoints(p, x, n)
    

    diff = np.zeros((n, n))
    for i in range(n):
        diff[i, 0] = p[i][1]  # putting the y values in the first column

    for col in range(1, n):
        for row in range(0, n-col):
            diff[row, col] = (diff[row, col-1] - diff[row+1, col-1])/(p[row][0]-p[row+col][0])

    if printTable:
        print(diff)

    #formula
    result = 0
    for j in range(n):
        mul = 1
        for i in range(j):
            mul *= (x-p[i][0])  # p[i][0] is the x value of the ith point
        result += mul*diff[0, j]
    return result


def plotFunctionByInterpolation(points, start=0, end=100, label = "Function"):
    '''
    Plots the function from the given points
    points  : array of (x,y) points to be interpolated
    start   : start of the x value in the plot
    end     : end of the x value in the plot
    '''
    x = np.linspace(start, end, 100)
    X = [i[0] for i in points]
    Y = [i[1] for i in points]
    plt.plot(x, interpolation(points, x), label = label)
    plt.scatter(X, Y)
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    p = [(10,227.04), (15,362.78), (20,517.35), (22.5,602.97)]
    print(interpolation(p,16))
    plotFunctionByInterpolation(p,0,50)