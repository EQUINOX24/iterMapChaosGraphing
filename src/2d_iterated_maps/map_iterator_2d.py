import numpy as np
import matplotlib.pyplot as plt

p = { # parameters
    'N_iter': int(8e+4), # number of iterations of the map
    'discard': 30, # how many initial iterations to discard while drawing
    'X_init': 0.9, # initial value of X
    'Y_init': 0.2, # initial value of Y
    'r_resolution': 300, # x axis resolution
    'map_X': None, # X component of the 2D->2D map to be iterated
    'map_Y': None, # Y component of the 2D->2D map to be iterated
    'r_0': 3.0, # lower limit of x axis
    'r_1': 4.0, # upper limit of x axis
}

def logistic(x):
    return x*(1 - x)

def map_X(x, y, r):
    return np.mod(r*logistic(y) + x, 1)

def map_Y(x, y, r):
    return r*logistic(x)

p['map_X'] = map_X
p['map_Y'] = map_Y

perc = (5/100)*p['r_resolution']
def iterate_map():
    X, Y = np.zeros((p['N_iter'],)), np.zeros((p['N_iter'],))
    X[0], Y[0] = p['X_init'], p['Y_init']
    
    r_optvar = p['r_1'] - p['r_0']
    for k in range(p['r_resolution']):
        if k%perc == 0: print(str(100*k/p['r_resolution']) + '%')
        r = p['r_0'] + r_optvar*k/(p['r_resolution'] - 1)
        
        for n in range(p['N_iter'] - 1):
            X[n+1] = p['map_X'](X[n], Y[n], r)
            Y[n+1] = p['map_Y'](X[n], Y[n], r)
        
        #%matplotlib notebook
        plt.plot(X[p['discard']:], Y[p['discard']:],
            linestyle='none', marker='.', markersize=0.4)
        plt.axis([0, 1, 0, 1])
        plt.gca().set_aspect('equal', adjustable='box')
        
        plt.savefig('./frames/frame '+str(k)+'.png')
        plt.cla()
