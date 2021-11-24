from math import pow as pangkat, sqrt
from math import sqrt as akar

var1 = input().split()
var2 = input().split()

x1,y1 = var1
x2,y2 = var2

p1 = pangkat(float(x2) - float(x1),2)
p2 = pangkat(float(y2) - float(y1),2)

distance = akar(p1 + p2)

print(f"{'{0:.4f}'.format(distance)}")