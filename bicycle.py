import numpy as np
from matplotlib import pyplot as pp

#Given
v_0 = 4
m = 70
P = 400
dt = 0.1
t_f = 200

#Making Arrays
t = np.arange(0, t_f + dt, dt)
v = np.zeros_like(t)
v[0] = v_0

#Euler 
for i in range(len(t)-1):
    v[i+1] = v[i] + dt * (P / (m*v[i]))
    
pp.figure()
pp.plot(t,v)
pp.xlabel("Time t (s)")
pp.ylabel("Velocity v (m/s)")
pp.title ("Cycling Without Drag")
pp.grid(True)
pp.show()