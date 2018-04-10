# Alex Stewart
# Module
# April, 2018

# Module for basic special relativistic computations
# Group members: Savannah, Ryan, Mason, Alex

# velocities need to be in fraction of speed of light
# mass needs to be in kg

from math import sqrt

c = 3.e8

def interval(dt,dx,dy,dz):
    inter = -1*dt**2 + dx**2 + dy**2 + dz**2
    return inter
    
def tdil(dt,v):
    time = dt/sqrt(1 - v**2)
    return time
    
def dcon(l,v):
    x = l/sqrt(1 - v**2)
    return x
    
def velcomp(W,v):
    vel = (W + v)/(1 + (W*v))
    return vel
    
def massenergy(m):
    energy = m*c**2
    return energy
    
def kinetic(m,v):
    KE = m*c**2*(1/sqrt(1-v**2) - 1)
    return KE
    
def reldoppleraway(wl,v):
    wl_obs = wl*sqrt(1+v)/sqrt(1-v)
    return wl_obs
    
def reldopplerto(wl,v):
    wl_obs = wl*sqrt(1-v)/sqrt(1+v)
    return wl_obs