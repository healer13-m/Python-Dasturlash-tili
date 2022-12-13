import math
x=0.1722
y=6.33
z=0.001325
gamma=5*math.atan(x)-(1/4)*math.acos(x)*((x+3*math.fabs(x-y)+x**2)/(math.fabs(x-y)*z+x**2))
print(gamma)
