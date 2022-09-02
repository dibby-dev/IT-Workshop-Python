mass = int(input('Enter mass: '))
height = int(input('Enter height: '))
velocity = int(input('Enter velocity: '))
g = 9.8
KE = (0.5)*mass*velocity*velocity
PE = mass*g*height
print("Kinetic Energy: {}J".format(KE))
print("Potential Energy: {}J".format(PE))