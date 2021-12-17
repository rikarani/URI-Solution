A, B, C = list(map(float, input().split()))

daftarNilai = [A,B,C]
daftarNilai.sort(reverse=True)

if daftarNilai[0] >= (daftarNilai[1] + daftarNilai[2]) :
    print("NAO FORMA TRIANGULO")
elif (daftarNilai[0]**2) == ((daftarNilai[1] ** 2) + (daftarNilai[2] ** 2)) :
    print("TRIANGULO RETANGULO")
elif (daftarNilai[0]**2) > ((daftarNilai[1] ** 2) + (daftarNilai[2] ** 2)) :
    print("TRIANGULO OBTUSANGULO")
elif (daftarNilai[0]**2) < ((daftarNilai[1] ** 2) + (daftarNilai[2] ** 2)) :
    print("TRIANGULO ACUTANGULO")

if (daftarNilai[0] == daftarNilai[1]) and (daftarNilai[1] == daftarNilai[2]) :
    print("TRIANGULO EQUILATERO")
elif (daftarNilai[0] == daftarNilai[1]) or (daftarNilai[1] == daftarNilai[2]) :
    print("TRIANGULO ISOSCELES")