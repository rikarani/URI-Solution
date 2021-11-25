A,B,C = map(float,input().split())

if ((A < (B + C)) and (B < (A + C)) and (C < (A + B))) :
    print(f"Perimetro = {'{0:.1f}'.format(A + B + C)}")
else :
    print(f"Area = {'{0:.1f}'.format(((A + B) * C) / 2)}")