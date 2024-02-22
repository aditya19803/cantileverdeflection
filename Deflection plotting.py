import numpy as np
import matplotlib.pyplot as plt


def deflection_plotting():
  l = float(input('enter the length of the beam: '))	# meters
  w = float(input('enter the width of the beam: '))	# meters
  h = float(input('enter the height of the beam: '))	# meters
  P = float(input('enter the point load acting on the beam: '))		# N/m^2
  E = float(input('enter the Modulus of Elasticity of the beam: '))	# N
  points_on_beam = int(input('enter the number of the point on beam: '))	# meters
  
  A = w*h
  deflection_values = np.array([])
  L = np.array([])
  
  for i in range(1, points_on_beam + 1):
    l = i/points_on_beam
    y = h/2
    I = A*y**2
    d = (P*l**3)/(3*E*I)
    L = np.append(L, l)
    deflection_values = np.append(deflection_values, d)
    print("Deflection at point", i, ":", d, "meters")
  
  plt.plot(L, deflection_values)
  plt.xlabel('Point load location (N)')
  plt.ylabel('Deflection (meters)')
  plt.show()


deflection_plotting()
