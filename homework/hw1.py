#%%
import numpy as np
import matplotlib.pyplot as plt
#%%

def f(x):
    '''
    The function f(x)
    '''
    a = 2
    return x**3-a

def df(x):
    '''
    The derivative of f(x)
    '''
    return 3*x**2

<<<<<<< HEAD
def newtonArray(f, df, x0, n):
    '''
    Replace the pass with the code, try replacing Newton's method with a simple relaxation.
    '''
    x = np.zeroes(n+1)
    x[0] = x0
    for k in range(n):
        x[k+1] = x[k] - f(x[k])/df(x[k])

    return x
    
=======
def newtonArray(f, df, x0, tol=1e-8, maxIter=100):
    '''
    tol: tolerance, stop Newton whenever
    |x - x_newton|<tol
    '''
    x = x0
    x_val = np.zeros((maxIter+1, ))
    it = 0 # it is the number of iterations
    x_val[it] = x0
    while np.abs(x - 2**(1/3)) > tol and it < maxIter:
        x -= f(x)/df(x)
        it += 1
        x_val[it] = x
    
    # x -= something means x = x- something
    return x_val
>>>>>>> 8459efca17e04beba486ef4a3a77867381703bc2

def plotError(y, x):
    '''
    Plot the error using matplotlib
    '''
    err = y - x
    plt.semilogy(np.abs(err))
    plt.show() 

def main():
    n = 20
    x0 = 1
    x = newtonArray(f, df, x0, n)
    y = 2**(1/3)
    plotError(y,x)

#%%
if __name__ == "__main__":
    main()
