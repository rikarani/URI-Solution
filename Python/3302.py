N = int(input())

daftar = []

for _ in range(N) :
    daftar.append(input())

for i in range(len(daftar)) :
    print(f"resposta {i+1}: {daftar[i]}")