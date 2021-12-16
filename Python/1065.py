total = 0

for i in range(5) :
    angka = int(input())

    if (abs(angka) % 2 == 0) :
        total += 1

print(f"{total} valores pares")