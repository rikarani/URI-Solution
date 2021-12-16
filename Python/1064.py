positif = 0
rata_rata = 0


for i in range(1,7) :
    angka = float(input())

    if (angka > 0) :
        rata_rata += angka
        positif += 1

print(f"{positif} valores positivos")
print(f"{'{0:.1f}'.format(rata_rata / positif)}")