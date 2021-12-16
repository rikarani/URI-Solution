dia,hari1 = input().split()
hari1 = int(hari1)
jam1, menit1, detik1 = map(int, input().split(" : "))

dia,hari2 = input().split()
hari2 = int(hari2)
jam2, menit2, detik2 = map(int, input().split(" : "))

detik = detik2 - detik1
menit = menit2 - menit1
jam = jam2 - jam1
hari = hari2 - hari1

if detik < 0 :
    detik += 60
    menit -= 1

if menit < 0 :
    menit += 60
    jam -= 1

if jam < 0 :
    jam += 24
    hari -= 1

print(f"{hari} dia(s)")
print(f"{jam} hora(s)")
print(f"{menit} minuto(s)")
print(f"{detik} segundo(s)")