import numpy as np
from matplotlib import pyplot as pp

m = 2
k = 3
t_i = 2
t_f = 20
dt = 0.1
steps = int((t_f - t_i)/dt)
V_i = 0
C_0 = 0 
C_critdamp = np.sqrt(4*k*m)
C_undamp = (1/5)*C_critdamp
C_overdamp = 2*C_critdamp
Y = [2]
V = [0]
t = [0]


def y_ode(v):
    return v

def V_ode(v,y):
    return -(C_overdamp/m) * v - (k / m)*y

def y_euler(y,v):
    k1 = dt * y_ode(v)
    return y + k1

def V_euler(v,y):
    k1 = dt * V_ode(v,y)
    return v + k1

for i in range(steps):
    V.append(V_euler(V[-1], Y[-1]))
    Y.append(y_euler(Y[-1],V[-1]))
    t.append(dt*(i+1))

Y = np.array(Y)
t = np.array(t)

pp.plot(t, Y)
pp.xlabel('Time t (s)')
pp.ylabel('Displacement y (m)')
pp.title ('Harmonic Oscillator Overdamped')
pp.show()

