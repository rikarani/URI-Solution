X = int(input())
Y = int(input())
jumlah = 0

for i in range(Y + 1, X) :
    if i % 2 != 0 :
        jumlah += i

print(jumlah)