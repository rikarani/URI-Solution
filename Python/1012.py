x = input().split()

A,B,C = x

triangulo = (float(A) * float(C)) / 2
circulo = 3.14159 * float(C) * float(C)
trapezium = ((float(A) + float(B)) * float(C)) / 2
quadrado = float(B) * float(B)
retangulo = float(A) * float(B)

print(f"TRIANGULO: {'{0:.3f}'.format(triangulo)}")
print(f"CIRCULO: {'{0:.3f}'.format(circulo)}")
print(f"TRAPEZIO: {'{0:.3f}'.format(trapezium)}")
print(f"QUADRADO: {'{0:.3f}'.format(quadrado)}")
print((f"RETANGULO: {'{0:.3f}'.format(retangulo)}"))