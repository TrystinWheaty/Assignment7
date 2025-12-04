import numpy as np
import math
from matplotlib import pyplot as pp
from creategrid import qgrid as qg

#Constants
epsilon_0 = 8.854e-12

#imported data
data = qg(50)
q = np.array(data['charges'])
pos = np.array(data['coordinates'])

#creating grid
x_list = np.arange(-10, 10, 0.1)
y_list = np.arange(-20, 20, 0.1)

X, Y = np.meshgrid(x_list, y_list)

#Calculating potential
Vtot = np.zeros_like(X)

for qi, (cx, cy) in zip(q, pos):
    r = np.sqrt((X - cx)**2 + (Y - cy)**2)
    #preventing r<0.2, makes the plot look better
    r[r < 0.2] = 0.2
    Vtot += qi / (4 * math.pi * epsilon_0 * r)

#Graphing Electric Potential
pp.figure(figsize=(10, 8))
PotentialPlot = pp.contourf(X, Y, Vtot, levels=100, cmap='coolwarm')
pp.xlabel('x position (m)')
pp.ylabel('y position (m)')
mycb = pp.colorbar(PotentialPlot,label="Electric Potential (V)")
pp.savefig("potential.png")
#pp.show()

#Computing Electric fields..the right way this time
dx = x_list[1] - x_list[0]
dy = y_list[1] - y_list[0]

Ey, Ex = np.gradient(-Vtot, dy, dx)




#Plotting Electric field, attempted quiver plot this time. 
step = 10 #showing less arrows

pp.figure(figsize=(11, 7))
# Combined plot
pp.figure(figsize=(10, 6))

pp.quiver(X[::step, ::step], Y[::step, ::step], Ex[::step, ::step], Ey[::step, ::step],
    color='black', scale=1e11, width=0.003, pivot='mid')

# Plot charges
for qi, (cx, cy) in zip(q, pos):
    pp.scatter(cx, cy,
               c='red' if qi > 0 else 'blue',
               s=60, edgecolor='white', linewidth=0.7)
    
pp.xlabel("x position (m)")
pp.ylabel("y position (m)")
pp.title("Electric Field")
pp.tight_layout()
pp.savefig("electricfield.png")
#pp.show
