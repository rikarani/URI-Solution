nama = input()
gaji_karyawan = float(input())
total_penjualan = float(input())

total_gaji = gaji_karyawan + (total_penjualan * 0.15)

print(f"TOTAL = R$ {'{0:.2f}'.format(total_gaji)}")