import numpy as np
import matplotlib.pyplot as plt

p = { # parameters
    'N_iter': 300, # number of iterations of the map
    'discard': 30, # how many initial iterations to discard while drawing
    'X_init': 0.5, # initial value
    'r_resolution': 2000, # x axis resolution
    'map': None, # the map to be iterated
    'r_0': 0.0, # lower limit of x axis
    'r_1': 4.0, # upper limit of x axis
}

def logistic(x):
    return x*(1 - x)

p['map'] = lambda x, r: r*logistic(x)

perc = (5/100)*p['r_resolution']
def iterate_map():
    X = np.zeros((p['N_iter'],))
    X[0] = p['X_init']
    
    r_optvar = p['r_1'] - p['r_0']
    for k in range(p['r_resolution']):
        if k%perc == 0: print(str(100*k/p['r_resolution']) + '%')
        r = p['r_0'] + r_optvar*k/(p['r_resolution'] - 1)
        
        for n in range(p['N_iter'] - 1):
            X[n+1] = p['map'](X[n], r)
        
        Z = X[p['discard']:]
        plt.plot(r*np.ones(Z.shape), Z, linestyle='none',
            marker='.', markersize=0.1, color='black')
    print(str(100.0) + '%')
    plt.show()
