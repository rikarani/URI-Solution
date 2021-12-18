gaji_karyawan = float(input())

if 0 <= gaji_karyawan <= 400.00 :
    gaji_tambahan = 0.15 * gaji_karyawan

    print(f"Novo salario: {'{0:.2f}'.format(gaji_karyawan + gaji_tambahan)}")
    print(f"Reajuste ganho: {'{0:.2f}'.format(gaji_tambahan)}")
    print(f"Em percentual: 15 %")
elif 400.01 <= gaji_karyawan <= 800.00 :
    gaji_tambahan = 0.12 * gaji_karyawan

    print(f"Novo salario: {'{0:.2f}'.format(gaji_karyawan + gaji_tambahan)}")
    print(f"Reajuste ganho: {'{0:.2f}'.format(gaji_tambahan)}")
    print(f"Em percentual: 12 %")
elif 800.01 <= gaji_karyawan <= 1200.00 :
    gaji_tambahan = 0.10 * gaji_karyawan

    print(f"Novo salario: {'{0:.2f}'.format(gaji_karyawan + gaji_tambahan)}")
    print(f"Reajuste ganho: {'{0:.2f}'.format(gaji_tambahan)}")
    print(f"Em percentual: 10 %")
elif 1200.01 <= gaji_karyawan <= 2000.00 :
    gaji_tambahan = 0.07 * gaji_karyawan

    print(f"Novo salario: {'{0:.2f}'.format(gaji_karyawan + gaji_tambahan)}")
    print(f"Reajuste ganho: {'{0:.2f}'.format(gaji_tambahan)}")
    print(f"Em percentual: 7 %")
else :
    gaji_tambahan = 0.04 * gaji_karyawan

    print(f"Novo salario: {'{0:.2f}'.format(gaji_karyawan + gaji_tambahan)}")
    print(f"Reajuste ganho: {'{0:.2f}'.format(gaji_tambahan)}")
    print(f"Em percentual: 4 %")