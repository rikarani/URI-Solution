N = int(input())

p100 = N // 100
sisa_N = N % 100

p50 = sisa_N // 50
sisa_N = sisa_N % 50

p20 = sisa_N // 20
sisa_N = sisa_N % 20

p10 = sisa_N // 10
sisa_N = sisa_N % 10

p5 = sisa_N // 5
sisa_N = sisa_N % 5

p2 = sisa_N // 2
sisa_N = sisa_N % 2

p1 = sisa_N // 1
sisa_N = sisa_N % 1

print(N)
print(f"{p100} nota(s) de R$ 100,00")
print(f"{p50} nota(s) de R$ 50,00")
print(f"{p20} nota(s) de R$ 20,00")
print(f"{p10} nota(s) de R$ 10,00")
print(f"{p5} nota(s) de R$ 5,00")
print(f"{p2} nota(s) de R$ 2,00")
print(f"{p1} nota(s) de R$ 1,00")