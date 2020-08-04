import numpy as np
from map_iterator_2d import *

v = 0 # version
#_______________________________________________________________________________
tau = 2*np.pi
a_weier, b_weier = 0.3, 4
def weierstrass_func(x):
    w = 0
    for n in range(11):
        w += (a_weier**n)*np.cos(tau*(b_weier**n)*x)
    return w

def fractal_map_0(x):
    return (0.55 - 0.385*weierstrass_func(x))/4

def fractal_map_1(x):
    return 0.11053*(1.25 - weierstrass_func(x))
#_______________________________________________________________________________
# modify default values of parameters based on the picked version
if v == 0:
    pass
    
elif v == 1:
    p['r_0'], p['r_1'] = 3.20, 4.0
    p['r_resolution'] = 200
    p['map_X'] = lambda x, y, r: r*logistic(y)*(1 - np.sin(x))
    p['map_Y'] = lambda x, y, r: r*logistic(x)
    
elif v == 2:
    p['r_0'], p['r_1'] = 3.766, 4.117 #4.0, 4.234 #3.766, 4.0
    p['r_resolution'] = 600
    def map_X(x, y, r):
        h = 1 + 2.5*(r - 3.20)
        return np.mod(r*logistic(y)*np.abs(1 - np.sin(h*x)), 1)
    p['map_X'] = map_X
    p['map_Y'] = lambda x, y, r: np.mod(r*logistic(x), 1)

#_______________________________________________________________________________

iterate_map()
