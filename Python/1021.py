N = float(input())

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

koin_N = int(N * 100)
koin_N = koin_N % 100

p050 = koin_N // 50
koin_N = koin_N % 50

p025 = koin_N // 25
koin_N = koin_N % 25

p010 = koin_N // 10
koin_N = koin_N % 10

p005 = koin_N // 5
koin_N = koin_N % 5

p001 = koin_N // 1
koin_N = koin_N % 1

print("NOTAS:")
print(f"{int(p100)} nota(s) de R$ 100.00")
print(f"{int(p50)} nota(s) de R$ 50.00")
print(f"{int(p20)} nota(s) de R$ 20.00")
print(f"{int(p10)} nota(s) de R$ 10.00")
print(f"{int(p5)} nota(s) de R$ 5.00")
print(f"{int(p2)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(p1)} moeda(s) de R$ 1.00")
print(f"{int(p050)} moeda(s) de R$ 0.50")
print(f"{int(p025)} moeda(s) de R$ 0.25")
print(f"{int(p010)} moeda(s) de R$ 0.10")
print(f"{int(p005)} moeda(s) de R$ 0.05")
print(f"{int(p001)} moeda(s) de R$ 0.01")