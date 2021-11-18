angka = int(input())
jam_kerja = int(input())
gaji_per_jam = float(input())

gaji_total = jam_kerja * gaji_per_jam

print(f"NUMBER = {angka}")
print(f"SALARY = U$ {'{0:.2f}'.format(gaji_total)}")