N = int(input())
listku = []
hitung = 0
angka = 0

for i in range(N) :
    nilai = int(input())
    listku.append(nilai)

while hitung != len(listku) :
    if (listku[angka] < 0) and (listku[angka] % 2 != 0) :
        print("ODD NEGATIVE")
    elif (listku[angka] < 0) and listku[angka] % 2 == 0 :
        print("EVEN NEGATIVE")
    elif (listku[angka] > 0) and listku[angka] % 2 != 0 :
        print("ODD POSITIVE")
    elif (listku[angka] > 0) and listku[angka] % 2 == 0 :
        print("EVEN POSITIVE")
    elif listku[angka] == 0 :
        print("NULL")
    

    angka += 1
    hitung += 1