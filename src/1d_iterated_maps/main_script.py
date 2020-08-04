import numpy as np
from map_iterator_1d import *

v = 9 # version
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

def Saw_wave(x):
    return (x + 1)%2 - 1
#_______________________________________________________________________________
# modify default values of parameters based on the picked version
if v == 0:
    pass
    
elif v == 1:
    p['r_0'], p['r_1'] = 0.1, 1.9
    def A(x, r):
        return 4 - 0.8*(r - p['r_0'])/(p['r_1'] - p['r_0'])
    p['map'] = lambda x, r: \
        A(x, r)*logistic(np.power(x, r))
    
elif v == 2:
    p['r_0'], p['r_1'] = 0.1, 1.9
    def A(x, r):
        return 4 - 0.1*r - 0.4*np.square(np.sin(2*r**2))/(r + 0.1)
    p['map'] = lambda x, r: \
        A(x, r)*logistic(np.power(x, r))
    
elif v == 3:
    p['r_0'], p['r_1'] = 0.2, 1.8
    def A(x, r):
        return (3.8 + 0.2*np.sin(7*np.pi*r))
    p['map'] = lambda x, r: \
        A(x, r)*logistic(np.power(x, r))
    
elif v == 4:
    p['r_0'], p['r_1'] = 0.2, 1.8
    def A(x, r):
        return 3.85 + 0.05*np.sin(7*np.pi*r)
    p['map'] = lambda x, r: \
        A(x, r)*logistic(np.power(x, r))
    
elif v == 5:
    p['r_0'], p['r_1'] = 0.2, 1.8
    def A(x, r):
        return 3.75 + 0.03*np.sin(5*np.pi*r)
    p['map'] = lambda x, r: \
        A(x, r)*logistic(np.power(x, r))
    
elif v == 6:
    p['r_0'], p['r_1'] = 0.2, 1.8
    def A(x, r):
        return 3.79 + 0.02*np.arcsin(np.sin(5*np.pi*r))
    p['map'] = lambda x, r: \
        A(x, r)*logistic(np.power(x, r))
    
elif v == 7:
    p['r_0'], p['r_1'] = 1.0, 4.0
    N_iter = 600
    p['r_resolution'] = 6000
    def A(x, r):
        return r*(1 - np.cos(5*np.pi*x)**2/8)
    p['map'] = lambda x, r: \
        A(x, r)*logistic(x)
    
elif v == 8:
    p['r_0'], p['r_1'] = 1.5, 4.0
    p['N_iter'] = 600
    p['map'] = lambda x, r: r*fractal_map_0(x)
    
elif v == 9:
    p['r_0'], p['r_1'] = 2.0, 4.0
    #p['r_0'], p['r_1'] = 3.1, 3.3
    #p['r_0'], p['r_1'] = 3.18, 3.23
    #p['r_0'], p['r_1'] = 3.2082, 3.2135
    #p['r_0'], p['r_1'] = 3.21178, 3.21192 #y [0.455, 0.458]
    #p['r_0'], p['r_1'] = 3.211841, 3.211848 #y [0.45575, 0.45625]
    
    p['N_iter'] = 600
    a_weier = 0.2
    p['map'] = lambda x, r: r*fractal_map_1(x)
    
elif v == 10:
    p['r_0'], p['r_1'] = 0.5, 1.0
    p['N_iter'] = 800
    p['map'] = lambda x, r: \
        (1 + 3*r)*(Saw_wave(x + r))**3/4
    
elif v == 11:
    p['r_0'], p['r_1'] = 0.7, 0.95
    p['N_iter'] = 600
    def the_map(x, r):
        var = np.sin(np.pi*((x + r - 1)%2 - 1)**3 + r)
        return (1 + 3*r)*var/4
    p['map'] = the_map
#_______________________________________________________________________________

iterate_map()
