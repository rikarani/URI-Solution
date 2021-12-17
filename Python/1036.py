A, B, C = list(map(float, input().split()))

D = (B * B) - (4 * A * C)

E = pow(D, .5)

if ((D < 0) or (A == 0)) :
    print("Impossivel calcular")
else :
    R1 = (-B + E) / (2 * A)
    R2 = (-B - E) / (2 * A)

    print(f"R1 = {'{0:.5f}'.format(R1)}")
    print(f"R2 = {'{0:.5f}'.format(R2)}")