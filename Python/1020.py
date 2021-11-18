umur = int(input())

tahun = umur // 365
sisa_umur = umur % 365

bulan = sisa_umur // 30
sisa_umur = sisa_umur % 30

hari = sisa_umur

print(f"{tahun} ano(s)")
print(f"{bulan} mes(es)")
print(f"{hari} dia(s)")